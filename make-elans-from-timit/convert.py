#!/usr/bin/python
import os
# import librosa
from pympi.Elan import Eaf
from typing import List, Dict
import argparse
import shutil
import glob


def make_elans(input_dir: str, output_dir: str, copy_wavs: bool):
    """
    Make ELAN files based on filenames of WAV files and annotation from matching text file
    :param input_dir: Directory name of folder containing TXT and WAV audio files
    :param  output_dir: Directory name to save EAF files into
    :param copy_wavs: Setting whether or not to copy the WAV file to the output dir
    """
    # Process each file
    files = glob.glob(f'{input_dir}/**/*.txt', recursive=True)
    print(files)

    for filename in files:

        filepath, ext = os.path.splitext(filename)
        basename = os.path.splitext(os.path.basename(filepath))[0]
        subdirname = os.path.basename(os.path.dirname(filepath))

        sex = subdirname[0]
        participant = subdirname[1:]

        # SEX :== m | f
        # SPEAKER_ID :== <INITIALS><DIGIT>
        # INITIALS :== speaker initials, 3 letters
        # DIGIT :== number 0-9 to differentiate speakers with identical initials

        # print(filename)     # input/dr1/fmem0/sa2.txt
        # print(filepath)     # input/dr1/fmem0/sa2
        # print(subdirname)   # fmem0
        # print(basename)     # sa2
        # print(ext)          # txt

        # Get audio file duration - use this as the EAF annotation's end timeslot
        # duration = int(librosa.get_duration(filename=os.path.join(input_dir, filename))*1000)

        # Get annotation from the text file matching on file basename
        with open(filename, 'r', encoding='utf-8') as text_file:
            annotation = text_file.read()
        annotation_split = annotation.split()
        start = int(annotation_split[0])
        duration = int(annotation_split[1])
        # convert audio samples to seconds to ms
        duration = int(duration/16000*1000)
        annotation_text = " ".join(annotation_split[2:])

        # Add any annotation cleaning here
        # annotation = re.sub(r"(\d+)", lambda x: num2words.num2words(int(x.group(0))), annotation)

        print(start, duration, annotation_text)

        # Make EAF file
        output_eaf = Eaf()
        output_eaf.add_tier('default', part=participant)
        output_eaf.add_annotation('default', start, duration, annotation_text)
        output_eaf.add_linked_file(os.path.join(output_dir, f'{subdirname}-{basename}.wav'))
        output_eaf.to_file(os.path.join(output_dir, f'{subdirname}-{basename}.eaf'))

        # Copy WAV?
        # if copy_wavs:
        shutil.copyfile(f'{filepath}.wav', os.path.join(output_dir, f'{subdirname}-{basename}.wav'))

    print('>>> Done')


def main():
    parser = argparse.ArgumentParser(description='Make ELAN files to match TXT and WAVs')
    parser.add_argument('-i', '--input_dir', help='Folder of TXT and WAV files', default='input')
    parser.add_argument('-o', '--output_dir', help='Folder to save EAFs', default='output')

    parser.add_argument('--copy_wavs', help='Copy WAV files to output dir', dest='copy_wavs', action='store_true')
    parser.add_argument('--no-copy_wavs', help='Copy WAV files to output dir', dest='copy_wavs', action='store_false')
    parser.set_defaults(copy_wavs=False)
    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir
    copy_wavs = args.copy_wavs

    if copy_wavs:
        print('copying WAVs')
    else:
        print('skip copying WAVs')

    # Reset the output dir
    print("resetting output dir")
    shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    # Go
    print("making elan files")
    make_elans(input_dir, output_dir, copy_wavs)


if __name__ == "__main__":
    main()
