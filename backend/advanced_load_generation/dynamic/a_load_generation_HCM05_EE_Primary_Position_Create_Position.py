import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\CATS\HCM05_EE_Primary_Position_V2 2026-05-18.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\CATS\Create Positions_FOUNDATOIN_CATS.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Create Position": [
        ("Position_Reference_ID", "Create Position Key"),
        ("Supervisory_Organization_Reference_ID", "Supervisory Organization Reference ID"),
        ("Position_Reference_ID", "Position ID"),
        ("Position_Time_Type_Reference_ID", "Time Type Reference ID"),
        ("Position_Title", "Job Posting Title"),
    ],
    "Job Profile Reference": [
        ("Position_Reference_ID", "Create Position Key"),
        ("Job_Profile_Reference_ID","Job Profile Reference Key"),
        ("Job_Profile_Reference_ID","ID"),
    ],
    "Location Reference": [
        ("Position_Reference_ID", "Create Position Key"),
        ("Location_Reference_ID","Location Reference Key"),
        ("Location_Reference_ID","ID"),
    ],
    "Position Worker Type Reference": [
        ("Position_Reference_ID", "Create Position Key"),
        ("Employee_Type_Reference_ID","Position Worker Type Reference Key"),
        ("Employee_Type_Reference_ID","ID"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
    "Create Position": [("Staffing_Model", "Position Management")],
    "Job Profile Reference": [("Staffing_Model", "Position Management")],
    "Location Reference": [("Staffing_Model", "Position Management")],
    "Position Worker Type Reference": [("Staffing_Model", "Position Management")],
}

# Define the header row for each sheet
header_rows = {
    "Create Position": 9,
    "Job Profile Reference": 7,
    "Location Reference": 7,
    "Position Worker Type Reference": 7,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Create Position": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None),
        ("Supervisory Organization Reference ID type","Organization_Reference_ID", None),
        ("Worker Type Reference ID type","Worker_Type_ID", None),
        ("Worker Type Reference ID","EE", None),
        ("Time Type Reference ID type","Position_Time_Type_ID", None),
        ("Availability Date","1900-01-01",None),
        ("Earliest Hire Date","1900-01-01",None),
    ],
    "Job Profile Reference": [
        ("ID type","Job_Profile_ID", None),
    ],
    "Location Reference": [
        ("ID type","Location_ID", None),
    ],
    "Position Worker Type Reference": [
        ("ID type","Employee_Type_ID", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)