import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets



# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\PAY20_PaymentElections_20260601.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\Payment Election Enrollments_NKU_GOLD.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Payment Election Enrollment": [
        ("Worker_ID", "Payment Election Enrollment Key"),
        ("Worker_ID", "Role ID Reference ID"),
        ("Country_Reference_ID", "Country Reference ID"),
        ("Currency_Reference_ID", "Currency Reference ID"),
    ],
    "Grid-1": [
        ("Worker_ID", "Payment Election Enrollment Key"),
        ("Payment_Types_Reference_ID", "Payment Election Rule Group Data Key"),
        ("Payment_Types_Reference_ID", "Payment Election Rule Reference ID"),
    ],
    "Payment Election Data": [
        ("Worker_ID", "Payment Election Enrollment Key"),
        ("Payment_Types_Reference_ID", "Payment Election Rule Group Data Key"),
        ("Payment_Types_Reference_ID", "Payment Election Rule Reference ID"),
        ("Priority", "Order"),
        ("Country_Reference_ID", "Country Reference ID"),
        ("Currency_Reference_ID", "Currency Reference ID"),
        ("Payment_Types_Reference_ID", "Payment Type Reference ID"),
        ("Country_Reference_ID", "Worker Bank Account Data - Country Reference ID"),
        ("Currency_Reference_ID", "Worker Bank Account Data - Currency Reference ID"),
        ("Account_Number", "Account Number"),
        ("Account_Type_Reference_ID", "Account Type Reference ID"),
        ("Bank_Name", "Bank Name"),
        ("Routing_Number", "Bank ID Number"),
        ("Amount", "Distribution Amount"),
        ("Percent", "Distribution Percentage"),
        ("Remaining_Balance", "Distribution Balance"),
        ("Expense_Account", "Account Type Reference Descriptor"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Payment Election Enrollment": 7,
    "Grid-1": 7,
    "Payment Election Data": 9,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Payment Election Enrollment": [
        ("Auto Complete", "1", None), 
        ("Role ID Reference ID type", "Employee_ID", None),
        ("Country Reference ID type", "ISO_3166-1_Alpha-3_Code", None),
        ("Currency Reference ID type", "Currency_ID", None),
    ],
    "Grid-1": [
        ("Payment Election Rule Reference ID type", "Payment_Election_Rule_ID", None), 
    ],
    "Payment Election Data": [
        ("Payment Election Data Key", "1", None), 
        ("Payment Election Rule Reference ID type", "Payment_Election_Rule_ID", None), 
        ("Country Reference ID type", "ISO_3166-1_Alpha-3_Code", None), 
        ("Currency Reference ID type", "Currency_ID", None), 
        ("Payment Type Reference ID type", "Payment_Type_ID", None), 
        ("Worker Bank Account Data - Country Reference ID type", "ISO_3166-1_Alpha-3_Code", None), 
        ("Worker Bank Account Data - Currency Reference ID type", "Currency_ID", None), 
        ("Account Type Reference ID type", "Bank_Account_Type_Code", None), 

    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)