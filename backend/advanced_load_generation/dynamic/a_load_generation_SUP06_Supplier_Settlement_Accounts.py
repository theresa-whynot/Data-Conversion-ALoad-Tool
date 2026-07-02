import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\SUP06_Supplier_Settlement_Accounts.5.7.26.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Suppliers__NKU_GOLD.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Settlement Account Data": [
        ("Supplier_ID", "Supplier Key"),
        ("Bank_Account_Number", "Settlement Account Data Key"),
        ("Country_Reference_ID", "Country Reference ID"),
        ("Bank_Account_Type_Reference_ID", "Bank Account Type Reference ID"),
        ("Bank_Name", "Bank Name"),
        ("Bank_Account_Number", "Bank Account Number"),
        ("Routing_Transit_Number", "Routing Transit Number"),
    ],
}
# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Settlement Account Data": 8,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Settlement Account Data": [
        ("Country Reference ID type","ISO_3166-1_Alpha-3_Code", None),
        ("Currency Reference ID type","Currency_ID", None),
        ("Currency Reference ID","USD", None),
        ("Bank Account Type Reference ID type","Bank_Account_Type_Code", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)