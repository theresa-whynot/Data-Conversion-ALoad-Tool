import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\CATS\HCM05_EE_Primary_Position_V2 2026-05-18.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\CATS\Edit Service Dates_FOUNDATOIN_CATS.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Edit Service Dates": [
        ("Worker_ID", "Edit Service Dates Key"),
        ("Worker_ID", "Worker Reference ID"),
        ("Hire_Date", "Effective Date"),
        ("Original_Hire_Date", "Original Hire Date"),
        ("Continuous_Service_Date", "Continuous Service Date"),
        ("Seniority_Date", "Seniority Date"),
        ("Benefits_Service_Date", "Benefits Service Date"),
        ("Company_Service_Date", "Company Service Date"),
        ("Severence_Service_Date", "Severance Date"),
        ("Vesting_Date", "Vesting Date"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Edit Service Dates": 7,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Edit Service Dates": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None),
        ("Worker Reference ID type", "Employee_ID", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)