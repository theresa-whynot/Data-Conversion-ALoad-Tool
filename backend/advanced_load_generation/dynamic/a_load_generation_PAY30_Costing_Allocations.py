import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets



# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\PAY30_CostingAllocations_20260610.xlsx"
target_file = r"C:\Users\TheresaReinhard\Downloads\Costing Allocations_Gol_aload.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Costing Allocation": [
        ("Worker_ID", "Costing Allocation Key"),
        ("Worker_ID", "Worker Reference ID"),
        ("Position_ID", "Position Reference ID"),
    ],
    "Grid-1": [
        ("Worker_ID", "Costing Allocation Key"),
        ("Start_Date", "Start Date"),
        ("End_Date_Future", "End Date"),
    ],
    "Costing Allocation Detail Data": [
        ("Worker_ID", "Costing Allocation Key"),
        ("Row", "Costing Allocation Detail Data Key"),
        ("Company_RefID", "Costing Override Company Reference ID"),
        ("Distribution_Percentage", "Distribution Percent"),
    ],
    "Grid-2": [
        ("Worker_ID", "Costing Allocation Key"),
        ("Row", "Costing Allocation Detail Data Key"),
        (("Cost_Center_RefID", "Fund_RefID", "Function_RefID", "Program_RefID", "Grant_RefID", "Gift_RefID"), "ID", "stack"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Costing Allocation": 7,
    "Grid-1": 6,
    "Costing Allocation Detail Data": 8,
    "Grid-2": 8,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Costing Allocation": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None),
        ("Worker Reference ID type", "Employee_ID", None),
        ("Position Reference ID type", "Position_ID", None),
    ],
    "Grid-1": [
        ("Costing Allocation Interval Data Key", "1", None), 
    ],
    "Costing Allocation Detail Data": [
        ("Costing Allocation Interval Data Key", "1", None),  
        ("Costing Override Company Reference ID type", "Organization_Reference_ID", None), 
    ],
    "Grid-2": [
        ("Costing Allocation Interval Data Key", "1", None),   
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)