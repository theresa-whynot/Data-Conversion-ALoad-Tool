import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\catch-up\HCM01_DC_New_Hire_Catch_Up_5.15.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\catch-up\Pre-Hires_NKU_Catch.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Applicant": [
        ("Worker_ID", "Applicant Key"),
        ("Worker_ID", "Applicant ID"),
        ("Country_Reference_ID", "Legal Name Data - Name Detail Data - Country Reference ID"),
        ("Legal_Prefix_Reference_ID", "Legal Name Data - Name Detail Data - Prefix Data - Title Reference ID"),
        ("Legal_First_Name", "Legal Name Data - Name Detail Data - First Name"),
        ("Legal_Middle_Name", "Legal Name Data - Name Detail Data - Middle Name"),
        ("Legal_Last_Name", "Legal Name Data - Name Detail Data - Last Name"),
        ("Legal_Suffix_Reference_ID", "Legal Name Data - Name Detail Data - Suffix Data - Social Suffix Reference ID"),
        ("Country_Reference_ID", "Preferred Name Data - Name Detail Data - Country Reference ID"),
        ("Preferred_Prefix_Reference_ID", "Preferred Name Data - Name Detail Data - Prefix Data - Title Reference ID"),
        ("Preferred_First_Name", "Preferred Name Data - Name Detail Data - First Name"),
        ("Preferred_Middle_Name", "Preferred Name Data - Name Detail Data - Middle Name"),
        ("Preferred_Last_Name", "Preferred Name Data - Name Detail Data - Last Name"),
        ("Preferred_Suffix_Reference_ID", "Preferred Name Data - Name Detail Data - Suffix Data - Social Suffix Reference ID"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Applicant": 11,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Applicant": [
        ("Add Only", "1", None), 
        ("Legal Name Data - Name Detail Data - Prefix Data - Title Reference ID type", "Predefined_Name_Component_ID", "Legal Name Data - Name Detail Data - Prefix Data - Title Reference ID"),
        ("Preferred Name Data - Name Detail Data - Prefix Data - Title Reference ID type", "Predefined_Name_Component_ID", "Preferred Name Data - Name Detail Data - Prefix Data - Title Reference ID"),
        ("Legal Name Data - Name Detail Data - Suffix Data - Social Suffix Reference ID type", "Predefined_Name_Component_ID", "Legal Name Data - Name Detail Data - Suffix Data - Social Suffix Reference ID"),
        ("Preferred Name Data - Name Detail Data - Suffix Data - Social Suffix Reference ID type", "Predefined_Name_Component_ID", "Preferred Name Data - Name Detail Data - Suffix Data - Social Suffix Reference ID"),
        ("Legal Name Data - Name Detail Data - Country Reference ID type", "ISO_3166-1_Alpha-3_Code", None),
        ("Preferred Name Data - Name Detail Data - Country Reference ID type", "ISO_3166-1_Alpha-3_Code", "Preferred Name Data - Name Detail Data - First Name")
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)