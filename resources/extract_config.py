import sys
from load_config import load_config


def extract_config(project_name):
    config = load_config(project_name)
    shared = config["shared_config"]
    hr = config["hr_system"]
    smartsheet = config["smartsheet"]

    return {
        "tenant_id": shared["tenant_id"],
        "client_id": shared["client_id"],
        "site_url": shared["site_url"],
        "cert_path": shared["cert_path"],
        "cert_password": shared["cert_password"],
        "thumbprint": shared["thumbprint"],
        "pre_validation_sharepoint_list": shared["pre_validation_sharepoint_list"],
        "username": hr["username"],
        "password": hr["password"],
        "workday_data_center": hr["workday_data_center"],
        "tenant_name": hr["tenant_name"],
        "build": hr["build"],
        "access_token": smartsheet["access_token"],
        "client_issue_log_sheet_id": smartsheet["client_issue_log_sheet_id"],
        "workday_pre_validations_issue_sheet_id": smartsheet["workday_pre_validations_issue_sheet_id"]
    }