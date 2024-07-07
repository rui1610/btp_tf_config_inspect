from dataclasses import dataclass
from pathlib import Path

@dataclass
class BTP_provider:
    mandatory_variables: list
    forbidden_variables: list
    required_resources: list
    forbidden_resources: list
    required_provider: str = "sap/btp"
    required_version: str = "~> 1.4.0"

