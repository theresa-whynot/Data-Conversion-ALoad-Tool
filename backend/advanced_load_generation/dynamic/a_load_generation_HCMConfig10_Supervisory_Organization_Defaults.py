import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets



# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\Monroe County\Gold Build\ALOADS\HCMConfig10_aload.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\Monroe County\Gold Build\ALOADS\Supervisory Organization Assignment Restrictions and Defaults_MC_GOLD.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Grid-1": [
        ("Sup_Org_ID", "Organization Assignment Restrictions Key"),
        ("Sup_Org_ID", "Supervisory Organization Reference ID"),
    ],
    "Grid-2": [
        (("Sup_Org_ID", "Sup_Org_ID", "Sup_Org_ID", "Sup_Org_ID", "Sup_Org_ID", "Sup_Org_ID", "Sup_Org_ID"), "Organization Assignment Restrictions Key", "stack"),
        (("Default_Company", "Default_Cost_Center", "Default_Function", "Default_Business_Unit", "Default_Fund", "Default_Department","Default_Cashflow" ), "Organization Assignment Restrictions by Type Data Key", "stack"),
    ],
    "Default Organization Data": [
        (("Sup_Org_ID", "Sup_Org_ID", "Sup_Org_ID", "Sup_Org_ID", "Sup_Org_ID", "Sup_Org_ID", "Sup_Org_ID"), "Organization Assignment Restrictions Key", "stack"),
        (("Default_Company", "Default_Cost_Center", "Default_Function", "Default_Business_Unit", "Default_Fund", "Default_Department", "Default_Cashflow"), "Organization Assignment Restrictions by Type Data Key", "stack"),
        (("Default_Company", "Default_Cost_Center", "Default_Function", "Default_Business_Unit", "Default_Fund", "Default_Department", "Default_Cashflow"), "Default Organization Data Key", "stack"),
        (("Default_Company", "Default_Cost_Center", "Default_Function", "Default_Business_Unit", "Default_Fund", "Default_Department", "Default_Cashflow"), "Default Organization Reference ID", "stack"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Grid-1": 6,
    "Grid-2": 7,
    "Default Organization Data": 8,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Grid-1": [
        ("Supervisory Organization Reference ID type", "Organization_Reference_ID", None), 
    ],
    "Grid-2": [
        ("Organization Type Reference ID type", "Organization_Type_ID", None), 
    ],
    "Default Organization Data": [
        ("Default Organization Reference ID type", "Organization_Reference_ID", None), 
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)