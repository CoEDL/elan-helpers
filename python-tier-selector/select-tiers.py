from PyInquirer import prompt
import glob
import os
from pympi.Elan import Eaf


# Return all files from a directory, that have matching extension
def find_files_by_ext(setOfAllFiles, exts):
    files = []
    for file in setOfAllFiles:
        name, ext = os.path.splitext(file)
        if ("*" + ext.lower()) in exts:
            files.append(file)
    return files


# Prompt user to select multiple tier names from a list of options
def select_tier(tier_names):
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
    extensions = ["*.eaf"]
    tier_names = set()
    all_files = set(glob.glob(os.path.join(input_dir, "**"), recursive=True))
    input_eafs = find_files_by_ext(all_files, set(extensions))
    # Compile tier info for the files in the input dir
    for input_eaf_path in input_eafs:
        input_eaf = Eaf(input_eaf_path)
        # Get the tier names — using pympi-ling
        file_tier_names = list(input_eaf.get_tier_names())
        # Compile tiers into set to use for user prompt
        for tier_name in file_tier_names:
            tier_names.add(tier_name)
    select_tier(tier_names)


if __name__ == '__main__':
    main()
