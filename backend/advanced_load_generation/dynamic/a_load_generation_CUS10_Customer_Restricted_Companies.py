import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets




# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\Monroe County\Gold Build\APPROVED\CUS10 CUSTOMER RESTRICTED COMPANIES 20260427 095830.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\Monroe County\Gold Build\APPROVED\Customers_MC_GOLD.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Grid-1": [
        ("Customer_ID", "Customer Key"),
        ("Restricted_Company_Reference_ID", "Restricted To Companies Reference Key"),
        ("Restricted_Company_Reference_ID", "ID"),
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