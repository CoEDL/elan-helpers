from PyInquirer import prompt
import glob
import os
from pympi.Elan import Eaf
from typing import Set


# Return all files that have matching extension, from a specified directory
def find_files_by_ext(all_files: Set[str], extensions: Set[str]):
    files = []
    for file in all_files:
        name, ext = os.path.splitext(file)
        if ("*" + ext.lower()) in extensions:
            files.append(file)
    return files


# Prompt user to select multiple tier names from a list of options
def select_tier(tier_names: Set[str]):
    print(type(tier_names))
    tier_names_checkboxes = []
    for tier_name in list(tier_names):
        tier_names_checkboxes.append({'name': tier_name})
    questions = [
        {
            'type': 'checkbox',
            'name': 'tier',
            'message': 'Choose a tier',
            'choices': tier_names_checkboxes
        }
    ]
    tier_choice = prompt(questions)
    print("Selected tier/s:", tier_choice["tier"])


# Read files from a folder,
# Compile a list of tier names,
# Then ask user to choose one tier
def main():
    # Start by asking where the Elan files are
    # Default is a folder named "input" in the same directory as this script
    input_dir_question = [
        {
            'type': 'input',
            'name': 'input_dir',
            'message': 'Name of folder with Elan files?',
            'default': 'input'
        }
    ]
    input_dir_prompt = prompt(input_dir_question)
    input_dir = input_dir_prompt["input_dir"]
    # Get all files from the input directory
    extensions = set(["*.eaf"])
    tier_names = set()
    all_files = set(glob.glob(os.path.join(input_dir, "**"), recursive=True))
    input_files = find_files_by_ext(all_files, extensions)
    # Compile tier info for the files in the input dir
    for input_file_path in input_files:
        input_file = Eaf(input_file_path)
        # Get the tier names — using pympi-ling
        file_tier_names = list(input_file.get_tier_names())
        # Compile tiers into set to use for user prompt
        for tier_name in file_tier_names:
            tier_names.add(tier_name)
    print(type(tier_names))
    select_tier(tier_names)


if __name__ == '__main__':
    main()
