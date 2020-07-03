# Elan Splitter

The script processes a directory of audio annotated in Elan, and outputs audio clips and matching-named text files containing the respective annotations. The original files are not altered. Audio clips are determined by the start and end times of annotations on the first tier. You can choose to use another tier by passing a tier name or a different order number as an argument to the script (see below for examples). Note that the tier name or number has to be consistent across the data set, it doesn't enable individual files to be handled differently.

Instructions here are for Mac OSX.

## Installation

Open Terminal and check what versions of Homebrew and Python you have (if any). If you get a message "command not found: ..." then we need to install that software.

```
brew --version
python --version
python3 --version
```

**Homebrew**
Install Homebrew if needed, following the instructions at https://brew.sh/

**Python**
OSX comes with Python 2.7 but we need version 3. If you got a "command not found" error when you did the python3 --version command before, type this into Terminal. <br />
`brew install python`

If you want to output mp3 files, also install ffmpeg <br />
`brew install ffmpeg`


**Splitter**

Clone this repository to the Desktop and cd into it. In Terminal:
```
cd ~/Desktop
git clone https://github.com/CoEDL/elan-splitter.git
cd elan-splitter
```

... and install the script's dependencies. <br />
`pip3 install -r requirements.txt`

Put your Elan and audio files into the `~/Desktop/elan-splitter/input` folder.


## Usage

Then you are ready to run the script. <br />
`python3 split_eafs.py`

The output folder should now be populated with clipped audio files and text annotations!



By the way, if you are using WAV audio, and don't have ffmpeg installed, you can ignore the error about RuntimeWarning: Couldn't find ffmpeg or avconv. They would be needed if converting to mp3 or some other audio formats, WAV format is handled by the Python library.


## Options

To slice using annotations on a tier named "Words" you can use this command: <br />
`python3 split_eafs.py -t Words`

To get annotations from the second tier pass the number as an argument like this: <br />
`python3 split_eafs.py -o 2`

If you want the files it generates to be named with the annotation name, run the script with -n flag. <br />
`python3 split_eafs.py -n`

Add a prefix to the generated files with `-p` setting. The following command, used with an Elan file that has the transcription "dog" will result in generated files named `A111_dog.txt` and `A111_dog.wav`. <br />
`python3 split_eafs.py -n -p "A111"`

To output audio in MP3 format, set the format type with -f flag. The default output format is WAV. <br />
`python3 split_eafs.py -f mp3`

You can combine options! E.g., to get annotations from the second highest tier, write files with annotations as the name, with A111 prefix: <br />
`python3 split_eafs.py -o 2 -n -p "A111"`
