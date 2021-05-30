#!/usr/bin/python
import os
import librosa
from pympi.Elan import Eaf
from typing import List, Dict
import argparse


def get_annotation(input_dir: str, basename: str):
    """
    Get annotation from a the text file contents
    :param filename: Name of the file which contains an annotation
    :return: annotation text
    """
    annotation = ''
    with open(os.path.join(input_dir, basename + '.txt'), 'r', encoding='utf-8') as text_file:
        annotation = text_file.read()

    print('annotation', annotation)
    return annotation



def make_elans(input_dir: str, output_dir: str):
    """
    Make ELAN files based on filenames of WAV files and annotation from matching text file
    :param input_dir: Directory name of folder containing TXT and WAV audio files
    :param  output_dir: Directory name to save EAF files into
    """

    # Process each file
    print('Processing TXT and WAVs')
    for _, _, filenames in os.walk(input_dir):

        for filename in filenames:
            if '.wav' in filename:
                basename, ext = os.path.splitext(os.path.basename(filename))
                print("basename", basename)

                # Get audio file duration - use this as the EAF annotation's end timeslot
                duration = int(librosa.get_duration(filename=os.path.join(input_dir, filename))*1000)
                print("filename", filename)

                # Get annotation from the text file matching on file basename
                annotation = get_annotation(input_dir, basename)

                # Add any annotation cleaning here
                # annotation = re.sub(r"(\d+)", lambda x: num2words.num2words(int(x.group(0))), annotation)

                print(filename, duration, annotation)

                # Make EAF file
                output_eaf = Eaf()
                output_eaf.add_tier('tx')
                output_eaf.insert_annotation('tx', 0, duration, annotation)
                output_eaf.add_linked_file(os.path.join(output_dir, f'{basename}.wav'))
                output_eaf.to_file(os.path.join(output_dir, f'{basename}.eaf'))
    print('>>> Done')


def main():
    parser = argparse.ArgumentParser(description='Make ELAN files to match TXT and WAVs')
    parser.add_argument('-i', '--input_dir', help='Folder of TXT and WAV files', default='input')
    parser.add_argument('-o', '--output_dir', help='Folder to save EAFs', default='output')
    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir
    make_elans(input_dir, output_dir)


if __name__ == "__main__":
    main()
