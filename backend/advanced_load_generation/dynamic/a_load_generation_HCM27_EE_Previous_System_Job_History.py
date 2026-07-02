import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\HCM27 EE Previous System Job History_2.24.26_NM.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\Previous System Compensation History_NKU_Parallel.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Previous System Job History": [
        ("Worker_ID", "Previous System Job History Key"),
    ],
    "Grid-1": [
        ("Worker_ID", "Previous System Job History Key"),
        ("Worker_ID", "Previous System Job History - Previous System Job History Key"),
        ("Worker_History_Name", "Worker History Name"),
        ("Action_Date", "Action Date"),
        ("Reason", "Reason"),
        ("Description", "Description"),
        ("Start_Date", "Start Date"),
    ],
}


# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Previous System Job History": 6,
    "Grid-1": 7,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Previous System Job History": [
        ("Worker Reference ID type", "Employee_ID", None),
    ],
    "Grid-1": [
        ("Add Only", "1", None), 
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)

