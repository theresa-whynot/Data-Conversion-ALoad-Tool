import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\SUP05_Supplier_Alternate_Names.5.6.26_NM.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Suppliers__NKU_GOLD.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Grid-30": [
        ("Supplier_ID", "Supplier Key"),
        ("Supplier_Alternate_Name", "Business Entity Alternate Name Data Key"),
        ("Supplier_Alternate_Name", "Alternate Name"),
    ],
    "Alternate Name Usage Reference": [
        ("Supplier_ID", "Supplier Key"),
        ("Supplier_Alternate_Name", "Business Entity Alternate Name Data Key"),
        ("Alternate_Name_Usage_ID", "Alternate Name Usage Reference Key"),
        ("Alternate_Name_Usage_ID", "ID"),
    ],
}
# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Grid-30": 7,
    "Alternate Name Usage Reference": 8,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Alternate Name Usage Reference": [
        ("ID type","Alternate_Name_Usage_ID", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)