import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\HCM13 Military_4.28.26SB.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Person Personal Information_Military_NKU GOLD.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Change Personal Information": [
        ("Worker_ID", "Change Personal Information Key"),
        ("Worker_ID", "Person Reference ID"),
        ("Worker_ID", "Worker Reference ID"),
    ],
    "Grid-7": [
        ("Worker_ID","Change Personal Information Key"),
        ("Military_Status", "Military Service Information Data Key"),
        ("Military_Status","Military Status Reference ID"),
        ("Discharge_Date","Military Discharge Date"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Change Personal Information": 7,
    "Grid-7": 10,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Change Personal Information": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None), 
        ("Worker Reference ID type", "Employee_ID", None),
        ("Person Reference ID type", "Employee_ID", None),
    ],
    "Grid-7": [
        ("Military Status Reference ID type","Military_Status_ID", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)