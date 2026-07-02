import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\HCM11 Citizenship_4.28.26SB.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\catch-up\Person Personal Information_NKU_catch.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Citizenship Reference": [
        ("Citizenship_Status_Code", "ID"),
        ("Worker_ID","Change Personal Information Key"),
        ("Citizenship_Status_Code","Citizenship Reference Key"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Citizenship Reference": 7,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Citizenship Reference": [
        ("ID type","Citizenship_Status_Code", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)