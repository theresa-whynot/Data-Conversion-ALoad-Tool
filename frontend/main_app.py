"""
Simple Streamlit frontend for running a-load generation scripts.

Pick an a-load mapping, provide source and target Excel paths, then generate.
"""

from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
ALG_DIR = ROOT / "backend" / "advanced_load_generation"
if str(ALG_DIR) not in sys.path:
    sys.path.insert(0, str(ALG_DIR))

from aload_runner import describe_script, list_aload_scripts, run_aload


st.set_page_config(
    page_title="A-Load Generator",
    page_icon="📄",
    layout="centered",
)

st.title("A-Load Generator")
st.caption(
    "Select an a-load mapping, enter source and target Excel paths, then generate."
)

scripts = list_aload_scripts()
if not scripts:
    st.error("No dynamic a-load scripts were found.")
    st.stop()

with st.sidebar:
    st.header("Browse")
    query = st.text_input("Filter scripts", placeholder="e.g. SUP02 or HCM01")
    filtered = [
        name
        for name in scripts
        if not query or query.lower() in name.lower()
    ]
    st.write(f"{len(filtered)} of {len(scripts)} scripts")

script_name = st.selectbox(
    "A-load script",
    options=filtered or scripts,
    index=0,
    help="Mappings come from backend/advanced_load_generation/dynamic/",
)

# Prefill path fields from the script defaults when the selection changes.
if "selected_script" not in st.session_state:
    st.session_state.selected_script = script_name

meta = None
try:
    meta = describe_script(script_name)
except Exception as exc:  # noqa: BLE001 - show any load/config issue in the UI
    st.warning(f"Could not inspect script defaults: {exc}")

if script_name != st.session_state.selected_script:
    st.session_state.selected_script = script_name
    if meta:
        st.session_state.source_path = meta.get("default_source_file") or ""
        st.session_state.target_path = meta.get("default_target_file") or ""

if "source_path" not in st.session_state:
    st.session_state.source_path = (meta or {}).get("default_source_file") or ""
if "target_path" not in st.session_state:
    st.session_state.target_path = (meta or {}).get("default_target_file") or ""

source_path = st.text_input(
    "Source file path",
    key="source_path",
    placeholder=r"C:\path\to\source.xlsx",
)
target_path = st.text_input(
    "Target file path",
    key="target_path",
    placeholder=r"C:\path\to\target_aload.xlsx",
)

if meta and meta.get("sheets"):
    st.info("Target sheets: " + ", ".join(meta["sheets"]))

col_run, col_hint = st.columns([1, 2])
with col_run:
    run_clicked = st.button("Generate a-load", type="primary", use_container_width=True)
with col_hint:
    st.caption("Writes into the existing target workbook using the selected mapping.")

if run_clicked:
    if not source_path.strip() or not target_path.strip():
        st.error("Both source and target file paths are required.")
    else:
        with st.spinner(f"Running {script_name}..."):
            try:
                output = run_aload(script_name, source_path.strip(), target_path.strip())
            except FileNotFoundError as exc:
                st.error(str(exc))
            except Exception as exc:  # noqa: BLE001 - surface transfer failures
                st.exception(exc)
            else:
                st.success(f"Finished generating `{script_name}`.")
                if output:
                    st.code(output, language="text")
                st.write(f"Updated target file: `{target_path.strip()}`")

st.divider()
st.markdown(
    """
**Notes**
- Paths can be local or OneDrive/synced folders available to this machine.
- Script mappings are unchanged; only the source/target paths are overridden at run time.
- A database is not required for this flow. Job history or saved presets can be added later.
"""
)
