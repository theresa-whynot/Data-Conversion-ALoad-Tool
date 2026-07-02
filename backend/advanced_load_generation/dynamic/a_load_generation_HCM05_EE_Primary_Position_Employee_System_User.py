import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\Monroe County\A&C\HCM05 EE Primary Position_avaap_manipulation.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\Monroe County\A&C\Employee System Users_1_MC_E2E_Build.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Employee System User": [
        ("Worker_ID", "Employee System User Key"),
        ("Worker_ID", "Employee Reference ID"),
        ("User_Name", "User Name"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Employee System User": 7,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Employee System User": [
        ("Employee Reference ID type", "Employee_ID", None),
        ("Generate Random Password", "1", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)