import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets

# Define the file paths
source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\HCM40 EE Additional Positions_4.27.26SB.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\NKU\a_load\Add Additional Jobs_NKU_GOLD.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Add Additional Job": [
        ("Position_Reference_ID", "Add Additional Job Key"),
        ("Worker_ID", "Employee Reference ID"),
        ("Additional_Jobs_Start_Date", "Start Date"),
        ("Position_Start_Date_For_Conversion", "Conversion Position Start Date"),
        ("Supervisory_Organization_Reference_ID", "Organization Reference ID"),
        ("Position_Reference_ID", "Position Reference ID"),
        ("Position_Reference_ID", "Position ID"),
        ("Employee_Type_Reference_ID", "Employee Type Reference ID"),
        ("End_Employment_Date", "End Employment Date"),
        ("Job_Profile_Reference_ID", "Job Profile Reference ID"),
        ("Position_Title", "Position Title"),
        ("Business_Title", "Business Title"),
        ("Location_Reference_ID", "Location Reference ID"),
        ("Position_Time_Type_Reference_ID", "Position Time Type Reference ID"),
        ("Default_Weekly_Hours", "Default Hours"),
        ("Scheduled_Weekly_Hours", "Scheduled Hours"),
        ("Work_Shift_Reference_ID", "Work Shift Reference ID"),
        ("Pay_Rate_Type_Reference_ID", "Pay Rate Type Reference ID"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Add Additional Job": 11,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Add Additional Job": [
        ("Auto Complete", "1", None), 
        ("Run Now", "1", None),
        ("Employee Reference ID type", "Employee_ID", None),
        ("Organization Reference ID type","Organization_Reference_ID", None),
        ("Position Reference ID type","Position_ID", None),
        ("Employee Type Reference ID type","Employee_Type_ID", None),
        ("Job Profile Reference ID type","Job_Profile_ID", None),
        ("Location Reference ID type","Location_ID", None),
        ("Position Time Type Reference ID type","Position_Time_Type_ID", None),
        ("Work Shift Reference ID type","Work_Shift_ID", "Work Shift Reference ID"),
        ("Pay Rate Type Reference ID type","Pay_Rate_Type_ID", None),
    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)