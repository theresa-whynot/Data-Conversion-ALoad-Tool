import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\City of Peoria\GOLD\Loads\A_load_generation\BEN01_Beneficiaries.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\City of Peoria\GOLD\Aloads\Change Beneficiaries_1_PEORIA_GOLD.xlsx"


# Define the mapping for each sheet
sheet_column_map = {
    "Change Beneficiary": [
        ("Employee_ID", "Employee Reference ID"),
        ("Beneficiary_ID", "Change Beneficiary Key"),
        ("Beneficiary_ID", "Beneficiary ID"),
    ],
    "Person Data": [
        ("Beneficiary_ID", "Change Beneficiary Key"),
        ("Dependent_ID", "Existing Related Person Reference ID"),
        ("Relationship_to_Employee", "Related Person Relationship Reference ID"),
        ("Irrevocable", "Irrevocable"),
        ("Use_Employee_Address", "Use Employee Address"),
        ("Use_Employee_Phone", "Use Employee Phone"),
    ],
    "Grid-2": [
        ("Beneficiary_ID", "Change Beneficiary Key"),
        ("Legal_First_Name", "First Name"),
        ("Legal_Middle_Name", "Middle Name"),
        ("Legal_Last_Name", "Last Name"),
        ("Legal_Name_Country", "Country Reference ID"),
        ("Title", "Title Reference ID"),
        ("Suffix", "Social Suffix Reference ID"),
        ("Date_of_Birth","Date of Birth"),
        ("Gender","Gender Reference ID"),
        ("Date_of_Death","Date of Death"),
    ],
    "Grid-3": [
        ("Beneficiary_ID", "Change Beneficiary Key"),
        ("Home_Address_Country", "Country Reference ID"),
        ("Home_Address_City","Municipality"),
        ("Home_Address_Region","Country Region Reference ID"),
        ("Postal_Code","Postal Code"),
    ],
    "Grid-4": [
        ("Beneficiary_ID", "Change Beneficiary Key"),
        ("Home_Address_Line_1","Address Line Data"),
    ],
    "Grid-9": [
        ("Beneficiary_ID", "Change Beneficiary Key"),
        ("Home_Phone_Number", "Phone Number"),
        ("Home_Phone_Country","Country ISO Code"),
        ("Home_Phone_Device_Type","Phone Device Type Reference ID"),
        ("Home_Phone_Extension","Phone Extension"),
    ],
    "Grid-12": [
        ("Beneficiary_ID", "Change Beneficiary Key"),
        ("Email_Address","Email Address"),
    ],
    "National ID": [
        ("Beneficiary_ID", "Change Beneficiary Key"),
        ("National_ID", "National ID Key"),
        ("National_ID", "ID"),
        ("National_ID_Type", "ID Type Reference ID"),
        ("National_ID_Country", "Country Reference ID")
    ],
    "Court Order": [
        ("Beneficiary_ID", "Change Beneficiary Key"),
        ("Court_Order_Benefit_Coverage_Type", "Benefit Coverage Type Reference ID"),
        ("Court_Order_Start_Date", "Start Date"),
        ("Court_Order_End_Date", "End Date"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
    "Grid-3": ("Home_Address_Country", "Exclude Blanks"),
    "Grid-4": ("Home_Address_Country", "Exclude Blanks"),
    "Grid-9": ("Home_Phone_Number", "Exclude Blanks"),
    "Grid-12": ("Email_Address", "Exclude Blanks"),
    "National ID": ("National_ID", "Exclude Blanks"),
    "Court Order": ("Court_Order_Benefit_Coverage_Type", "Exclude Blanks"),
}

# Define the header row for each sheet
header_rows = {
    "Change Beneficiary": 7,
    "Person Data": 8,
    "Grid-2": 12,
    "Grid-3": 13,
    "Grid-4": 11,
    "Grid-9": 13,
    "Grid-12": 13,
    "National ID": 12,
    "Court Order": 9,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Change Beneficiary": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None),
        ("Employee Reference ID type", "Employee_ID", None),
    ],
    "Person Data": [
        ("Person Data Key", "1", None), 
        ("Existing Related Person Reference ID type", "Dependent_ID", "Existing Related Person Reference ID"), 
        ("Related Person Relationship Reference ID type", "Related_Person_Relationship_ID", None),
    ],
    "Grid-2": [
        ("Person Data Key", "1", None), 
        ("Beneficiary Person Personal Information Data Key","1",None),
        ("Country Reference ID type","ISO_3166-1_Alpha-3_Code",None),
        ("Title Reference ID type", "Predefined_Name_Component_ID", "Title Reference ID"),
        ("Social Suffix Reference ID type", "Predefined_Name_Component_ID", "Social Suffix Reference ID"),
        ("Gender Reference ID type","Gender_Code","Gender Reference ID")
    ],
    "Grid-3": [
        ("Person Data Key", "1", None), 
        ("Beneficiary Person Personal Information Data Key","1",None),
        ("Address Data Key","1",None),
        ("Effective Date","1900-01-01", None), 
        ("Country Reference ID type", "ISO_3166-1_Alpha-3_Code", None),
        ("Country Region Reference ID type","Country_Region_ID",None),
        ("Public","0",None),
        ("Primary","1",None),
        ("Type Reference ID type","Communication_Usage_Type_ID",None),
        ("Type Reference ID","Home",None)
    ],
    "Grid-4": [
        ("Person Data Key", "1", None), 
        ("Beneficiary Person Personal Information Data Key","1",None),
        ("Address Data Key","1",None),
        ("Address Line Data Key","1",None),
        ("Address Line Data Type", "Address_Line_1", None),
    ],
    "Grid-9": [
        ("Person Data Key", "1", None), 
        ("Beneficiary Person Personal Information Data Key","1",None),
        ("Phone Data Key","1",None),
        ("Phone Device Type Reference ID type","Phone_Device_Type_ID",None),
        ("Public","0",None),
        ("Primary","1",None),
        ("Type Reference ID type","Communication_Usage_Type_ID",None),
        ("Type Reference ID","Home",None)
    ],
    "Grid-12": [
        ("Person Data Key", "1", None), 
        ("Beneficiary Person Personal Information Data Key","1",None),
        ("Email Address Data Key","1", None),
        ("Public","0",None),
        ("Primary","1",None),
        ("Type Reference ID type","Communication_Usage_Type_ID",None),
        ("Type Reference ID","Home",None)
    ],
    "National ID": [
        ("Person Data Key", "1", None), 
        ("Beneficiary Person Personal Information Data Key","1",None),
        ("ID Type Reference ID type", "National_ID_Type_Code", None), 
        ("Country Reference ID type", "ISO_3166-1_Alpha-3_Code", None)
    ],
    "Court Order": [
        ("Person Data Key", "1", None), 
        ("Court Order Key", "1", None), 
        ("Benefit Coverage Type Reference ID type", "Benefit_Coverage_Type_ID", None)
    ],


}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)
