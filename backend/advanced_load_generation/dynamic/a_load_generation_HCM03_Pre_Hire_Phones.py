import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets



# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\catch-up\HCM03_DC_New_Hire_Catch_Up_5.15.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\catch-up\Pre-Hires_NKU_Catch.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Applicant - Phone Data": [
        ("Worker_ID", "Applicant Key"),
        ("Phone_Number", "Phone Data Key"),
        ("Country_Reference_ID", "Country ISO Code"),
        ("Phone_Number", "Phone Number"),
        ("Phone_Extension", "Phone Extension"),
        ("Phone_Device_Type_Reference_ID", "Phone Device Type Reference ID"),
        ("Visibility", "Public"),
        ("Primary", "Primary"),
        ("Type_Reference_ID", "Type Reference ID"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Applicant - Phone Data": 11,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Applicant - Phone Data": [
        ("Type Reference ID type", "Communication_Usage_Type_ID", None), 
        ("Phone Device Type Reference ID type", "Phone_Device_Type_ID", None), 
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)