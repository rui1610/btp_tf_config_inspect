import re
from pathlib import Path
from typing import List
from libs.constants.files_folders import FOLDER_SCRIPTS
from libs.inspect import get_tf_definitions
from libs.inspection.provider import TF_Provider
from libs.io.files import write_string_to_file


# read all folders in the tfscripts folder
def get_folders() -> List[Path]:
    """
    Get all folders and subfolders in the FOLDER_SCRIPTS folder that contain at least one .tf file.

    Returns:
        List[Path]: A list of Path objects representing the folders that contain .tf files.
    """
    folders = [folder for folder in FOLDER_SCRIPTS.glob("**/*") if folder.is_dir(
    ) and any([re.match(r".*\.tf", file.name) for file in folder.iterdir()])]

    return folders


# get all folders
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
    message_text = "# " + "-" * 80 + "\n"
    message_text += f"Findings in {folder}\n"

    for finding in all_findings:
        # if the severity is error, print the finding in red
        if finding.severity == "error":
            message_text += f"\033[91m - {finding.type} ({finding.provider} provider) '{finding.asset}'\033[0m\n"
            print(message_text)
            filename = Path(folder, "TF_compliance_TODO.txt")
            write_string_to_file(string_data=message_text, file_path=folder)
