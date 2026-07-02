import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets


# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\CUS_03_New.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Customers_NKU_SBX_NEW.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Phone Data": [
        ("Customer_ID", "Customer Key"),
        ("Phone_Number", "Phone Data Key"),
        ("Country_Reference_ID", "Country ISO Code"),
        ("Phone_Number", "Phone Number"),
        ("Phone_Extension", "Phone Extension"),
        ("Phone_Device_Type_Reference_ID", "Phone Device Type Reference ID"),
        ("Visibility", "Public"),
        ("Primary", "Primary"),
        ("Type_Reference_ID", "Type Reference ID"),
    ],
    "Phone Data - Use For Reference": [
        ("Customer_ID", "Customer Key"),
        ("Phone_Number", "Phone Data Key"),
        (("Usage_1", "Usage_2", "Usage_3"), "Use For Reference Key", "stack"),
        (("Usage_1", "Usage_2", "Usage_3"), "ID", "stack"),
    ],
}
# Define filters and subfilters for each sheet
filters = {
        "Phone Data - Use For Reference": [("Usage_1","Exclude Blanks")],
}

# Define the header row for each sheet
header_rows = {
    "Phone Data": 11,
    "Phone Data - Use For Reference": 10,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Phone Data": [
        ("Phone Device Type Reference ID type", "Phone_Device_Type_ID", None), 
        ("Type Reference ID type", "Communication_Usage_Type_ID", None), 
    ],
    "Phone Data - Use For Reference": [
        ("ID type","Communication_Usage_Behavior_ID", "ID"),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)