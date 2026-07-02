import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets



# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\CATS\HCMConfig10.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\CATS\Supervisory Organizations_FOUNDATOIN_CATS.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Supervisory Organization": [
        ("Sup_Org_ID", "Supervisory Organization Key"),
        ("Sup_Org_ID", "Supervisory Organization Reference ID"),
        ("Sup_Org_ID", "ID"),
        ("Sup_Org_Name", "Organization Name"),
        ("Include_Sup_Org_ID_In_Name", "Include Organization ID in Name"),
        ("Code", "Organization Code"),
        ("Include_Manager_In_Name", "Include Leader in Name"),
        ("Sup_Org_Location_ID", "Primary Location Reference ID"),
        ("Staffing_Model", "Job Management Enabled"),
        ("Staffing_Model", "Position Management Enabled"),
        ("Superior_Sup_Org_ID", "Supervisory Organization Superior Reference ID"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Supervisory Organization": 7,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Supervisory Organization": [
        ("Add Only", "0", None), 
        ("Supervisory Organization Reference ID type", "Organization_Reference_ID", None), 
        ("Effective Date", "1900-01-01", None),
        ("Availability Date", "1900-01-01", None),
        ("Organization Active","1", None),
        ("Organization Visibility Reference ID type","WID", None),
        ("Organization Visibility Reference ID","9c875610c4fc496499e39741b6541dbc", None),
        ("Organization Subtype Reference ID type","Organization_Subtype_ID", None),
        ("Organization Subtype Reference ID","Department", None),
        ("Primary Location Reference ID type","Location_ID", None),
        ("Supervisory Organization Superior Reference ID type","Organization_Reference_ID", "Supervisory Organization Superior Reference ID"),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)