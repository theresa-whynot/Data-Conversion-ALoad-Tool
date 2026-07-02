import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\SUP14_Supplier_Company_Restrictions.5.6.26_NM.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Suppliers__NKU_GOLD.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Grid-1": [
        ("Supplier_ID", "Supplier Key"),
        ("Company", "Restricted To Companies Reference Key"),
        ("Company", "ID"),
    ],
}
# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Grid-1": 6,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Grid-1": [
        ("ID type","Company_Reference_ID", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)