import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\catch-up\HCM04_DC_New_Hire_Catch_Up_5.15.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\catch-up\Pre-Hires_NKU_Catch.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Applicant - Address Data": [
        ("Worker_ID", "Applicant Key"),
        ("Address_Line_1", "Address Data Key"),
        ("Country_Reference_ID", "Country Reference ID"),
        ("Municipality", "Municipality"),
        ("Country_Region_Reference_ID", "Country Region Reference ID"),
        ("Postal_Code", "Postal Code"),
        ("Visibility", "Public"),
        ("Primary", "Primary"),
        ("Type_Reference_ID", "Type Reference ID"),
    ],
    "Grid-8": [
        ("Worker_ID", "Applicant Key"),
        ("Address_Line_1", "Address Data Key"),
        (("Address_Line_1", "Address_Line_2"), "Address Line Data Key", "stack"),
        (("Address_Line_1", "Address_Line_2"), "Address Line Data", "stack"),
    ],
    "Grid-11": [
        ("Worker_ID", "Applicant Key"),
        ("Address_Line_1", "Address Data Key"),
        ("Communication_Usage_Reference_ID","Use For Reference Key"),
        ("Communication_Usage_Reference_ID","ID"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
    "Grid-11": ("Communication_Usage_Reference_ID", "Exclude Blanks"),  
}

# Define the header row for each sheet
header_rows = {
    "Applicant - Address Data": 11,
    "Grid-8": 9,
    "Grid-11": 10,

}

# Define default columns for each sheet (optional)
default_columns = {
    "Applicant - Address Data": [
        ("Country Reference ID type", "ISO_3166-1_Alpha-3_Code", None), 
        ("Country Region Reference ID type", "Country_Region_ID", None), 
        ("Type Reference ID type", "Type_Reference_ID", None), 
        ("Type Reference ID type", "Communication_Usage_Type_ID", None), 
        ("Effective Date", "1900-01-01", None), 
    ],
    "Grid-8": [
        ("Address Line Data Type", "Address_Line_1", None), 
    ],
    "Grid-11": [
        ("ID type", "Communication_Usage_Behavior_ID", None), 
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)