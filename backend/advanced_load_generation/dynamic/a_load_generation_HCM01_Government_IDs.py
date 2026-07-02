import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\catch-up\HCM01_DC_New_Hire_Catch_Up_5.15.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\catch-up\Person Government IDs_NKU_catch.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Change Government IDs": [
        ("Worker_ID", "Change Government IDs Key"),
        ("Worker_ID", "Person Reference ID"),
        ("Worker_ID", "Worker Reference ID"),
    ],
    "National ID":[
        ("Worker_ID", "Change Government IDs Key"),
        ("National_ID", "National ID Key"),
        ("National_ID", "ID"),
        ("Country_Reference_ID", "Country Reference ID"),
        ("National_ID_Type_Reference_ID", "ID Type Reference ID"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
    "Change Government IDs": ("National_ID", "Exclude Blanks"),
    "National ID": ("Is_Dependent", "Exclude Blanks"),
}

# Define the header row for each sheet
header_rows = {
    "Change Government IDs": 7,
    "National ID": 9,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Change Government IDs": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None), 
        ("Worker Reference ID type", "Employee_ID", None),
        ("Person Reference ID type", "Employee_ID", None),
    ],
    "National ID":[
        ("ID Type Reference ID type", "National_ID_Type_Code", None),
        ("Country Reference ID type", "ISO_3166-1_Alpha-3_Code", None), 
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)