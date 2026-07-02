import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets



# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\CATS\HCMConfig10.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\CATS\Role Assignments_Managers_FOUNDATOIN_CATS.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Role Assigner": [
        ("Sup_Org_ID", "Role Assigner Key"),
        ("Sup_Org_ID", "Role Assigner Reference ID"),
    ],
    "Role Assignment Data": [
        ("Sup_Org_ID", "Role Assigner Key"),
        ("Sup_Org_ID", "Role Assignment Data Key"),
    ],
    "Role Assignee Reference": [
        ("Sup_Org_ID", "Role Assigner Key"),
        ("Sup_Org_ID", "Role Assignment Data Key"),
        ("Primary_Manager_Position_ID", "Role Assignee Reference Key"),
        ("Primary_Manager_Position_ID", "ID"),
    ],

}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Role Assigner": 6,
    "Role Assignment Data": 7,
    "Role Assignee Reference": 7,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Role Assigner": [
        ("Role Assigner Reference ID type", "Organization_Reference_ID", None), 
        ("Effective Date", "1900-01-01", None),
    ],
    "Role Assignment Data": [
        ("Organization Role Reference ID type", "Organization_Role_ID", None), 
        ("Organization Role Reference ID", "Manager", None),
    ],
    "Role Assignee Reference": [
        ("ID type", "Position_ID", None), 
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)