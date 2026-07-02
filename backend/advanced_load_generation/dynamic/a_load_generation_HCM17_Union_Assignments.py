import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\Monroe County\Gold Build\ALOADS\HCM21RD.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\Monroe County\Gold Build\ALOADS\Union Memberships_MCGOLDRD.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Union Member": [
        ("Worker_ID", "Union Member Key"),
        ("Worker_ID", "Worker Reference ID"),
        ("Union_Reference_ID", "Union Reference ID"),
        ("Seniority_Date", "Seniority Date"),
    ],
    "Union Membership Data": [
        ("Worker_ID", "Union Member Key"),
        ("Worker_ID", "Union Membership Data Key"),
        ("Membership_Type_Reference_ID","Membership Type Reference ID"),
        ("Start_Date","Start Date"),
        ("End_Date","End Date"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Union Member": 7,
    "Union Membership Data": 7,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Union Member": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None),
        ("Worker Reference ID type","Employee_ID", None),
        ("Union Reference ID type","Union_ID", None),
    ],
    "Union Membership Data": [
        ("Membership Type Reference ID type","Membership_Type_ID", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)