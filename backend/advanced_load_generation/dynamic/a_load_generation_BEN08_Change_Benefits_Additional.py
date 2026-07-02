import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\Monroe County\Gold Build\catchup\R2\BEN08_R2_aload.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\Monroe County\Gold Build\catchup\R2\Change Benefits for Life Event_BEN08_Additional_R2.xlsx"

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
        ("Additional_Benefits_Plan_ID","Benefit Election Data Key"),
        ("Most_Recent_Enrollment_Date", "Coverage Begin Date"),
        ("Original_Coverage_Begin_Date", "Original Coverage Begin Date"),
    ],
    "Grid-8": [
        ("Employee_ID", "Change Benefits Key"),
        ("Additional_Benefits_Plan_ID","Benefit Election Data Key"),
        ("Additional_Benefits_Plan_ID","Additional Benefits Election Data Key"),
        ("Additional_Benefits_Plan_ID","Additional Benefits Plan Reference ID"),
        ("Additional_Benefits_Coverage_Target","Additional Benefits Coverage Target Reference ID"),
        ("Additional_Benefits_Flat_Rate","Additional Benefits Flat Contribution Amount"),
        ("Additional_Benefits_Percentage","Additional Benefits Percentage Contribution Value"),
        ("Employee_Cost_Pre_Tax","Employee Cost PreTax"),
        ("Employee_Cost_Post_Tax","Employee Cost PostTax"),
        ("Employer_Cost_Non_Taxable","Employer Cost NonTaxable"),
        ("Employer_Cost_Taxable","Employer Cost Taxable"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
    "Change Benefits": [("Waive", "No")],
    "Benefit Event Type Reference": [("Waive", "No")],
    "Benefit Election Data": [("Waive", "No")],
    "Grid-8": [("Waive", "No")],
}

# Define the header row for each sheet
header_rows = {
    "Change Benefits": 7,
    "Benefit Event Type Reference": 6,
    "Benefit Election Data": 6,
    "Grid-8": 9,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Change Benefits": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None),
        ("Employee Reference ID type", "Employee_ID", None),
    ],
    "Benefit Event Type Reference": [
        ("Benefit Event Type Reference Key","Conversion_Additional_Benefits", None),
        ("ID type","Benefit_Event_Type_ID", None),
        ("ID","Conversion_Additional_Benefits", None),
    ],
    "Grid-8": [
        ("Additional Benefits Plan Reference ID type", "Benefit_Plan_ID", None),
        ("Additional Benefits Coverage Target Reference ID type", "Additional_Benefits_Coverage_Target_ID", "Additional Benefits Coverage Target Reference ID"),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)