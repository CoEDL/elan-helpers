# Make ELANs from WAVs

This is a script to generate ELAN files matching a folder of WAVs. The WAV filenames are used to retrieve annotation value from a spreadsheet. If an audio filename isn't found in the spreadsheet, an ELAN file with blank annotation value will be created. 

## Requirements
The spreadsheet must contain at least one column named "File name" and one column named "Transcription". The spreadsheet can contain other columns.

Put your audio in the wav dir, put your spreadsheet in the input dir.

## Usage

Start a Python virtual environment.
```bash
python3 -m venv venv
source ./venv/bin/activate

```

Install the packages which the script needs
```bash
pip install argparse librosa pympi-ling pandas

```

Run the script 
```bash
python make-elan.py -a input/test.xlsx -s wav -t eaf 
```


When finished, deactivate the venv
```bash
deactivate
```