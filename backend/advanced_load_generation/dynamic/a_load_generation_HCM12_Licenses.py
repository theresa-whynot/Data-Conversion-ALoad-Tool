import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\catch-up\HCM12_DC_New_Hire_Catch_Up_5.15.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\catch-up\Person Licenses.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Change Licenses": [
        ("Worker_ID", "Change Licenses Key"),
        ("Worker_ID", "Person Reference ID"),
    ],
    "License ID": [
        ("Worker_ID", "Change Licenses Key"),
        ("License_ID","License ID Key"),
        ("License_ID","ID"),
        ("License_Type_Reference_ID","ID Type Reference ID"),
        ("Issued_By_Country_Reference_ID","Country Reference ID"),
        ("Issued_By_Country_Region_Reference_ID","Country Region Reference ID"),
        ("Issued_By_Authority_Reference_ID","Authority Reference ID"),
        ("Issued_Date","Issued Date"),
        ("Expiration_Date","Expiration Date"),
        ("Verification_Date","Verification Date"),
        ("Verified_By_Employee_ID","Verified By Reference ID"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Change Licenses": 7,
    "License ID": 9,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Change Licenses": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None),
        ("Person Reference ID type","Employee_ID", None),
    ],
    "License ID": [
        ("ID Type Reference ID type","License_ID_Type_ID", None),
        ("Country Reference ID type","ISO_3166-1_Alpha-3_Code", "Country Reference ID"),
        ("Country Region Reference ID type","Country_Region_ID", "Country Region Reference ID"),
        ("Authority Reference ID type","Authority_ID", "Authority Reference ID"),
        ("Verified By Reference ID type","Employee_ID", "Verified By Reference ID"),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)