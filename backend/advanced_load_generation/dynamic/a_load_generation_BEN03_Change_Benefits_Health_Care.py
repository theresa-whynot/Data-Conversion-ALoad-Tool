import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\BEN03H.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Change Benefits for Life Event_BEN03_Healthcare-history.xlsx"

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
        ("Health_Care_Coverage_Plan_ID","Benefit Election Data Key"),
        ("Most_Recent_Enrollment_Date", "Coverage Begin Date"),
        ("Original_Coverage_Begin_Date", "Original Coverage Begin Date"),
    ],
    "Health Care Election Data": [
        ("Employee_ID", "Change Benefits Key"),
        ("Health_Care_Coverage_Plan_ID","Benefit Election Data Key"),
        ("Health_Care_Coverage_Plan_ID","Health Care Election Data Key"),
        ("Health_Care_Coverage_Plan_ID","Health Care Coverage Plan Reference ID"),
        ("Health_Care_Coverage_Target_ID","Health Care Coverage Target Reference ID"),
        ("Health_Care_Provider_ID","Provider ID"),
        ("Employee_Cost_Pre_Tax","Employee Cost PreTax"),
        ("Employee_Cost_Post_Tax","Employee Cost PostTax"),
        ("Employer_Cost_Non_Taxable","Employer Cost NonTaxable"),
        ("Employer_Cost_Taxable","Employer Cost Taxable"),
    ],
    "Dependent Election Data": [
        ("Employee_ID", "Change Benefits Key"),
        ("Health_Care_Coverage_Plan_ID","Benefit Election Data Key"),
        ("Health_Care_Coverage_Plan_ID","Health Care Election Data Key"),
        ("Dependent_ID","Dependent Election Data Key"),
        ("Dependent_ID", "Dependent Reference ID"),
        ("Dependent_Provider_ID","Provider ID"),
        ("Dependent_Original_Coverage_Begin_Date", "Original Coverage Begin Date"),
    ],

}

# Define filters and subfilters for each sheet
filters = {
    "Change Benefits": [("Waive", "No")],
    "Benefit Event Type Reference": [("Waive", "No")],
    "Benefit Election Data": [("Waive", "No")],
    "Health Care Election Data": [("Waive", "No")],
    "Dependent Election Data": [("Waive", "No"),("Dependent_ID","Exclude Blanks")],
}

# Define the header row for each sheet
header_rows = {
    "Change Benefits": 7,
    "Benefit Event Type Reference": 6,
    "Benefit Election Data": 6,
    "Health Care Election Data": 9,
    "Dependent Election Data": 10,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Change Benefits": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None),
        ("Employee Reference ID type", "Employee_ID", None),
    ],
    "Benefit Event Type Reference": [
        ("Benefit Event Type Reference Key","Conversion_Health_Care", None),
        ("ID type","Benefit_Event_Type_ID", None),
        ("ID","Conversion_Health_Care", None),
    ],

    "Health Care Election Data": [
        ("Health Care Coverage Plan Reference ID type", "Benefit_Plan_ID", None),
        ("Health Care Coverage Target Reference ID type","Health_Care_Coverage_Target_ID",None),
    ],
    "Dependent Election Data": [
        ("Dependent Reference ID type", "Dependent_ID", "Dependent Reference ID"),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)