import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\Downloads\Business Entity Contacts_2_PCOM_Foundation.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\Lee's Summit\A&C\Supplier Contacts_LS_E2E.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Submit Remit To Supplier Connec": [
        ("Supplier_Connection_ID", "Fields"),
        ("Supplier_Connection_ID", "Spreadsheet Key*"),
        ("Supplier_ID", "Supplier"),
        ("Supplier_ID", "Supplier ID"),
        ("Supplier_Connection_ID", "Supplier Connection ID"),
        ("Supplier_Connection_Name", "Supplier Connection Name*"),
        ("Remit_To_Supplier", "Remit To Supplier*"),
        ("Default_Payment_Type", "Default Payment Type*"),
        ("Accepted_Payment_Type", "Accepted Payment Type*+*"),
        ("Default_Payment_Terms", "Default Payment Terms"),
        ("Do_Not_Pay_During_Bank_Account_Updates", "Do not pay during Bank Account updates"),
        ("Settlement_Bank_Account_ID", "Settlement Bank Account"),
        ("Remit_To_Emails", "Remit To Email Address"),
        ("Remit_To_Address_ID", "Remit To Address"),
        ("Always_Separate_Payments", "Always Separate Payments"),
        ("Payee_Alternate_Name", "Payee Alternate Name*"),
        ("Payment_Memo", "Payment Memo"),
        ("Is_Default", "Is Default"),
    ],
}
# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Submit Remit To Supplier Connec": 5,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Submit Remit To Supplier Connec": [
        ("Auto Complete","Y", None),
        ("Row ID*","1", None),
        ("Remit to Connection Status*", "ACTIVE", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)