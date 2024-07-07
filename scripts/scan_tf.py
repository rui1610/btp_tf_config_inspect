import re
from pathlib import Path
from typing import List
from libs.constants.files_folders import FOLDER_SCRIPTS
from libs.inspect import get_tf_definitions
from libs.inspection.provider import TF_Provider

# read all folders in the tfscripts folder


def get_folders() -> List[Path]:

    # Get all folders and subfolders in the FOLDER_SCRIPTS folder that contain at least one .tf file
    folders = [folder for folder in FOLDER_SCRIPTS.glob("**/*") if folder.is_dir(
    ) and any([re.match(r".*\.tf", file.name) for file in folder.iterdir()])]

    return folders


folders = get_folders()

# iterate through all folders
for folder in folders:
    all_findings = []
    # run the inspect_folder function
    defs = get_tf_definitions(folder)

    for provider in defs["required_providers"]:
        result = TF_Provider(folder=folder, provider=provider,
                             tf_definitions=defs)
        if len(result.findings) > 0:
            all_findings.extend(result.findings)

    # loop through all findings and print them
    print("# " + "-" * 80)
    print(f"Findings in {folder}")

    for finding in all_findings:
        # if the severity is error, print the finding in red
        if finding.severity == "error":
            print(
                f"\033[91m - {finding.type} ({finding.provider} provider) '{finding.asset}'\033[0m")
