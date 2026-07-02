import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\Monroe County\Gold Build\ALOADS\HCMConfig10_aload.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\Monroe County\Gold Build\ALOADS\Hiring Restrictions_MC_GOLD.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Organization Job Group Data": [
        ("Sup_Org_ID", "Organization Job Group Data Key"),
        ("Sup_Org_ID", "Organization Reference ID"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
    "Organization Job Group Data": [("Staffing_Model", "Job Management")],
}

# Define the header row for each sheet
header_rows = {
    "Organization Job Group Data": 7,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Organization Job Group Data": [
        ("Availability Date", "1900-01-01", None),
        ("Earliest Hire Date", "1900-01-01", None),
        ("Organization Reference ID type","Organization_Reference_ID", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)