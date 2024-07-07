BTP_PROVIDER_MANDATORY_VARIABLES = ["globalaccount", "region", "custom_idp", "cli_server_url",
                                    "subaccount_admins", "subaccount_service_admins", "subaccount_name", "subaccount_id"]

CF_PROVIDER_MANDATORY_VARIABLES = ["cf_org_admins", "cf_org_name", "cf_space_developers", "cf_landscape_label", "cf_org_id", "cf_api_url",
                                   "cf_space_managers", "cf_space_name", "cli_server_url", "origin"]

BTP_PROVIDER_MANDATORY_RESOURCES = [
    "btp_subaccount", "btp_subaccount_trust_configuration"]

CF_PROVIDER_MANDATORY_RESOURCES = [
    "cloudfoundry_space", "cloudfoundry_org_role", "cloudfoundry_space_role"]
