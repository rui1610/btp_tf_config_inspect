from dataclasses import dataclass
from pathlib import Path


@dataclass
class Finding:
    provider: str
    folder: Path
    asset: str
    type: str
    severity: str
