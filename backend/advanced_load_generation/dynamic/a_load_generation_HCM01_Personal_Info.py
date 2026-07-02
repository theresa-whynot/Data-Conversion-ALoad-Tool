import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\catch-up\HCM01_DC_New_Hire_Catch_Up_5.15.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\catch-up\Person Personal Information_NKU_catch.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Change Personal Information": [
        ("Worker_ID", "Change Personal Information Key"),
        ("Worker_ID", "Person Reference ID"),
        ("Worker_ID", "Worker Reference ID"),
        ("Country_Reference_ID", "Country Reference ID"),
        ("Date_of_Birth", "Date of Birth"),
        ("Gender_Reference_ID", "Gender Reference ID"),
        ("Marital_Status_Reference_ID", "Marital Status Reference ID"),
        ("Marital_Status_Date", "Marital Status Date"),
        ("Hispanic_or_Latino", "Hispanic or Latino"),
        ("Date_of_Death","Date of Death"),
    ],
    "Ethnicity Reference":[
        ("Worker_ID", "Change Personal Information Key"),
        ("Ethnicity_Reference_ID", "Ethnicity Reference Key"),
        ("Ethnicity_Reference_ID", "ID"),
    ],
    "Gender Identity Reference":[
        ("Worker_ID", "Change Personal Information Key"),
        ("Gender_Identity_Reference_ID", "Gender Identity Reference Key"),
        ("Gender_Identity_Reference_ID", "ID"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
    "Gender Identity Reference": [("Gender_Identity_Reference_ID", "Exclude Blanks")],
}

# Define the header row for each sheet
header_rows = {
    "Change Personal Information": 7,
    "Ethnicity Reference": 7,
    "Gender Identity Reference": 7,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Change Personal Information": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None), 
        ("Worker Reference ID type", "Employee_ID", None),
        ("Person Reference ID type", "Employee_ID", None),
        ("Country Reference ID type", "ISO_3166-1_Alpha-3_Code", None),
        ("Gender Reference ID type", "Gender_Code", None),
        ("Marital Status Reference ID type", "Marital_Status_ID", "Marital Status Reference ID"),
        ("Country Reference ID type", "ISO_3166-1_Alpha-3_Code", None),
        ("Country Reference ID type", "ISO_3166-1_Alpha-3_Code", None),
    ],
    "Ethnicity Reference":[
        ("ID type", "Ethnicity_ID", "ID"), 
    ],
    "Gender Identity Reference":[
        ("ID type", "Gender_Identity_ID", "ID"), 
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)