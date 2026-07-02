import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\PAY03.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Worker FICA Medicare Withholdings_1__NKU_GOLD.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Payroll Payee FICA": [
        ("Worker_ID", "Payroll Payee FICA Key"),
        ("Worker_ID", "Worker Reference ID"),
        ("Effective_Date", "Effective As Of"),
        ("Apply_to_Worker", "Apply To Worker"),
    ],
    "Medicare Exempt Data": [
        ("Worker_ID", "Payroll Payee FICA Key"),
        ("Medicare_Exemption_Reason", "Medicare Exempt Data Key"),
    ],
    "Grid-1": [
        ("Worker_ID", "Payroll Payee FICA Key"),
        ("Medicare_Exemption_Reason", "Medicare Exempt Data Key"),
        ("Medicare_Exemption_Reason", "Medicare Reason for Exemption Reference Key"),
        ("Medicare_Exemption_Reason", "ID"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Payroll Payee FICA": 6,
    "Medicare Exempt Data": 6,
    "Grid-1": 7,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Payroll Payee FICA": [
        ("Add Only", "1", None), 
        ("Worker Reference ID type", "Employee_ID", None),
    ],
    "Medicare Exempt Data": [
        ("Exempt from Medicare", "1", None), 
    ],
    "Grid-1": [
        ("ID type", "Exempt_Reason_ID", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)