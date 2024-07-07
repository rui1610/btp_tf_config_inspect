from dataclasses import dataclass, field
from pathlib import Path
from libs.model.finding import Finding


@dataclass
class TF_provider:
    folder: Path
    mandatory_variables: list = field(default_factory=list)
    forbidden_variables: list = field(default_factory=list)
    required_resources: list = field(default_factory=list)
    forbidden_resources: list = field(default_factory=list)
    required_provider: str = None
    required_version: str = None
    findings: list[Finding] = field(default_factory=list)
