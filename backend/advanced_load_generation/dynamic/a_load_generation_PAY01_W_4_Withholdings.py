import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets



# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\CATS\PAY01_EE_W-4_Withholdings_V2 2026-05-21.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\CATS\Worker W-4 Withholdings_FOUNDATION_CATS.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Grid-1": [
        ("Worker_ID", "Payroll Federal W-4 Tax Election Key"),
        ("Worker_ID", "Worker Reference ID"),
        ("W4_Effective_Date", "Effective as of"),
        ("Company_Reference_ID", "Company Reference ID"),
        ("Payroll_Marital_Status_Reference_ID", "Marital Status Reference ID"),
        ("Number_of_Allowances", "Number of Allowances"),
        ("Additional_Amount", "Additional Amount"),
        ("Multiple_Jobs_or_Spouse_Works", "Multiple Jobs or Spouse Works"),
        ("Total_Dependent_Amount", "Total Dependent Amount"),
        ("Other_Income", "Other Income"),
        ("Deductions", "Deductions"),
        ("Exempt", "Exempt"),
        ("Nonresident_Alien", "Nonresident Alien"),
        ("Exempt_from_NRA_Additional_Amount", "Exempt from NRA Additional Amount"),
        ("Lock_In_Letter", "Lock In Letter"),
        ("No_Wage_No_Tax", "No Wage No Tax"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Grid-1": 6,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Grid-1": [
        ("Add Only", "1", None), 
        ("Worker Reference ID type", "Employee_ID", None),
        ("Company Reference ID type", "Company_Reference_ID", None),
        ("Marital Status Reference ID type", "Payroll_Marital_Status_ID", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)
