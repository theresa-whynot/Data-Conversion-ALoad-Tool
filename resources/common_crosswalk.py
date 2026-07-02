import json
import sys
import pandas as pd
from sharepoint_utils import get_access_token, make_api_request
from load_config import load_config

# Check if a project name is provided as a command-line argument
if len(sys.argv) > 1:
    project_name = sys.argv[1]  # Get the project name from command-line args
else:
    raise ValueError("Please provide a project name as a command-line argument.")

# Load the configuration dynamically
config = load_config(project_name)
shared_config = config["shared_config"]

# Extract shared config fields
tenant_id = shared_config["tenant_id"]
client_id = shared_config["client_id"]
site_url = shared_config["site_url"]
cert_path = shared_config["cert_path"]
cert_password = shared_config["cert_password"]
thumbprint = shared_config["thumbprint"]
common_crosswalk_sharepoint_list = shared_config["common_crosswalk_sharepoint_list"]

def get_list_data_by_title(access_token, site_url, common_crosswalk_sharepoint_list, top=100000):
    """
    Retrieve data from a specific SharePoint list by name.
    """
    endpoint = f"{site_url}/_api/web/lists/getbytitle('{common_crosswalk_sharepoint_list}')/items?$top={top}"
    return make_api_request(access_token, endpoint)

# Execution
try:
    token = get_access_token(tenant_id, client_id, cert_path, cert_password, thumbprint)
    print("Access token obtained.")

    list_data = get_list_data_by_title(token, site_url, common_crosswalk_sharepoint_list)
    print("List Data:", json.dumps(list_data, indent=4))

    # Extract relevant data into a DataFrame
    extracted_data = []
    for item in list_data.get('d', {}).get('results', []):
        extracted_data.append({
            "Title": item.get("Title", ""),
            "OldValue": item.get("OldValue", ""),
            "NewValue": item.get("NewValue", ""),
            "Active": item.get("Active", False)
        })

    # Convert to DataFrame
    df = pd.DataFrame(extracted_data)
    print("Extracted DataFrame:")
    print(df)

except ValueError as e:
    print(f"Error: {e}")