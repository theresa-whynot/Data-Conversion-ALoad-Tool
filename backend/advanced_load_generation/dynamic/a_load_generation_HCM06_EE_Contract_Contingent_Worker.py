import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from a_load_generation import transfer_data_multiple_sheets

source_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\CATS\HCM06_Contract_Contingent_Worker 2026-05-06.xlsx"
target_file = r"C:\Users\TheresaReinhard\OneDrive - AVAAP\Documents\CATS\Contract Contingent Workers_CW_CATS.xlsx"

# Define the mapping for each sheet
sheet_column_map = {
    "Contingent Worker Data": [
        ("Worker_ID", "Contingent Worker Data Key"),
        ("Worker_ID", "Applicant Reference ID"),
        ("Worker_ID", "Contingent Worker ID"),
        ("Contract_Start_Date", "Contract Begin Date"),
        ("Contract_End_Date", "Contract End Date"),
        ("Position_Start_Date_For_Conversion", "Position Start Date for Conversion"),
        ("Supervisory_Organization_Reference_ID", "Organization Reference ID"),
        ("Position_Reference_ID", "Position Reference ID"),
        ("Position_Reference_ID", "Position ID"),
        ("Contingent_Worker_Type_Reference_ID", "Contingent Worker Type Reference ID"),
        ("Job_Profile_Reference_ID", "Job Profile Reference ID"),
        ("Position_Title", "Position Title"),
        ("Business_Title", "Business Title"),
        ("Location_Reference_ID", "Location Reference ID"),
        ("Position_Time_Type_Reference_ID", "Position Time Type Reference ID"),
        ("Default_Weekly_Hours", "Default Weekly Hours"),
        ("Scheduled_Weekly_Hours", "Scheduled Weekly Hours"),
        ("Work_Shift_Reference_ID", "Work Shift Reference ID"),
        ("User_Name", "User Name"),
        ("Contract_Pay_Rate", "Contract Pay Rate"),
        ("Currency_Reference_ID", "Currency Reference ID"),
        ("Frequency_Reference_ID", "Frequency Reference ID"),
    ],
}

# Define filters and subfilters for each sheet
filters = {
}

# Define the header row for each sheet
header_rows = {
    "Contingent Worker Data": 8,
}

# Define default columns for each sheet (optional)
default_columns = {
    "Contingent Worker Data": [
        ("Applicant Reference ID type", "Applicant_ID", None),
        ("Organization Reference ID type","Organization_Reference_ID", None),
        ("Position Reference ID type","Position_ID", None),
        ("Contingent Worker Type Reference ID type","Contingent_Worker_Type_ID", None),
        ("Job Profile Reference ID type","Job_Profile_ID", None),
        ("Location Reference ID type","Location_ID", None),
        ("Position Time Type Reference ID type","Position_Time_Type_ID", None),
        ("Work Shift Reference ID type","Work_Shift_ID", "Work Shift Reference ID"),
        ("Currency Reference ID type","Currency_ID", "Currency Reference ID"),
        ("Frequency Reference ID type","Frequency_ID", "Frequency Reference ID"),
        ("Generate Random Password","1", None),
        

    ],
}

# Run the data transfer with filtering and default columns
transfer_data_multiple_sheets(source_file, target_file, sheet_column_map, filters, header_rows, default_columns)