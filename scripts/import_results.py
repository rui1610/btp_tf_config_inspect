import re
from pathlib import Path
from typing import List
from libs.constants.files_folders import FOLDER_SCRIPTS
from libs.constants.variables import VARIABLES_MUST_EXIST
from libs.inspect import get_tf_definitions

# read all folders in the tfscripts folder

def get_folders() -> List[Path]:
    
    # Get all folders and subfolders in the FOLDER_SCRIPTS folder that contain at least one .tf file
    folders = [folder for folder in FOLDER_SCRIPTS.glob("**/*") if folder.is_dir() and any([re.match(r".*\.tf", file.name) for file in folder.iterdir()])]

    return folders

folders = get_folders()

# iterate through all folders
for folder in folders:
    # run the inspect_folder function
    tf_definitions = get_tf_definitions(folder)

    # iterate through all VARIABLES_MUST_EXIST
    for variable in VARIABLES_MUST_EXIST:
        # check if the variable is in the tf_definitions
        if variable not in tf_definitions:
            print(f"Variable {variable} is missing in folder {folder}")

