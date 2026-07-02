import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\HCM10 Custom ID_4.28.26SB.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Person Other IDs__NKU_GOLD.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Change Other IDs": [
        ("Worker_ID", "Change Other IDs Key"),
        ("Worker_ID", "Person Reference ID"),
    ],
    "Custom ID": [
        ("Worker_ID", "Change Other IDs Key"),
        ("Custom_ID","Custom ID Key"),
        ("Custom_ID","ID"),
        ("Custom_ID_Type_Reference_ID","ID Type Reference ID"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Change Other IDs": 7,
    "Custom ID": 9,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Change Other IDs": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None),
        ("Person Reference ID type","Employee_ID", None),
    ],
    "Custom ID": [
        ("ID Type Reference ID type","Custom_ID_Type_ID", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)