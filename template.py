import os
from pathlib import Path
import logging

# Configure logging to display info level messages with a specific format
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the project name
project_name = 'wine_quality_prediction_project'

# List of files and directories to be created for the project
list_of_files = [
    f"src/{project_name}/__init__.py", # constructor file
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html", # for flask app
]

# Iterate over the list of files
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert the file path to a Path object
    filedir, filename = os.path.split(filepath)  # Split the path into directory and file name

    # If the directory part is not empty, create the directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create the directory if it doesn't exist
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # If the file does not exist or is empty, create an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")