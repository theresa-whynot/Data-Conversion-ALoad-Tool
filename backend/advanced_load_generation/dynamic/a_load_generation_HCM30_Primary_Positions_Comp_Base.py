import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\CATS\HCM30_EE_Primary_Position_Comp_Base V2 2026-05-18.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\CATS\Request Compensation Change_FOUNDATION_CATS.xlsx"


# Define the mapping for each sheet
sheet_column_map = {
    "Request Compensation Change": [
        ("Worker_ID", "Request Compensation Change Key"),
        ("Worker_ID", "Employee Reference ID"),
        ("Position_ID", "Position Reference ID"),
        ("Compensation_Effective_Date", "Compensation Change Date"),
        ("Compensation_Package_Reference_ID", "Compensation Package Reference ID"),
        ("Grade_Reference_ID", "Compensation Grade Reference ID"),
        ("Grade_Profile_Reference_ID", "Compensation Grade Profile Reference ID"),
        ("Grade_Step_Reference_ID", "Compensation Step Reference ID"),
        ("Progression_Start_Date", "Progression Start Date"),
    ],
    "Pay Plan Sub Data": [
        ("Worker_ID", "Request Compensation Change Key"),
        ("Compensation_Plan_ID", "Pay Plan Sub Data Key"),
        ("Compensation_Plan_ID", "Pay Plan Reference ID"),
        ("Rate", "Amount"),
        ("Currency_Reference_ID", "Currency Reference ID"),
        ("Frequency_Reference_ID", "Frequency Reference ID"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Request Compensation Change": 9,
    "Pay Plan Sub Data": 9,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Request Compensation Change": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None),
        ("Employee Reference ID type", "Employee_ID", None),
        ("Position Reference ID type","Position_ID", None),
        ("Reason Reference ID type","General_Event_Subcategory_ID", None),
        ("Reason Reference ID","Request_Compensation_Change_Conversion_Conversion", None),
        ("Compensation Package Reference ID type","Compensation_Package_ID", None),
        ("Compensation Grade Reference ID type","Compensation_Grade_ID", None),
        ("Compensation Grade Profile Reference ID type","Compensation_Grade_Profile_ID", "Compensation Grade Profile Reference ID"),
        ("Compensation Step Reference ID type","Compensation_Step_ID", "Compensation Step Reference ID"),
    ],
    "Pay Plan Sub Data": [
        ("Pay Plan Reference ID type","Compensation_Plan_ID", None),
        ("Currency Reference ID type","Currency_ID", None),
        ("Frequency Reference ID type","Frequency_ID", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)