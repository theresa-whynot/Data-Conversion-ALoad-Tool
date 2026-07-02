import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\HCM28 EE Previous System Comp History_3.9.26_SB.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\Previous System Job and Position History_NKU_Parallel.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Grid-1": [
        ("Worker_ID", "Previous System Compensation History Key"),
        ("Worker_ID", "Worker Reference ID"),
    ],
    "Previous System Job History": [
        ("Worker_ID", "Previous System Compensation History Key"),
        ("Worker_ID", "Previous System Job History Key"),
        ("Worker_History_Name", "Worker History Name"),
        ("Action_Date", "Action Date"),
        ("Reason", "Reason"),
        ("Amount", "Amount"),
        ("Currency_Reference_ID", "Currency"),
        ("Frequency_Reference_ID", "Frequency"),
        ("Amount_Change", "Amount Change"),
        ("Description", "Description"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Grid-1": 6,
    "Previous System Job History": 8,

}

# Define default columns for each sheet (optional)
default_columns = {
    "Grid-1": [
        ("Worker Reference ID type","Employee_ID", None),
    ],
    "Previous System Job History": [
        ("Add Only", "1", None), 
        ("Currency Reference ID type", "Currency_ID", None), 
        ("Frequency Reference ID type", "Frequency_ID", None), 
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)