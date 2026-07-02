import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\SUP16_Supplier_Classification.5.6.26._NM.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Suppliers__NKU_GOLD.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Supplier Classification Data": [
        ("Supplier_ID", "Supplier Key"),
        ("Supplier_Classification", "Supplier Classification Data Key"),
        ("Supplier_Classification", "Supplier Classification Reference - Supplier Classification Reference ID"),
    ],
}
# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Supplier Classification Data": 8,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Supplier Classification Data": [
        ("Supplier Classification Reference ID type","Custom_Supplier_Classification_ID", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)