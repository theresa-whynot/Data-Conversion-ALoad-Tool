import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets



# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\catch-up\HCM02_DC_New_Hire_Catch_Up_5.15.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\catch-up\Pre-Hires_NKU_Catch.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Applicant - Email Address Data": [
        ("Worker_ID", "Applicant Key"),
        ("Email_Address", "Email Address Data Key"),
        ("Email_Address", "Email Address"),
        ("Visibility", "Public"),
        ("Primary", "Primary"),
        ("Communication_Usage_Type_Reference_ID", "Type Reference ID"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Applicant - Email Address Data": 11,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Applicant - Email Address Data": [
        ("Type Reference ID type", "Communication_Usage_Type_ID", None), 
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)