import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\PAY08.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Worker_Work_Home_County_Withholdings__NKU_GOLD.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Grid-1": [
        (("Worker_ID", "Worker_County_Reference_ID", "Effective_Date"), "Payroll USA Worker State and Local Tax Election Key", "concat"),
        ("Worker_ID", "Worker Reference ID"),
        ("Effective_Date", "Effective Date"),
        ("Company_Reference_ID", "Company Reference ID"),
    ],
    "Grid-2": [
        (("Worker_ID", "Worker_County_Reference_ID", "Effective_Date"), "Payroll USA Worker State and Local Tax Election Key", "concat"),
        ("Worker_County_Reference_ID", "Payroll State Authority Reference Descriptor"),
    ],
    "Payroll State County Tax Data": [
        (("Worker_ID", "Worker_County_Reference_ID", "Effective_Date"), "Payroll USA Worker State and Local Tax Election Key", "concat"),
        ("Worker_County_Reference_ID", "Payroll State County Tax Data Key"),
        ("Tax_Address_Type_Reference_ID", "Tax Address Type Reference ID"),
        ("Worker_County_Reference_ID", "Payroll Local County Authority Reference ID"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Grid-1": 7,
    "Grid-2": 8,
    "Payroll State County Tax Data": 9,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Grid-1": [
        ("Add Only", "1", None), 
        ("Worker Reference ID type", "Employee_ID", None),
        ("Company Reference ID type", "Company_Reference_ID", None),
    ],
    "Grid-2": [
        ("Payroll USA State and Local Tax Election Data Key", "1", None), 
        ("Payroll State Authority Reference ID type", "Payroll_State_Authority_Tax_Code", None),
    ],
    "Payroll State County Tax Data": [
        ("Payroll USA State and Local Tax Election Data Key", "1", None),
        ("Tax Address Type Reference ID type", "Tax_Address_Type_ID", None), 
        ("Payroll Local County Authority Reference ID type", "Payroll_Local_County_Authority_Tax_Code", None), 
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)