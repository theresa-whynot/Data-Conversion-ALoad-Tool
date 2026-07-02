import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\Monroe County\Gold Build\catchup\R2\BEN01_R2_aload.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\Monroe County\Gold Build\catchup\R2\Dependents_R2.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Add Dependent": [
        ("Employee_ID", "Employee Reference ID"),
        ("Dependent_ID", "Add Dependent Key"),
        ("Dependent_ID", "Dependent ID"),
        ("Legal_First_Name", "First Name"),
        ("Legal_Middle_Name", "Middle Name"),
        ("Legal_Last_Name", "Last Name"),
        ("Legal_Name_Country", "Country Reference ID"),
        ("Title", "Title Reference ID"),
        ("Suffix", "Social Suffix Reference ID"),
        ("Relationship_to_Employee", "Related Person Relationship Reference ID"),
        ("Use_Employee_Address", "Use Employee Address"),
        ("Use_Employee_Phone", "Use Employee Phone"),
        ("Date_of_Birth","Date of Birth"),
        ("Gender","Gender Reference ID"),
        ("Date_of_Death","Date of Death"),
        ("Uses_Tobacco","Uses Tobacco"),
        ("Full_time_Student","Full-Time Student"),
        ("Disabled","Disabled"),
        ("Dependent_for_Payroll","Dependent for Payroll Purposes"),
        ("Could_be_Covered_Elsewhere","Could Be Covered For Health Care Coverage Elsewhere"),
        ("Could_be_Covered_Elsewhere_Effective_Date","Could Be Covered For Health Care Coverage Elsewhere Effective Date"),
        ("Student_Status_Start_Date","Student Status Start Date"),
        ("Student_Status_End_Date","Student Status End Date")
    ],
    "National ID": [
        ("Dependent_ID", "Add Dependent Key"),
        ("National_ID", "National ID Key"),
        ("National_ID", "ID"),
        ("National_ID_Type", "ID Type Reference ID"),
        ("National_ID_Country", "Country Reference ID")
    ],
    "Address Data": [
        ("Dependent_ID", "Add Dependent Key"),
        ("Home_Address_Country", "Country Reference ID"),
        ("Home_Address_City","Municipality"),
        ("Home_Address_Region","Country Region Reference ID"),
        ("Postal_Code","Postal Code"),
    ],
    "Address Line Data": [
        ("Dependent_ID", "Add Dependent Key"),
        ("Home_Address_Line_1","Address Line Data"),
    ],
    "Email Address Data": [
        ("Dependent_ID", "Add Dependent Key"),
        ("Email_Address","Email Address"),
    ],
    "Phone Data": [
        ("Dependent_ID", "Add Dependent Key"),
        ("Home_Phone_Number", "Phone Number"),
        ("Home_Phone_Country","Country ISO Code"),
        ("Home_Phone_Device_Type","Phone Device Type Reference ID"),
        ("Home_Phone_Extension","Phone Extension"),
    ]
}

# Define filters and subfilters for each sheet
filters = {
    "Add Dependent": ("Is_Dependent", "Yes"),
    "National ID": [("Is_Dependent", "Yes"), ("National_ID", "Exclude Blanks")],  
    "Address Data": [("Is_Dependent", "Yes"), ("Home_Address_Country", "Exclude Blanks")],  
    "Address Line Data": [("Is_Dependent", "Yes"), ("Home_Address_Country", "Exclude Blanks")], 
    "Email Address Data": [("Is_Dependent", "Yes"), ("Email_Address", "Exclude Blanks")],
    "Phone Data": [("Is_Dependent", "Yes"), ("Home_Phone_Number", "Exclude Blanks")],
}

# Define the header row for each sheet
header_rows = {
    "Add Dependent": 10,
    "National ID": 10,
    "Address Data": 11,
    "Address Line Data": 9,
    "Email Address Data": 11,
    "Phone Data": 11,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Add Dependent": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None),
        ("Employee Reference ID type", "Employee_ID", None),
        ("Related Person Relationship Reference ID type", "Related_Person_Relationship_ID", None),
        ("Country Reference ID type","ISO_3166-1_Alpha-3_Code",None),
        ("Title Reference ID type", "Predefined_Name_Component_ID", "Title Reference ID"),
        ("Social Suffix Reference ID type", "Predefined_Name_Component_ID", "Social Suffix Reference ID"),
        ("Gender Reference ID type", "Gender_Code", "Gender Reference ID"),
        ("Effective Date","1900-01-01",None),
    ],
    "National ID": [
        ("Country Reference ID type","ISO_3166-1_Alpha-3_Code",None),
        ("ID Type Reference ID type","National_ID_Type_Code",None),
    ],
    "Address Data": [
        ("Address Data Key", "1", None),
        ("Effective Date","1900-01-01", None), 
        ("Country Reference ID type", "ISO_3166-1_Alpha-3_Code", None),
        ("Country Region Reference ID type","Country_Region_ID",None),
        ("Public","0",None),
        ("Primary","1",None),
        ("Type Reference ID type","Communication_Usage_Type_ID",None),
        ("Type Reference ID","Home",None)
    ],
    "Address Line Data": [
        ("Address Data Key","1",None),
        ("Address Line Data Key","1",None),
        ("Address Line Data Type", "Address_Line_1", None),
        
    ],
    "Email Address Data": [
        ("Email Address Data Key","1", None),
        ("Public","0",None),
        ("Primary","1",None),
        ("Type Reference ID type","Communication_Usage_Type_ID",None),
        ("Type Reference ID","Home",None)
    ],
    "Phone Data": [
        ("Phone Data Key","1",None),
        ("Phone Device Type Reference ID type","Phone_Device_Type_ID",None),
        ("Public","0",None),
        ("Primary","1",None),
        ("Type Reference ID type","Communication_Usage_Type_ID",None),
        ("Type Reference ID","Home",None)
    ]
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)
