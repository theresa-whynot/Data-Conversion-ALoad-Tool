import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\SUP08_Supplier_Accepted_Currencies5.6.26_NM.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Suppliers__NKU_GOLD.xlsx"


# Define the mapping for each sheet
sheet_column_map = {
    "Accepted Currencies Reference": [
        ("Supplier_ID", "Supplier Key"),
        ("Accepted_Currency_Reference_ID", "Accepted Currencies Reference Key"),
        ("Accepted_Currency_Reference_ID", "ID"),
    ],
}
# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Accepted Currencies Reference": 6,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Accepted Currencies Reference": [
        ("ID type","Currency_ID", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)