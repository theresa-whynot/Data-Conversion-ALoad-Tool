import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets

# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\HCM40 EE Additional Positions_4.27.26SB.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Pay Group Assignments_Additional_Jobs__NKU_GOLD.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Assign Pay Group Event": [
        ("Position_Reference_ID", "Assign Pay Group Event Key"),
        ("Worker_ID", "Worker Reference ID"),
        ("Pay_Group_Reference_ID", "Pay Group Reference ID"),
        ("Position_Reference_ID", "Position Reference ID"),
        ("Additional_Jobs_Start_Date", "Effective Date"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Assign Pay Group Event": 7,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Assign Pay Group Event": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None),
        ("Worker Reference ID type", "Employee_ID", None),
        ("Pay Group Reference ID type","Organization_Reference_ID", None),
        ("Position Reference ID type","Position_ID", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)