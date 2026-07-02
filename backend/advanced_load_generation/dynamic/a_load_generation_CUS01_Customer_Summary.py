import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\CUS_01_New.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Customers_NKU_SBX_NEW.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Customer": [
        ("Customer_ID", "Customer Key"),
        ("Customer_ID", "Customer ID"),
        ("Legacy_Customer_ID", "Customer Data - Customer Reference ID"),
        ("Customer_Name", "Customer Name"),
        ("Customer_Category_Reference_ID","Customer Category Reference ID"),
        ("Default_Payment_Terms_Reference_ID", "Payment Terms Reference ID"),
        ("Default_Payment_Type_Reference_ID", "Default Payment Type Reference ID"),
        ("Default_Currency_Reference_ID", "Currency Reference ID"),
        ("Customer_Name", "Business Entity Name"),
    ],
    "Tax ID Data": [
        ("Customer_ID", "Customer Key"),
        ("Tax_Identification_Number", "Tax ID Text"),
        ("Tax_Authority_Form_Type_Reference_ID", "Tax ID Type Reference ID"),
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
    "Customer": 7,
    "Tax ID Data": 8,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Customer": [
        ("Auto Complete", "1", None), 
        ("Add Only", "1", None),
        ("Submit", "1", None),
        ("Payment Terms Reference ID type", "Payment_Terms_ID", None),
        ("Currency Reference ID type", "Currency_ID", None),
        ("Default Payment Type Reference ID type", "Payment_Type_ID", None),
        ("Customer Category Reference ID type", "Customer_Category_ID", None),
        ("Customer Category Reference ID type", "Customer_Category_ID", None),

    ],
    "Tax ID Data": [
        ("Tax ID Data Key","1", None),
        ("Tax ID Type Reference ID type","Tax_ID_Type", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)