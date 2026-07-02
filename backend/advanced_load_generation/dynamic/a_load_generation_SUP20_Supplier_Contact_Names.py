import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\SUP20_Supplier_Contact_Name_5.6.26._NM.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Business Entity Contacts_NKU_GOLD.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Business Entity Contact": [
        ("Supplier_Contact_ID", "Business Entity Contact Key"),
        ("Supplier_Contact_ID", "Business Entity Contact ID"),
        ("Supplier_ID", "Supplier Reference ID"),
        ("Supplier_ID", "Supplier Reference Descriptor"),
    ],
    "Name Data": [
        ("Supplier_Contact_ID", "Business Entity Contact Key"),
        ("Supplier_Contact_ID", "Name Data Key"),
        ("Country_Reference_ID", "Country Reference ID"),
        ("Prefix_Reference_ID", "Title Reference ID"),
        ("First_Name", "First Name"),
        ("Middle_Name", "Middle Name"),
        ("Last_Name", "Last Name"),
        ("Suffix", "Social Suffix Reference ID"),
    ],
}
# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Business Entity Contact": 7,
    "Name Data": 10,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Business Entity Contact": [
        ("Add Only","1", None),
        ("Supplier Reference ID type","Supplier_Reference_ID", None),
    ],
    "Name Data": [
        ("Country Reference ID type","ISO_3166-1_Alpha-3_Code", None),
        ("Social Suffix Reference ID type","Predefined_Name_Component_ID", "Social Suffix Reference ID"),
        ("Title Reference ID type","Predefined_Name_Component_ID", "Title Reference ID"),
    ],


}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)