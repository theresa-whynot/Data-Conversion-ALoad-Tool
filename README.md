# Data Conversion A-Load Tool

Generate Workday a-load Excel files from source conversion workbooks using the
dynamic mapping scripts in `backend/advanced_load_generation/dynamic/`.

## Setup

```bash
pip install -r requirements.txt
```

## Frontend (recommended)

Start the Streamlit UI:

```bash
streamlit run frontend/main_app.py
```

Then:

1. Select an a-load script (for example `SUP02_Supplier_Emails`)
2. Enter the **source** Excel path
3. Enter the **target** a-load Excel path
4. Click **Generate a-load**

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
