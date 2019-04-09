# Elan Splitter

The script reads the Elan files and slice audio based on annotations on the first tier. You can choose other tiers by passing a tier name, or a different order number as an argument to the script. Note that the tier name or number has to be consistent across the data set.

## Installation
Open terminal and check what versions of python you have. 

brew --version
python --version
python3 --version

If you get a message "command not found: ..." then we need to install that software. 

Install homebrew if needed, following the instructions at https://brew.sh/

OSX comes with Python 2.7 but we need version 3. If you got a "command not found" error when you did the python3 --version command before, type this into Terminal.
`brew install python`


Put the script folder on the Desktop and put your Elan files and audio into the `Desktop/splitter/input` folder

In Terminal, change into the script folder ...
`cd ~/Desktop/splitter`

... and install the script's dependencies.
`pip3 install -r requirements.txt`

Then you are ready to run the script.
`python3 split_eafs.py`

The output folder should now be populated with clipped audio files and text annotations!


## Alternate usage

For example, to slice using annotations on a tier named "Words" you can use this command: 
`python3 split_eafs.py -t Words`

To get annotations from the second tier pass the number as an argument like this.. 
`python3 split_eafs.py -o 2`
