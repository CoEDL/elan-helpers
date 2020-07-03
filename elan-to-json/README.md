# Elan to JSON
The script reads an Elan file (or a directory including Elan files) and exports a JSON file with the annotations on a selected tier. You can choose which tier by passing a tier name, tier type, or a tier order number as an argument to the script. Note that the tier selection has to be consistent across the data set.

### Sample usage:

This will write a JSON file containing the annotations on the third tier (from the top) of all `.eaf` files in a folder named `transcriptions`. 

```
python3 elan_to_json.py -i transcriptions -r 3
```

### Sample output:

```
[
    {
        "audio_file_name": "abui_1.wav",
        "transcript": "amakaang di kaai hada muila",
        "start_ms": 290,
        "stop_ms": 1910,
        "speaker_id": "SL"
    },
    {
        "audio_file_name": "abui_2.wav",
        "transcript": "dining ayoku kamar mia mui muila",
        "start_ms": 890,
        "stop_ms": 2960,
        "speaker_id": "SL"
    },
    {
        "audio_file_name": "abui_3.wav",
        "transcript": "hekaai dining ayoku kamar mia muila",
        "start_ms": 1850,
        "stop_ms": 4140,
        "speaker_id": "SL"
    }
]
```
