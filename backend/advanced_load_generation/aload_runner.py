"""
Discover and run a-load dynamic scripts with caller-provided source/target paths.

Dynamic scripts keep their sheet mappings/filters/defaults as module-level config.
This runner intercepts their module-level transfer call, then re-runs the transfer
with the paths supplied by the frontend (or CLI).
"""

from __future__ import annotations

import importlib.util
import io
import re
import sys
from contextlib import redirect_stdout
from pathlib import Path
from typing import Iterable

from a_load_generation import transfer_data_multiple_sheets

DYNAMIC_DIR = Path(__file__).resolve().parent / "dynamic"
SCRIPT_PREFIX = "a_load_generation_"


def list_aload_scripts() -> list[str]:
    """Return display names for available dynamic a-load scripts, sorted."""
    names: list[str] = []
    for path in DYNAMIC_DIR.glob(f"{SCRIPT_PREFIX}*.py"):
        names.append(path.stem.removeprefix(SCRIPT_PREFIX))
    return sorted(names)


def resolve_script_path(script_name: str) -> Path:
    """Map a display name (e.g. SUP02_Supplier_Emails) to its script path."""
    cleaned = script_name.strip()
    if cleaned.endswith(".py"):
        cleaned = Path(cleaned).stem
    if cleaned.startswith(SCRIPT_PREFIX):
        cleaned = cleaned.removeprefix(SCRIPT_PREFIX)

    path = DYNAMIC_DIR / f"{SCRIPT_PREFIX}{cleaned}.py"
    if not path.is_file():
        raise FileNotFoundError(f"A-load script not found: {cleaned}")
    return path


def _load_script_config(script_path: Path) -> dict:
    """
    Import a dynamic script without writing Excel output, capturing its transfer args.
    """
    parent_dir = str(script_path.parent.parent)
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)

    captured: dict = {}

    def _capture(
        source_file,
        target_file,
        sheet_column_map,
        filters,
        header_rows,
        default_columns,
    ):
        captured["sheet_column_map"] = sheet_column_map
        captured["filters"] = filters
        captured["header_rows"] = header_rows
        captured["default_columns"] = default_columns
        captured["default_source_file"] = source_file
        captured["default_target_file"] = target_file

    # Patch before the script does `from a_load_generation import transfer_data_multiple_sheets`
    import a_load_generation as alg

    original = alg.transfer_data_multiple_sheets
    alg.transfer_data_multiple_sheets = _capture

    module_name = f"aload_dynamic_{script_path.stem}_{id(script_path)}"
    try:
        spec = importlib.util.spec_from_file_location(module_name, script_path)
        if spec is None or spec.loader is None:
            raise ImportError(f"Unable to load script: {script_path}")
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
    finally:
        alg.transfer_data_multiple_sheets = original
        sys.modules.pop(module_name, None)

    required = (
        "sheet_column_map",
        "filters",
        "header_rows",
        "default_columns",
    )
    missing = [key for key in required if key not in captured]
    if missing:
        raise RuntimeError(
            f"Script did not call transfer_data_multiple_sheets as expected "
            f"({script_path.name}). Missing: {', '.join(missing)}"
        )
    return captured


def run_aload(
    script_name: str,
    source_file: str,
    target_file: str,
) -> str:
    """
    Run the selected a-load using the script's mappings and the provided paths.

    Returns captured stdout from the transfer for UI display.
    """
    source_path = Path(source_file).expanduser()
    target_path = Path(target_file).expanduser()

    if not source_path.is_file():
        raise FileNotFoundError(f"Source file not found: {source_path}")
    if not target_path.is_file():
        raise FileNotFoundError(f"Target file not found: {target_path}")

    script_path = resolve_script_path(script_name)
    config = _load_script_config(script_path)

    buffer = io.StringIO()
    with redirect_stdout(buffer):
        transfer_data_multiple_sheets(
            str(source_path),
            str(target_path),
            config["sheet_column_map"],
            config["filters"],
            config["header_rows"],
            config["default_columns"],
        )
    return buffer.getvalue().strip()


def describe_script(script_name: str) -> dict:
    """Return script metadata including hardcoded default paths and target sheets."""
    script_path = resolve_script_path(script_name)
    config = _load_script_config(script_path)
    return {
        "name": script_name,
        "path": str(script_path),
        "default_source_file": config.get("default_source_file"),
        "default_target_file": config.get("default_target_file"),
        "sheets": sorted(config["sheet_column_map"].keys()),
    }


def filter_scripts(query: str | None = None, scripts: Iterable[str] | None = None) -> list[str]:
    """Optional case-insensitive filter helper for the UI."""
    items = list(scripts) if scripts is not None else list_aload_scripts()
    if not query:
        return items
    pattern = re.compile(re.escape(query.strip()), re.IGNORECASE)
    return [name for name in items if pattern.search(name)]
