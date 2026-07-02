import os
import pandas as pd

def load_files_from_documents():
    # Get the path to the Documents directory
    documents_path = os.path.join(os.path.expanduser("~"), "Documents")
    
    # Define the file names (HCM files)
    file_names = [
        "HCM10.xlsx", "HCM01.xlsx", "HCM02.xlsx", "HCM03.xlsx", 
        "HCM04.xlsx", "HCM05.xlsx", "HCM06.xlsx", "HCM20.xlsx", 
        "HCM40.xlsx", "HCM41.xlsx", "BEN05.xlsx", "BEN06.xlsx",
        "CUS01.xlsx", "CUS02.xlsx", "CUS03.xlsx", "CUS04.xlsx", 
        "CUS08.xlsx", "CUS10.xlsx", "HCM50.xlsx", "HCM29.xlsx", 
        "HCM28.xlsx", "HCM18.xlsx", "BEN00.xlsx", "HCMConfig10.xlsx",
        "BEN01Dependents.xlsx", "BEN01Trusts.xlsx", "BEN01Beneficiaries.xlsx",
        "BEN03.xlsx", "BEN04.xlsx","BEN08.xlsx", "BEN01.xlsx","PAY03.xlsx",
        "BEN07.xlsx", "PAY20.xlsx", "PAY01.xlsx","PAY02.xlsx","PAY10.xlsx",
        "HCM00.xlsx","HCM00.xlsx","HCM10.xlsx","HCM11.xlsx","HCM17.xlsx", "HCM16.xlsx",
        "HCM30.xlsx","HCM31.xlsx", "HCM27.xlsx", "CUS07.xlsx", "CUS12.xlsx",
        "CUS20.xlsx", "CUS21.xlsx","CUS22.xlsx","CUS23.xlsx", "SUP01.xlsx",
        "SUP02.xlsx", "SUP03.xlsx", "SUP04.xlsx", "SUP05.xlsx", "SUP06.xlsx",
        "SUP07.xlsx", "SUP08.xlsx", "SUP09.xlsx", "SUP10.xlsx", "SUP11.xlsx",
        "SUP12.xlsx", "SUP13.xlsx", "SUP14.xlsx", "SUP15.xlsx", "SUP16.xlsx",
        "SUP20.xlsx", "SUP21.xlsx", "SUP22.xlsx", "SUP23.xlsx", "SUP24.xlsx",
        "SUP25.xlsx", "HCM13.xlsx", "PAY04.xlsx","CUS11.xlsx", "HCM42.xlsx",
        "PAY11.xlsx", "PAY12.xlsx", "PAY08.xlsx","HCM24.xlsx", "HCM12.xlsx", "HCM00.xlsx",
        "HCM38.xlsx","HCM26.xlsx","HCM15.xlsx","BEN09.xlsx",
    ]
    
    # Dictionary to store the DataFrames
    file_data = {}
    
    # Loop through the file names and attempt to load each file
    for file_name in file_names:
        file_path = os.path.join(documents_path, file_name)
        try:
            # Load the Excel file into a DataFrame
            df = pd.read_excel(file_path, dtype=str)
            # Save it in the dictionary with the file name (without .xlsx)
            file_data[file_name.split(".")[0]] = df
            print(f"{file_name} loaded successfully.")
        except FileNotFoundError:
            print(f"{file_name} not found in {documents_path}. Skipping.")
        except Exception as e:
            print(f"Error loading {file_name}: {e}")
    
    if not file_data:
        print("No files were loaded.")
    else:
        print(f"Successfully loaded {len(file_data)} files.")
    
    return file_data

if __name__ == "__main__":
    load_files_from_documents()
