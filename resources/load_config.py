import json
import os

# Define the correct path to config.json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, 'config.json')


def load_config(project_name):
    """Load credentials and config for a given project from config.json."""
    
    print(f"Looking for config file at: {CONFIG_FILE}")
    
    if not os.path.exists(CONFIG_FILE):
        raise FileNotFoundError(f"{CONFIG_FILE} not found. Please ensure the config file exists.")
    
    print(f"{CONFIG_FILE} found! Loading configuration...")

    with open(CONFIG_FILE, 'r') as file:
        config = json.load(file)
    
    print(f"Config file loaded. Checking for project '{project_name}'.")

    if "projects" not in config:
        raise KeyError("'projects' key not found in config.json. Please check the structure of the config file.")

    if project_name not in config["projects"]:
        raise KeyError(f"Project '{project_name}' not found in config.json.")

    # Retrieve shared configuration
    shared_config = config.get("shared_config", {})

    # Retrieve the configuration for the specific project
    project_config = config["projects"][project_name]

    hr_system = project_config.get("hr_system", {})
    smartsheet = project_config.get("smartsheet", {})

    loaded_config = {
        "hr_system": {
            "username": hr_system.get("username"),
            "password": hr_system.get("password"),
            "url": hr_system.get("url"),
            "workday_data_center":hr_system.get("workday_data_center"),
            "tenant_name":hr_system.get("tenant_name"),
            "build":hr_system.get("build")
        },
        "smartsheet": {
            "access_token": smartsheet.get("access_token"),
            "client_issue_log_sheet_id": smartsheet.get("client_issue_log_sheet_id"),
            "workday_pre_validations_issue_sheet_id": smartsheet.get("workday_pre_validations_issue_sheet_id")
        },
        "shared_config": shared_config
    }

    # Print the loaded configuration for verification
    print("\nLoaded Configuration:")
    print(json.dumps(loaded_config, indent=4))

    return loaded_config

if __name__ == "__main__":
    print("Program started.")
   
