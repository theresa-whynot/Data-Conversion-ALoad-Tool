import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\Updated 7.9_Avaap_Manipulation\HCM29 EE Termination_2025_07_09_BLB.xlsx"
target_file = r"C:\Users\TheresaReinhard\Downloads\Terminate Employees_1_NKU_Foundation.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Terminate Employee": [
        ("Worker_ID", "Spreadsheet Key*"),
        ("Worker_ID", "Employee*"),
        ("Termination_Date", "Termination Date*"),
        ("Last_Day_of_Work", "Last Day of Work"),
        ("Termination_Reason_Reference_ID", "Primary Reason*"),
        ("Pay_Through_Date", "Pay Through Date"),
        ("Regrettable", "Regrettable"),
        ("Eligible_For_Rehire", "Eligible for Hire"),
        ("Close_Position", "Close Position"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Terminate Employee": 5,
}

# Define default columns for each sheet (optional)
default_columns = {
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)