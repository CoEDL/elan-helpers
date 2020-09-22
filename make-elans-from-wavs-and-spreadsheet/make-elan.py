import os
import librosa
import re
import num2words
from pympi.Elan import Eaf
import argparse
import pandas
import json
# import excel2json


def prepare_input_file(spreadsheet):
    spreadsheet_data = pandas.read_excel(spreadsheet)
    spreadsheet_not_really_json = spreadsheet_data.to_json(orient='records')
    # excel2json generates a JSON file. Maybe handy instead of pandas?
    # spreadsheet_data = excel2json.convert_from_file(spreadsheet)
    return json.loads(spreadsheet_not_really_json)


def get_annotation_from_spreadsheet(spreadsheet_json, filename):
    annotation = ''
    for record in spreadsheet_json:
        if record["File name"] == filename:
            annotation = record["Transcription"]
            break
    return annotation


def main():
    """
    Make elan files based on filenames of wav files
    """
    parser = argparse.ArgumentParser(description='make .eaf to match .wav and spreadsheet with transcriptions')
    parser.add_argument('-a', '--annotations', help='spreadsheet name', default=os.path.join('input', 'test.xlsx'))
    parser.add_argument('-s', '--source', help='folder of wavs', default='wav')
    parser.add_argument('-t', '--target', help='folder to save eafs', default='eaf')
    args = parser.parse_args()

    # Read spreadsheet data and convert to JSON format
    spreadsheet_json = prepare_input_file(args.annotations)

    # Set paths for input and output
    source_path = args.source
    target_path = args.target

    # Process each file
    for _, _, filenames in os.walk(source_path):

        for filename in filenames:
            if '.wav' in filename:
                basename, ext = os.path.splitext(os.path.basename(filename))

                # Audio file duration - use this as end time slot
                duration = int(librosa.get_duration(filename=os.path.join(source_path, filename))*1000)

                # Make file annotation from filename (minus the suffix)
                annotation = get_annotation_from_spreadsheet(spreadsheet_json, filename)

                # text = re.sub(r"(\d+)", lambda x: num2words.num2words(int(x.group(0))), annotation)

                print(filename, duration, annotation)

                # Make elan
                output_eaf = Eaf()
                output_eaf.add_tier('tx')
                output_eaf.insert_annotation('tx', 0, duration, annotation)
                output_eaf.add_linked_file(os.path.join(target_path, f'{basename}.wav'))
                output_eaf.to_file(os.path.join(target_path, f'{basename}.eaf'))


if __name__ == "__main__":
    main()
