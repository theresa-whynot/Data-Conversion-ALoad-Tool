import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\SUP02_Supplier_Emails.5.6.26_NM.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Suppliers__NKU_GOLD.xlsx"


# Define the mapping for each sheet
sheet_column_map = {
    "Email Address Data": [
        ("Supplier_ID", "Supplier Key"),
        ("Email_Address", "Email Address Data Key"),
        ("Email_Address", "Email Address"),
        ("Visibility", "Public"),
        ("Primary", "Primary"),
        ("Communication_Usage_Type_Reference_ID", "Type Reference ID"),
    ],
    "Grid-10": [
        ("Supplier_ID", "Supplier Key"),
        ("Email_ID", "Email Address Data Key"),
        (("Usage_1", "Usage_2", "Usage_3", "Usage_4"), "Use For Reference Key", "stack"),
        (("Usage_1", "Usage_2", "Usage_3", "Usage_4"), "ID", "stack"),
    ],
}
# Define filters and subfilters for each sheet
filters = {
    "Grid-10": [("Usage_1","Exclude Blanks")],
}

# Define the header row for each sheet
header_rows = {
    "Email Address Data": 11,
    "Grid-10": 10,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Email Address Data": [
        ("Type Reference ID type", "Communication_Usage_Type_ID", None), 
    ],
    "Grid-10": [
        ("ID type","Communication_Usage_Behavior_ID", "ID"),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)