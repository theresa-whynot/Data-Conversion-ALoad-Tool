"""
Streamlit frontend for running one or many a-load generation scripts.

Each section picks an a-load mapping, Client File Spec, and Blank A-Load.
Sections are add-only; generate individually or all at once.
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


def pick_excel_file(title: str) -> str:
    """Open a local OS file dialog and return the selected Excel path."""
    try:
        import tkinter as tk
        from tkinter import filedialog
    except Exception as exc:  # noqa: BLE001
        st.error(f"File browser unavailable in this environment: {exc}")
        return ""

    root = tk.Tk()
    root.withdraw()
    try:
        root.wm_attributes("-topmost", 1)
    except tk.TclError:
        pass

    path = filedialog.askopenfilename(
        title=title,
        filetypes=[
            ("Excel files", "*.xlsx *.xlsm *.xls"),
            ("All files", "*.*"),
        ],
    )
    root.destroy()
    return path or ""


def new_job(job_id: int, default_script: str) -> dict:
    return {
        "id": job_id,
        "script": default_script,
        "source": "",
        "target": "",
    }


def ensure_job_state(job: dict, default_script: str) -> None:
    job_id = job["id"]
    script_key = f"script_{job_id}"
    source_key = f"source_{job_id}"
    target_key = f"target_{job_id}"

    if script_key not in st.session_state:
        st.session_state[script_key] = job.get("script") or default_script
    if source_key not in st.session_state:
        st.session_state[source_key] = job.get("source", "")
    if target_key not in st.session_state:
        st.session_state[target_key] = job.get("target", "")


def sync_job_from_widgets(job: dict) -> None:
    job_id = job["id"]
    job["script"] = st.session_state.get(f"script_{job_id}", job.get("script", ""))
    job["source"] = st.session_state.get(f"source_{job_id}", job.get("source", ""))
    job["target"] = st.session_state.get(f"target_{job_id}", job.get("target", ""))


def run_one_job(job: dict) -> tuple[bool, str]:
    """Run a single a-load job. Returns (ok, message)."""
    script_name = (job.get("script") or "").strip()
    source_path = (job.get("source") or "").strip()
    target_path = (job.get("target") or "").strip()

    if not script_name:
        return False, "A-load script is required."
    if not source_path or not target_path:
        return False, "Both Client File Spec and Blank A-Load are required."

    try:
        output = run_aload(script_name, source_path, target_path)
    except FileNotFoundError as exc:
        return False, str(exc)
    except Exception as exc:  # noqa: BLE001
        return False, f"{type(exc).__name__}: {exc}"

    message = f"Finished generating `{script_name}` → `{target_path}`"
    if output:
        message = f"{message}\n{output}"
    return True, message


scripts = list_aload_scripts()
if not scripts:
    st.error("No dynamic a-load scripts were found.")
    st.stop()

if "jobs" not in st.session_state:
    st.session_state.jobs = [new_job(0, scripts[0])]
if "next_job_id" not in st.session_state:
    st.session_state.next_job_id = 1

st.title("A-Load Generator")
st.caption(
    "Add one or more a-load sections, choose files from your computer, "
    "then generate individually or all at once."
)

with st.sidebar:
    st.header("Browse")
    query = st.text_input("Filter scripts", placeholder="e.g. SUP02 or HCM01")
    filtered = [
        name
        for name in scripts
        if not query or query.lower() in name.lower()
    ]
    st.write(f"{len(filtered)} of {len(scripts)} scripts available")
    st.caption("Use the filter to narrow the dropdown options in each section.")

script_options = filtered or scripts

for index, job in enumerate(st.session_state.jobs):
    job_id = job["id"]
    ensure_job_state(job, script_options[0])

    st.markdown(f"### A-load {index + 1}")

    current_script = st.session_state[f"script_{job_id}"]
    if current_script not in script_options:
        options = [current_script] + script_options
    else:
        options = script_options

    st.selectbox(
        "A-load script",
        options=options,
        key=f"script_{job_id}",
        help="Mappings come from backend/advanced_load_generation/dynamic/",
    )

    meta = None
    try:
        meta = describe_script(st.session_state[f"script_{job_id}"])
    except Exception as exc:  # noqa: BLE001
        st.warning(f"Could not inspect script defaults: {exc}")

    src_col, src_btn_col = st.columns([4, 1])
    with src_col:
        st.text_input(
            "Client File Spec",
            key=f"source_{job_id}",
            placeholder=r"C:\path\to\client_file_spec.xlsx",
        )
    with src_btn_col:
        st.write("")
        if st.button("Browse", key=f"browse_source_{job_id}", use_container_width=True):
            path = pick_excel_file("Select Client File Spec")
            if path:
                st.session_state[f"source_{job_id}"] = path
                st.rerun()

    tgt_col, tgt_btn_col = st.columns([4, 1])
    with tgt_col:
        st.text_input(
            "Blank A-Load",
            key=f"target_{job_id}",
            placeholder=r"C:\path\to\blank_aload.xlsx",
        )
    with tgt_btn_col:
        st.write("")
        if st.button("Browse", key=f"browse_target_{job_id}", use_container_width=True):
            path = pick_excel_file("Select Blank A-Load")
            if path:
                st.session_state[f"target_{job_id}"] = path
                st.rerun()

    sync_job_from_widgets(job)

    if meta and meta.get("sheets"):
        st.caption("Target sheets: " + ", ".join(meta["sheets"]))

    if st.button(
        f"Generate a-load {index + 1}",
        key=f"generate_{job_id}",
        type="primary",
        use_container_width=True,
    ):
        sync_job_from_widgets(job)
        with st.spinner(f"Running {job['script']}..."):
            ok, message = run_one_job(job)
        if ok:
            st.success(message.split("\n", 1)[0])
            if "\n" in message:
                st.code(message.split("\n", 1)[1], language="text")
        else:
            st.error(message)

    st.divider()

if st.button("Add a-load section", use_container_width=True):
    st.session_state.jobs.append(
        new_job(st.session_state.next_job_id, script_options[0])
    )
    st.session_state.next_job_id += 1
    st.rerun()

st.markdown("### Generate all")
st.caption("Runs every section that has a script, Client File Spec, and Blank A-Load.")

if st.button("Generate all a-loads", type="primary", use_container_width=True):
    for job in st.session_state.jobs:
        sync_job_from_widgets(job)

    runnable = [
        job
        for job in st.session_state.jobs
        if (job.get("script") or "").strip()
        and (job.get("source") or "").strip()
        and (job.get("target") or "").strip()
    ]
    skipped = len(st.session_state.jobs) - len(runnable)

    if not runnable:
        st.error("No complete a-load sections to run. Fill in script and both file paths.")
    else:
        successes = 0
        failures = 0
        with st.spinner(f"Generating {len(runnable)} a-load(s)..."):
            for index, job in enumerate(runnable, start=1):
                ok, message = run_one_job(job)
                label = f"{index}. {job['script']}"
                if ok:
                    successes += 1
                    st.success(f"{label}: {message.split(chr(10), 1)[0]}")
                    if "\n" in message:
                        st.code(message.split("\n", 1)[1], language="text")
                else:
                    failures += 1
                    st.error(f"{label}: {message}")

        summary = f"Done. {successes} succeeded, {failures} failed."
        if skipped:
            summary += f" Skipped {skipped} incomplete section(s)."
        if failures:
            st.warning(summary)
        else:
            st.success(summary)
