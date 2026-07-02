import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\SUP09_Supplier_Payment.5.14.26.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Suppliers__NKU_GOLD.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Grid-3": [
        ("Supplier_ID", "Supplier Key"),
        ("Accepted_Payment_Type_Reference_ID", "Payment Types Accepted Reference Key"),
        ("Accepted_Payment_Type_Reference_ID", "ID"),
    ],
}
# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Grid-3": 6,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Grid-3": [
        ("ID type","Payment_Type_ID", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)