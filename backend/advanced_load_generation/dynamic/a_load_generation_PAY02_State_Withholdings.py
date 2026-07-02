import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets



# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\Monroe County\Parallel3 Build\00 - Completed Data from MC\PAY\PAY02_STATE_20260112_Load_Source.xlsx"
target_file = r"C:\Users\TheresaReinhard\Downloads\Worker Work State Withholdings_NKU_FOUNDATION.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Grid-1": [
        ("Worker_ID", "Payroll USA Worker State and Local Tax Election Key"),
        ("Worker_ID", "Worker Reference ID"),
        ("Effective_Date", "Effective Date"),
        ("Company_Reference_ID", "Company Reference ID"),
    ],
    "Grid-2": [
        ("Worker_ID", "Payroll USA Worker State and Local Tax Election Key"),
        ("Payroll_State_Authority_Tax_Code", "Payroll USA State and Local Tax Election Data Key"),
        ("Payroll_State_Authority_Tax_Code", "Payroll State Authority Reference ID"),
    ],
    "State Income Tax Data": [
        ("Worker_ID", "Payroll USA Worker State and Local Tax Election Key"),
        ("Payroll_State_Authority_Tax_Code", "Payroll USA State and Local Tax Election Data Key"),
        ("Marital_Filing_Status", "Payroll Withholding Status Reference ID"),
        ("Number_of_Allowances", "Number of Allowances"),
        ("Additional_Withholding", "Additional Amount"),
        ("Reduced_Withholding", "Reduced Withholding Amount"),
        ("Exempt", "Exempt"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Grid-1": 7,
    "Grid-2": 8,
    "State Income Tax Data": 9,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Grid-1": [
        ("Add Only", "1", None), 
        ("Worker Reference ID type", "Employee_ID", None),
        ("Company Reference ID type", "Company_Reference_ID", None),
    ],
    "Grid-2": [
        ("Payroll State Authority Reference ID type", "Payroll_State_Authority_Tax_Code", None),
    ],
    "State Income Tax Data": [
        ("State Income Tax Data Key", "1", None),
        ("Payroll Withholding Status Reference ID type", "Payroll_Marital_Status_ID", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)