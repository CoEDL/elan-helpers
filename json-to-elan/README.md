# JSON to ELAN

The script reads a JSON file (or folder) and generates an ELAN file to match.

## JSON format

It has been written for the JSON output from Huggingface ASR pipelines. Here's an example of the expected JSON format. 

```json
[
    {
        "text": "luanghan",
        "timestamp":
        [
            1.16,
            1.48
        ]
    },
    {
        "text": "ian",
        "timestamp":
        [
            1.56,
            1.7
        ]
    }.
]
```

## Setup 

Create a virtual environment and install the required packages.
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


Put your JSON files in the `input` directory, then run the script. The script will build an ELAN file with the annotations from the JSON file. It expects that your WAV files are named the same as the JSON basename (eg, if your JSON file is named `audio_1.json`, the ELAN file will end up with a linked media added for `audio_1.wav`). 
```
python convert.py
```

Optionally, you can specify a different input directory for the JSON files, and the output directory to write the ELAN files. If you have WAV files in the input directory, you can choose to copy them into the output too. You can also set a different tier name from the default (which is "default"). Here's an example:
```
python convert.py --tier_name Words --input source_files --output elan_files --copy_wavs 
```
