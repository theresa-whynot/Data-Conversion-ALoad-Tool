import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\HCM18 Veteran Status_4.28.26SB.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Veteran Status Identifications__NKU_GOLD.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Grid-1": [
        ("Worker_ID", "Change Veteran Status Identification Key"),
        ("Worker_ID", "Worker Reference ID"),
        ("US_Veteran_Status_ID", "US Veteran Tenanted Reference ID"),
        ("Dischage_Date", "Discharge Date"),
    ],
    "Grid-3": [
        ("Worker_ID", "Change Veteran Status Identification Key"),
        ("US_Protected_Veteran_Status_Type_ID_1","US Protected Veteran Status Type Reference Key"),
        ("US_Protected_Veteran_Status_Type_ID_1","ID"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
    "Grid-3": [("US_Protected_Veteran_Status_Type_ID_1", "Exclude Blanks")],
}

# Define the header row for each sheet
header_rows = {
    "Grid-1": 7,
    "Grid-3": 6,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Grid-1": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None),
        ("Worker Reference ID type","Employee_ID", None),
        ("US Veteran Tenanted Reference ID type","US_Veteran_Status__Tenanted__Reference_ID", None),
    ],
    "Custom ID": [
        ("ID type","US_Protected_Veteran_Status_Type_ID", "ID"),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)