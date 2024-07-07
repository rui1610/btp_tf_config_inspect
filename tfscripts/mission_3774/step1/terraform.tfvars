# ------------------------------------------------------------------------------------------------------
# Provider configuration
# ------------------------------------------------------------------------------------------------------
# Your global account subdomain
globalaccount   = "ticrossa"
region          = "us10"
subaccount_name = "SAP Discovery Center Mission 3774 2"

service_plan__build_workzone = "standard"

# ------------------------------------------------------------------------------------------------------
# Project specific configuration (please adapt!)
# ------------------------------------------------------------------------------------------------------

subaccount_admins         = ["thomas.ziegert@sap.com"]
subaccount_service_admins = ["thomas.ziegert@sap.com"]

cf_org_admins       = ["thomas.ziegert@sap.com"]
cf_space_managers   = ["thomas.ziegert@sap.com", "rui.nogueira@sap.com"]
cf_space_developers = ["thomas.ziegert@sap.com", "rui.nogueira@sap.com"]

launchpad_admins = ["thomas.ziegert@sap.com", "rui.nogueira@sap.com"]

create_tfvars_file_for_step2 = true