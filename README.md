# Elan Helpers

Tools and scripts for working with ELAN. See the README file in each script folder for usage instuctions.

## Elan Character Spacer

This script will space-separate characters in all words in specified Elan tiers.


## Elan to JSON

The script reads an Elan file (or a directory including Elan files) and exports a JSON file with the annotations on a selected tier. You can choose which tier by passing a tier name, tier type, or a tier order number as an argument to the script.


## Elan Splitter

The script processes a directory of audio annotated in Elan, and outputs audio clips and matching-named text files containing the respective annotations. The original files are not altered. Audio clips are determined by the start and end times of annotations on the first tier. You can choose to use another tier by passing a tier name or a different order number (not tier type) as an argument to the script.

## Python Tier Selector

This script doesn't do much on its own, but can be used as a basis for your own processing script. It looks in a folder the user specifies, and compiles a list of all the tiers in the Elan files in that folder. The script offers the user an option to select one or more tiers from the list. From this point you could extend the script to extract all the annotations on the selected tiers, or perhaps write a new Elan file that combines the selected tiers.
