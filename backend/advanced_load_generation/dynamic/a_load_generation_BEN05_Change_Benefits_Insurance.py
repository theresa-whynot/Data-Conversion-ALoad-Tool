import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\BEN05.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Change Benefits for Life Event_BEN05_Insurance.xlsx"

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
        ("Insurance_Coverage_Plan_ID","Benefit Election Data Key"),
        ("Most_Recent_Enrollment_Date", "Coverage Begin Date"),
        ("Original_Coverage_Begin_Date", "Original Coverage Begin Date"),
    ],
    "Insurance Election Data": [
        ("Employee_ID", "Change Benefits Key"),
        ("Insurance_Coverage_Plan_ID","Benefit Election Data Key"),
        ("Insurance_Coverage_Plan_ID","Insurance Election Data Key"),
        ("Insurance_Coverage_Plan_ID","Insurance Coverage Plan Reference ID"),
        ("Coverage_Amount","Coverage Amount Reference Descriptor"),
        ("Employee_Cost_Pre_Tax","Employee Cost PreTax"),
        ("Employee_Cost_Post_Tax","Employee Cost PostTax"),
        ("Employer_Cost_Non_Taxable","Employer Cost NonTaxable"),
        ("Employer_Cost_Taxable","Employer Cost Taxable"),
    ],
    "Dependent Reference": [
        ("Employee_ID", "Change Benefits Key"),
        ("Insurance_Coverage_Plan_ID","Benefit Election Data Key"),
        ("Insurance_Coverage_Plan_ID","Insurance Election Data Key"),
        ("Dependent_ID","Dependent Reference Key"),
        ("Dependent_ID","ID"),
    ],
    "Grid-5": [
        ("Employee_ID", "Change Benefits Key"),
        ("Insurance_Coverage_Plan_ID","Benefit Election Data Key"),
        ("Insurance_Coverage_Plan_ID","Insurance Election Data Key"),
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
    "Insurance Election Data": [("Waive", "No")],
    "Dependent Reference": [("Waive", "No"), ("Dependent_ID","Exclude Blanks")],
    "Grid-5": [("Waive", "No"), ("Beneficiary_ID","Exclude Blanks")],
}

# Define the header row for each sheet
header_rows = {
    "Change Benefits": 7,
    "Benefit Event Type Reference": 6,
    "Benefit Election Data": 6,
    "Insurance Election Data": 9,
    "Dependent Reference": 9,
    "Grid-5": 10,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Change Benefits": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None),
        ("Employee Reference ID type", "Employee_ID", None),
    ],
    "Benefit Event Type Reference": [
        ("Benefit Event Type Reference Key","Conversion_Insurance", None),
        ("ID type","Benefit_Event_Type_ID", None),
        ("ID","Conversion_Insurance", None),
    ],
    "Insurance Election Data": [
        ("Insurance Coverage Plan Reference ID type", "Benefit_Plan_ID", None),
        ("Coverage Amount Reference ID type","Currency_Coverage_Master_Amount_ID",None)
    ],
    "Dependent Reference": [
        ("ID type", "Dependent_ID", "ID"),
    ],
    "Grid-5": [
        ("Beneficiary Reference ID type", "Beneficiary_ID", "Beneficiary Reference ID"),
    ],

}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)