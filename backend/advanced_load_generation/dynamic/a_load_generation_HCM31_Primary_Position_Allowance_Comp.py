import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets



# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\CATS\HCM31_EE_Primary_Position_Comp_Allowance_V2 2026-05-21.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\CATS\Request Compensation Change_Allowance_FOUNDATION_CATS.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Request Compensation Change": [
        (("Worker_ID", "Compensation_Plan_ID"), "Request Compensation Change Key", "concat"),
        ("Worker_ID", "Employee Reference ID"),
        ("Position_ID", "Position Reference ID"),
        ("Compensation_Effective_Date", "Compensation Change Date"),
    ],
    "Allowance Plan Sub Data": [
        (("Worker_ID", "Compensation_Plan_ID"), "Request Compensation Change Key", "concat"),
        ("Compensation_Plan_ID", "Allowance Plan Sub Data Key"),
        ("Compensation_Plan_ID", "Allowance Plan Reference ID"),
        ("Amount", "Amount"),
        ("Percent", "Percent"),
        ("Reimbursement_Start_Date", "Reimbursement Start Date"),
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
    "Allowance Plan Sub Data": 9,
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
    ],
    "Allowance Plan Sub Data": [
        ("Allowance Plan Reference ID type","Compensation_Plan_ID", None),
        ("Currency Reference ID type","Currency_ID", None),
        ("Frequency Reference ID type","Frequency_ID", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)