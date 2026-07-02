import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\CUS_12_New.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Customers_NKU_SBX_NEW.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Invoice Delivery Type Reference": [
        ("Customer_ID", "Customer Key"),
        ("Customer_ID", "Invoice Delivery Type Reference Key"),
        ("Invoice_Delivery_Method", "ID"),
    ],
    "Grid-27": [
        ("Customer_ID", "Customer Key"),
        ("Customer_ID", "Invoice Notification Email Recipients Reference Key"),
        ("Invoice_Notification_Email_Recipients", "ID"),
    ],
    "Grid-28": [
        ("Customer_ID", "Customer Key"),
        ("Customer_ID", "Statement Delivery Type Reference Key"),
        ("Statement_Delivery_Method", "ID"),
    ],
    "Grid-29": [
        ("Customer_ID", "Customer Key"),
        ("Customer_ID", "Statement Notification Email Recipients Reference Key"),
        ("Statement_Notification_Email_Recipients", "ID"),
    ],
    "Dunning Delivery Type Reference": [
        ("Customer_ID", "Customer Key"),
        ("Customer_ID", "Dunning Delivery Type Reference Key"),
        ("Dunning_Delivery_Method", "ID"),
    ],
    "Grid-30": [
        ("Customer_ID", "Customer Key"),
        ("Customer_ID", "Dunning Letter Notification Email Recipients Reference Key"),
        ("Dunning_Letter_Notification_Email_Recipients", "ID"),
    ],
}
# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Invoice Delivery Type Reference": 6,
    "Grid-27": 6,
    "Grid-28": 6,
    "Grid-29": 6,
    "Dunning Delivery Type Reference": 6,
    "Grid-30": 6,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Invoice Delivery Type Reference": [
        ("ID type","Document_Delivery_Type_ID", None),
    ],
    "Grid-27": [
        ("ID type","Customer_Document_Email_Recipient_Option_Reference_ID", None),
    ],
    "Grid-28": [
        ("ID type","Document_Delivery_Type_ID", None),
    ],
    "Grid-29": [
        ("ID type","Customer_Document_Email_Recipient_Option_Reference_ID", None),
    ],
    "Dunning Delivery Type Reference": [
        ("ID type","Document_Delivery_Type_ID", None),
    ],
    "Grid-30": [
        ("ID type","Customer_Document_Email_Recipient_Option_Reference_ID", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)