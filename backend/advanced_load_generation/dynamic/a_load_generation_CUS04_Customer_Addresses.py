import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\CUS_04_New.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Customers_NKU_SBX_NEW.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Customer - Address Data": [
        ("Customer_ID", "Customer Key"),
        ("Address_Line_1", "Address Data Key"),
        ("Country_Reference_ID", "Country Reference ID"),
        ("Municipality", "Municipality"),
        ("Country_Region_Reference_ID", "Country Region Reference ID"),
        ("Postal_Code", "Postal Code"),
        ("Visibility", "Public"),
        ("Primary", "Primary"),
        ("Communication_Usage_Type_Reference_ID", "Type Reference ID"),
    ],
    "Grid-3": [
        ("Customer_ID", "Customer Key"),
        ("Address_Line_1", "Address Data Key"),
        (("Address_Line_1", "Address_Line_2"), "Address Line Data Key", "stack"),
        (("Address_Line_1", "Address_Line_2"), "Address Line Data", "stack"),
    ],
    "Grid-6": [
        ("Customer_ID", "Customer Key"),
        ("Address_Line_1", "Address Data Key"),
        (("Usage_1", "Usage_2", "Usage_3"), "Use For Reference Key", "stack"),
        (("Usage_1", "Usage_2", "Usage_3"), "ID", "stack"),
    ],
}
# Define filters and subfilters for each sheet
filters = {
        "Grid-6": [("Usage_1","Exclude Blanks")],
}

# Define the header row for each sheet
header_rows = {
    "Customer - Address Data": 11,
    "Grid-3": 9,
    "Grid-6": 10,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Customer - Address Data": [
        ("Type Reference ID type", "Communication_Usage_Type_ID", None), 
        ("Effective Date", "1900-01-01", None), 
        ("Country Reference ID type", "ISO_3166-1_Alpha-3_Code", None), 
        ("Country Region Reference ID type", "Country_Region_ID", None), 
    ],
    "Grid-3": [
        ("Address Line Data Key","1", None),
        ("Address Line Data Type","ADDRESS_LINE_1", None),
    ],
    "Grid-6": [
        ("ID type","Communication_Usage_Behavior_ID", "ID"),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)