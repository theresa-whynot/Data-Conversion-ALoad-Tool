import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\catch-up\HCM16_DC_New_Hire_Catch_Up_5.15.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\catch-up\Person Passports and Visas_NKU_New_Hire_Catch.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Change Passports and Visas": [
        ("Worker_ID", "Change Passports and Visas Key"),
        ("Worker_ID", "Worker Reference ID"),
        ("Worker_ID", "Person Reference ID"),
    ],
    "Passport ID": [
        ("Worker_ID", "Change Passports and Visas Key"),
        ("Passport_Type_Name","Passport ID Key"),
        ("Passport_ID","ID"),
        ("Passport_Type_Name","ID Type Reference ID"),
        ("Passport_Country","Country Reference ID"),
        ("Issued_Date","Issued Date"),
        ("Expiration_Date","Expiration Date"),
        ("Verification_Date","Verification Date"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
    "Grid-3": [("US_Protected_Veteran_Status_Type_ID_1", "Exclude Blanks")],
}

# Define the header row for each sheet
header_rows = {
    "Change Passports and Visas": 7,
    "Passport ID": 9,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Change Passports and Visas": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None),
        ("Worker Reference ID type","Employee_ID", None),
        ("Person Reference ID type","Employee_ID", None),
        ("Replace All","0", None),
    ],
    "Passport ID": [
        ("ID Type Reference ID type","Passport_ID_Type_ID", None),
        ("Country Reference ID type","ISO_3166-1_Alpha-3_Code", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)