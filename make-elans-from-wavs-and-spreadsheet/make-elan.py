#!/usr/bin/python
import os
import librosa
from pympi.Elan import Eaf
from typing import List, Dict
import argparse
import pandas
import json


def get_annotations(spreadsheet: str):
    """
    Get filenames and annotations from a spreadsheet (actually loads all spreadsheet columns)
    :param spreadsheet: Name of the spreadsheet which contains rows of audio filenames and annotations
    :return: JSON format list of objects. Each object corresponds to a row of data in the excel file
    """
    spreadsheet_data = pandas.read_excel(spreadsheet)
    spreadsheet_json = spreadsheet_data.to_json(orient='records')
    annotations = json.loads(spreadsheet_json)
    print('Spreadsheet loaded')
    return annotations


def get_annotation(annotations: List[Dict[str, str]], filename: str):
    """
    Get annotation for an audio file by looking up filename match in the spreadsheet json
    :param annotations: data from input spreadsheet in JSON format
    :param filename: name of WAV file to get annotation for
    :return: annotation retrieved from the spreadsheet data matching the WAV filename
    """
    annotation = ''
    for record in annotations:
        if record["File name"] == filename:
            annotation = record["Transcription"]
            break
    return annotation


def make_elans(spreadsheet: str, source: str, target: str):
    """
    Make ELAN files based on filenames of WAV files
    :param spreadsheet: Path and file name of the spreadsheet containing WAV filenames and matching annotations
    :param source: Directory name of folder containing WAV audio files
    :param  target: Directory name to save EAF files into
    """

    # Read spreadsheet data and convert to JSON format
    print('Loading data from spreadsheet')
    annotations = get_annotations(spreadsheet)

    # Process each file
    print('Processing WAVs')
    for _, _, filenames in os.walk(source):

        for filename in filenames:
            if '.wav' in filename:
                basename, ext = os.path.splitext(os.path.basename(filename))

                # Get audio file duration - use this as the EAF annotation's end timeslot
                duration = int(librosa.get_duration(filename=os.path.join(source, filename))*1000)

                # Get annotation from the source data matching on filename
                annotation = get_annotation(annotations, filename)

                # Add any annotation cleaning here
                # annotation = re.sub(r"(\d+)", lambda x: num2words.num2words(int(x.group(0))), annotation)

                print(filename, duration, annotation)

                # Make EAF file
                output_eaf = Eaf()
                output_eaf.add_tier('tx')
                output_eaf.insert_annotation('tx', 0, duration, annotation)
                output_eaf.add_linked_file(os.path.join(target, f'{basename}.wav'))
                output_eaf.to_file(os.path.join(target, f'{basename}.eaf'))
    print('>>> Done')


def main():
    parser = argparse.ArgumentParser(description='make ELAN files to match WAVs')
    parser.add_argument('-a', '--annotations', help='spreadsheet name', default=os.path.join('input', 'test.xlsx'))
    parser.add_argument('-s', '--source', help='folder of WAVs', default='wav')
    parser.add_argument('-t', '--target', help='folder to save EAFs', default='eaf')
    args = parser.parse_args()

    spreadsheet = args.annotations
    source = args.source
    target = args.target
    make_elans(spreadsheet, source, target)


if __name__ == "__main__":
    main()
