import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\CATS\HCM50_Open_Positions 2026-05-21.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\CATS\Change Organization Assignments_Position_Management_Open_Update.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Change Organization Assignments": [
        ("Position_Reference_ID", "Change Organization Assignments Key"),
        ("Position_Reference_ID", "Position Reference ID"),
        ("Availability_Date", "Effective Date"),
    ],
    "Company Assignments Reference": [
        ("Position_Reference_ID", "Change Organization Assignments Key"),
        ("Company_Reference_ID","Company Assignments Reference Key"),
        ("Company_Reference_ID","ID"),
    ],
    "Grid-2": [
        ("Position_Reference_ID", "Change Organization Assignments Key"),
        ("Cost_Center_Reference_ID","Cost Center Assignments Reference Key"),
        ("Cost_Center_Reference_ID","ID"),
    ],
    "Region Assignments Reference": [
        ("Position_Reference_ID", "Change Organization Assignments Key"),
        ("Region_Reference_ID","Region Assignments Reference Key"),
        ("Region_Reference_ID","ID"),
    ],
    "Grid-3": [
        ("Position_Reference_ID", "Change Organization Assignments Key"),
        (("Custom_Org_1_Reference_ID", "Custom_Org_2_Reference_ID"), "Custom Organization Assignment Data Key", "stack"),
        (("Custom_Org_1_Reference_ID", "Custom_Org_2_Reference_ID"), "Custom Organization Assignment Reference ID", "stack"),
    ],
    "Fund Assignments Reference": [
        ("Position_Reference_ID", "Change Organization Assignments Key"),
        ("Fund_Reference_ID","Fund Assignments Reference Key"),
        ("Fund_Reference_ID","ID"),
    ],
    "Program Assignments Reference": [
        ("Position_Reference_ID", "Change Organization Assignments Key"),
        ("Program_Reference_ID","Program Assignments Reference Key"),
        ("Program_Reference_ID","ID"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
    "Company Assignments Reference": [("Company_Reference_ID", "Exclude Blanks")],
    "Grid-2": [("Cost_Center_Reference_ID", "Exclude Blanks")],
    "Region Assignments Reference": [("Region_Reference_ID", "Exclude Blanks")],
    "Grid-3": [("Custom_Org_1_Reference_ID", "Exclude Blanks")],
    "Fund Assignments Reference": [("Fund_Reference_ID", "Exclude Blanks")],
    "Program Assignments Reference": [("Program_Reference_ID", "Exclude Blanks")],
}

# Define the header row for each sheet
header_rows = {
    "Change Organization Assignments": 9,
    "Company Assignments Reference": 7,
    "Grid-2": 7,
    "Region Assignments Reference": 7,
    "Grid-3": 8,
    "Fund Assignments Reference": 7,
    "Program Assignments Reference": 7,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Change Organization Assignments": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None),
        ("Position Reference ID type","Position_ID", None),
    ],
    "Company Assignments Reference": [
        ("ID type","Company_Reference_ID", "ID"),
    ],
    "Grid-2": [
        ("ID type","Cost_Center_Reference_ID", "ID"),
    ],
    "Region Assignments Reference": [
        ("ID type","Region_Reference_ID", "ID"),
    ],
    "Grid-3": [
        ("Custom Organization Assignment Reference ID type","Custom_Organization_Reference_ID", "Custom Organization Assignment Reference ID"),
    ],
    "Fund Assignments Reference": [
        ("ID type","Fund_ID", "ID"),
    ],
    "Program Assignments Reference": [
        ("ID type","Program_ID", "ID"),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)