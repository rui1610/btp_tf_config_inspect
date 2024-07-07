from libs.model.provider import TF_provider as ProviderDefinition
from dataclasses import dataclass
from libs.constants.variables import BTP_PROVIDER_MANDATORY_VARIABLES, CF_PROVIDER_MANDATORY_VARIABLES, BTP_PROVIDER_MANDATORY_RESOURCES, CF_PROVIDER_MANDATORY_RESOURCES
from libs.model.finding import Finding


@dataclass
class TF_Provider(ProviderDefinition):
    """
    Represents a Terraform provider.

    Args:
        folder (str): The folder path of the provider.
        provider (str): The name of the provider.
        tf_definitions (dict): The Terraform definitions.

    Attributes:
        mandatory_variables (list): The list of mandatory variables for the provider.
        mandatory_resources (list): The list of mandatory resources for the provider.
        findings (list): The list of findings for the provider.

    """

    def __init__(self, folder, provider, tf_definitions):
        super().__init__(folder, tf_definitions)

        if provider == "btp":
            self.mandatory_variables = BTP_PROVIDER_MANDATORY_VARIABLES
            self.mandatory_resources = BTP_PROVIDER_MANDATORY_RESOURCES
        else:
            self.mandatory_variables = CF_PROVIDER_MANDATORY_VARIABLES
            self.mandatory_resources = CF_PROVIDER_MANDATORY_RESOURCES

        # only execute if the provider is btp or cloudfoundry
        if provider in ["btp", "cloudfoundry"]:
            self._check_variables_mandatory(provider, tf_definitions)
            self._check_resources_mandatory(provider, tf_definitions)
            self.folder = folder
        else:
            self = None

    def _check_variables_mandatory(self, provider, tf_definitions):
        """
        Checks if the mandatory variables are defined in the Terraform definitions.

        Args:
            provider (str): The name of the provider.
            tf_definitions (dict): The Terraform definitions.

        """

        for variable in self.mandatory_variables:
            if variable not in tf_definitions["variables"]:
                finding = Finding(provider=provider,
                                  folder=self.folder,
                                  asset=variable,
                                  type="variable not defined",
                                  severity="error")
                self.findings.append(finding)

    def _check_resources_mandatory(self, provider, tf_definitions):
        """
        Checks if the mandatory resources are defined in the Terraform definitions.

        Args:
            provider (str): The name of the provider.
            tf_definitions (dict): The Terraform definitions.

        """

        for resource in self.manadatory_resources:
            # check whether the resource is in the tf_definitions["managed_resources"] or in the tf_definitions["managed_resources"] split with a "."
            if resource not in tf_definitions["managed_resources"] and not any([resource in managed_resource.split(".") for managed_resource in tf_definitions["managed_resources"]]):
                finding = Finding(provider=provider,
                                  folder=self.folder,
                                  asset=resource,
                                  type="resource not defined",
                                  severity="error")
                self.findings.append(finding)
