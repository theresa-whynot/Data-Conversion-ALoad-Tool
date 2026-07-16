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
