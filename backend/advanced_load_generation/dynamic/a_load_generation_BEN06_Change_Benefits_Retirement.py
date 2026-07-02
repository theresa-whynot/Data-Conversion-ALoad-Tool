import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets



# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\Monroe County\Gold Build\catchup\R2\BEN06_R2_aload.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\Monroe County\Gold Build\catchup\R2\Change Benefits for Life Event_BEN06_Retirement_R2.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Change Benefits": [
        ("Employee_ID", "Change Benefits Key"),
        ("Employee_ID", "Employee Reference ID"),
        ("Most_Recent_Enrollment_Date", "Event Date"),
    ],
    "Benefit Event Type Reference": [
        ("Employee_ID", "Change Benefits Key"),
    ],
    "Benefit Election Data": [
        ("Employee_ID", "Change Benefits Key"),
        ("Retirement_Savings_Plan_ID","Benefit Election Data Key"),
        ("Most_Recent_Enrollment_Date", "Coverage Begin Date"),
        ("Original_Coverage_Begin_Date", "Original Coverage Begin Date"),
    ],
    "Grid-6": [
        ("Employee_ID", "Change Benefits Key"),
        ("Retirement_Savings_Plan_ID","Benefit Election Data Key"),
        ("Retirement_Savings_Plan_ID","Retirement Savings Election Data Key"),
        ("Retirement_Savings_Plan_ID","Retirement Savings Plan Reference ID"),
        ("Election_Percentage","Election Percentage"),
        ("Election_Amount","Election Amount"),
    ],
    "Grid-7": [
        ("Employee_ID", "Change Benefits Key"),
        ("Retirement_Savings_Plan_ID","Benefit Election Data Key"),
        ("Retirement_Savings_Plan_ID","Retirement Savings Election Data Key"),
        ("Beneficiary_ID","Beneficiary Allocation Data Key"),
        ("Beneficiary_ID","Beneficiary Reference ID"),
        ("Primary_Percentage", "Primary Percentage"),
        ("Contingent_Percentage","Contingent Percentage"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
    "Change Benefits": [("Waive", "No")],
    "Benefit Event Type Reference": [("Waive", "No")],
    "Benefit Election Data": [("Waive", "No")],
    "Grid-6": [("Waive", "No")],
    "Grid-7": [("Waive", "No"), ("Beneficiary_ID","Exclude Blanks")],
}

# Define the header row for each sheet
header_rows = {
    "Change Benefits": 7,
    "Benefit Event Type Reference": 6,
    "Benefit Election Data": 6,
    "Grid-6": 9,
    "Grid-7": 10,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Change Benefits": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None),
        ("Employee Reference ID type", "Employee_ID", None),
    ],
    "Benefit Event Type Reference": [
        ("Benefit Event Type Reference Key","Conversion_Retirement", None),
        ("ID type","Benefit_Event_Type_ID", None),
        ("ID","Conversion_Retirement", None),
    ],
    "Grid-6": [
        ("Retirement Savings Plan Reference ID type", "Benefit_Plan_ID", None),
    ],
    "Grid-7": [
        ("Beneficiary Reference ID type", "Beneficiary_ID", "Beneficiary Reference ID"),
    ],

}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)