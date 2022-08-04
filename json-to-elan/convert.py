import os
from pympi.Elan import Eaf
from typing import List, Dict
import argparse
import shutil
import json
from pathlib import Path


def make_elans(tier_name: str, input_dir: str, output_dir: str, copy_wavs: bool):
    """
    Make ELAN files based on JSON data
    :param tier_name: The name of the tier to write into
    :param input_dir: Directory name of folder containing JSON (and optionally also matching WAV audio) files
    :param output_dir: Directory name to save EAF files into
    :param copy_wavs: Setting whether or not to copy the WAV file to the output dir
    """
    # Process each file
    for _, _, filenames in os.walk(input_dir):

        for filename in filenames:
            if '.json' in filename:
                print(filename)
                basename, ext = os.path.splitext(os.path.basename(filename))

                file_path = Path(input_dir, filename)
                # read the JSON
                with open(file_path) as json_file:
                    annotation_data = json.load(json_file)
                    print(annotation_data)

                # Make EAF file
                output_eaf = Eaf()
                for annotation in annotation_data:
                    start = int(annotation["timestamp"][0] * 1000)
                    end = int(annotation["timestamp"][1] * 1000)
                    print(end, start)
                    output_eaf.add_annotation("default", start, end, value=annotation["text"])

                if tier_name != "default":
                    output_eaf.rename_tier("default", tier_name)
                output_eaf.add_linked_file(str(Path(output_dir, f'{basename}.wav')))
                output_eaf.to_file(str(Path(output_dir, f'{basename}.eaf')))

                # Copy WAV?
                if copy_wavs:
                    shutil.copyfile(Path(input_dir, f"{basename}.wav"), Path(output_dir, f"{basename}.wav"))


def main():
    parser = argparse.ArgumentParser(description='Make ELAN files from JSON data')
    parser.add_argument('-t', '--tier_name', help='Name of the tier', default='default')
    parser.add_argument('-i', '--input_dir', help='Folder of JSON files', default='input')
    parser.add_argument('-o', '--output_dir', help='Folder to save EAFs', default='output')
    parser.add_argument('--copy_wavs', help='Copy WAV files to output dir', dest='copy_wavs', action='store_true')
    parser.add_argument('--no-copy_wavs', help='Copy WAV files to output dir', dest='copy_wavs', action='store_false')
    parser.set_defaults(copy_wavs=False)

    args = parser.parse_args()
    tier_name = args.tier_name
    input_dir = args.input_dir
    output_dir = args.output_dir
    copy_wavs = args.copy_wavs

    # Reset the output dir
    print("resetting output dir")
    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    # Go
    print("making elan files")
    make_elans(tier_name, input_dir, output_dir, copy_wavs)


if __name__ == "__main__":
    main()
