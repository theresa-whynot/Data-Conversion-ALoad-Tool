import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets



# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\BEN07_FINAL.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Change Benefits for Life Event_BEN07_Spending_Account.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Change Benefits": [
        ("Employee_ID", "Change Benefits Key"),
        ("Employee_ID", "Employee Reference ID"),
        ("Most_Recent_Enrollment_Date", "Event Date"),
        ("Remaining_Period_Frequency", "Remaining Period Frequency Reference ID"),
        ("Benefit_Deductions_Period_Remaining", "Benefit Deduction Periods Remaining"),
    ],
    "Benefit Event Type Reference": [
        ("Employee_ID", "Change Benefits Key"),
    ],
    "Benefit Election Data": [
        ("Employee_ID", "Change Benefits Key"),
        ("Spending_Account_Plan_ID","Benefit Election Data Key"),
        ("Most_Recent_Enrollment_Date", "Coverage Begin Date"),
        ("Original_Coverage_Begin_Date", "Original Coverage Begin Date"),
    ],
    "Spending Account Election Data": [
        ("Employee_ID", "Change Benefits Key"),
        ("Spending_Account_Plan_ID","Benefit Election Data Key"),
        ("Spending_Account_Plan_ID","Spending Account Election Data Key"),
        ("Spending_Account_Plan_ID","Spending Account Plan Reference ID"),
        ("YTD_Contribution_Amount","YTD Contribution Amount"),
        ("Annual_Contribution_Amount","Annual Contribution"),
        ("Employee_Cost","Employee Cost"),
    ],
    "Grid-4": [
        ("Employee_ID", "Change Benefits Key"),
        ("Health_Savings_Account_Plan_ID","Benefit Election Data Key"),
        ("Health_Savings_Account_Plan_ID","Spending Account Election Data Key"),
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
    "Spending Account Election Data": [("Waive", "No")],
    "Grid-4": [("Waive", "No"), ("Beneficiary_ID","Exclude Blanks")],
}

# Define the header row for each sheet
header_rows = {
    "Change Benefits": 7,
    "Benefit Event Type Reference": 6,
    "Benefit Election Data": 6,
    "Spending Account Election Data": 9,
    "Grid-4": 10,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Change Benefits": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None),
        ("Employee Reference ID type", "Employee_ID", None),
        ("Remaining Period Frequency Reference ID type","Frequency_ID", None),
    ],
    "Benefit Event Type Reference": [
        ("Benefit Event Type Reference Key","Conversion_Spending_Account", None),
        ("ID type","Benefit_Event_Type_ID", None),
        ("ID","Conversion_Spending_Account", None),
    ],
    "Spending Account Election Data": [
        ("Spending Account Plan Reference ID type", "Benefit_Plan_ID", None),
    ],
    "Grid-4": [
        ("Beneficiary Reference ID type", "Beneficiary_ID", "Beneficiary Reference ID"),
    ],

}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)