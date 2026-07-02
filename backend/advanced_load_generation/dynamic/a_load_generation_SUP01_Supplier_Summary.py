import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\SUP01_Supplier_Summary.5.6.26_NM.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Suppliers__NKU_GOLD.xlsx"


# Define the mapping for each sheet
sheet_column_map = {
    "Supplier": [
        ("Supplier_ID", "Supplier Key"),
        ("Supplier_ID", "Supplier ID"),
        ("Legacy_Supplier_ID", "Supplier Data - Supplier Reference ID"),
        ("Supplier_Name", "Supplier Name"),
        ("Supplier_Category_Reference_ID","Supplier Category Reference ID"),
        ("Default_Payment_Terms_Reference_ID", "Payment Terms Reference ID"),
        ("Default_Payment_Type_Reference_ID", "Default Payment Type Reference ID"),
        ("Supplier_Name", "Business Entity Name"),
        ("Default_Currency_Reference_ID", "Currency Reference ID"),
        ("Tax_Authority_Form_Type_Reference_ID", "Tax Authority Form Type Reference ID"),
        ("IRS_1099_Supplier", "IRS 1099 Supplier"),
        ("Integration_System_Reference_ID", "Integration System Reference ID"),
        ("DUNS_Number", "DUNS Number"),
        ("Customer_Account_Number", "Customer Account Number"),
        ("Certificate_Of_Insurance_Date", "Certificate of Insurance Date"),
    ],
    "Tax ID Data": [
        ("Supplier_ID", "Supplier Key"),
        ("Tax_Identification_Number", "Tax ID Data Key"),
        ("Tax_Identification_Number", "Tax ID Text"),
        ("Tax_ID_Type_Reference_ID", "Tax ID Type Reference ID"),
        ("Transaction_Tax_ID", "Transaction Tax ID"),
        ("Primary_Tax_ID", "Primary Tax ID"),
    ],
}
# Define filters and subfilters for each sheet
filters = {
    "Tax ID Data": [("Tax_Identification_Number", "Exclude Blanks")],
}

# Define the header row for each sheet
header_rows = {
    "Supplier": 7,
    "Tax ID Data": 8,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Supplier": [
        ("Auto Complete", "1", None), 
        ("Add Only", "1", None),
        ("Submit", "1", None),
        ("Approval Status Reference ID type", "Document_Status_ID", None),
        ("Approval Status Reference ID", "APPROVED", None),
        ("Payment Terms Reference ID type", "Payment_Terms_ID", None),
        ("Default Payment Type Reference ID type", "Payment_Type_ID", None),
        ("Supplier Category Reference ID type", "Supplier_Category_ID", None),
        ("Status Reference ID type", "Business_Entity_Status_Value_ID", None),
        ("Status Reference ID", "ACTIVE", None),
        ("Currency Reference ID type", "Currency_ID", None),
        ("Integration System Reference ID type", "Integration_System_ID", "Integration System Reference ID"),
        ("Tax Authority Form Type Reference ID type", "Tax_Authority_Form_Type", "Tax Authority Form Type Reference ID"),

    ],
    "Tax ID Data": [
        ("Tax ID Type Reference ID type","Tax_ID_Type", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)