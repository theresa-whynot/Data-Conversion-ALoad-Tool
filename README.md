# Data Conversion A-Load Tool

Generate Workday a-load Excel files from source conversion workbooks using the
dynamic mapping scripts in `backend/advanced_load_generation/dynamic/`.

## Setup

```bash
pip install -r requirements.txt
```

## Desktop app (recommended)

### Run from source (no browser / localhost typing)

```bash
pip install -r requirements.txt
python desktop_launcher.py
```

This starts Streamlit in the background and opens the UI in a native desktop window.

### Build a downloadable Windows `.exe`

On a Windows machine with Python installed:

```bat
build_desktop_app.bat
```

Or manually:

```bash
pip install -r requirements.txt -r requirements-desktop.txt
pyinstaller --noconfirm desktop_app.spec
```

When the build finishes, share this folder:

```text
dist/ALoadGenerator/
```

Users double-click:

```text
dist/ALoadGenerator/ALoadGenerator.exe
```

Tip: zip the whole `ALoadGenerator` folder (not just the `.exe`). The onedir build
needs the files beside the executable.

If a coworker PC does not have Microsoft Edge WebView2, the app falls back to the
system browser automatically. To install WebView2 (optional, for the native window):

https://developer.microsoft.com/microsoft-edge/webview2/

## Browser mode (optional)

```bash
streamlit run frontend/main_app.py
```

Then open `http://localhost:8501` if it does not open automatically.

## Using the app

1. Select an a-load script (for example `SUP02_Supplier_Emails`)
2. Choose the **Client File Spec** (Browse or path)
3. Choose the **Blank A-Load** (Browse or path)
4. Click **Generate a-load** for that section, or add more sections and use **Generate all a-loads**

The UI reuses each script's existing sheet mappings, filters, header rows, and
defaults. Only the file paths are overridden.

## CLI runner

```bash
cd backend/advanced_load_generation
python -c "from aload_runner import list_aload_scripts, run_aload; print(list_aload_scripts()[:5])"
```

## Existing scripts

You can still run any dynamic script directly:

```bash
python backend/advanced_load_generation/dynamic/a_load_generation_SUP02_Supplier_Emails.py
```

## Design notes

- **File paths first:** source/target inputs match how the mappings already work.
- **No database required** for generation. A DB (or simple log) can be added later
  for run history, saved path presets, or SharePoint integration.
- **Desktop packaging** wraps Streamlit in a native window with `pywebview` and
  can be frozen with PyInstaller for distribution.
