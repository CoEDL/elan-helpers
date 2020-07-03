#!/usr/bin/python3
import xml.etree.ElementTree as ET
import glob
import os
from pathlib import Path


def spaceMe(file_):
    print(file_)
    # Which tier?
    tier_name = 'Phrase'
    tree = ET.parse(file_)

    root = tree.getroot()

    for tier in root.iter('TIER'):
        if tier.attrib['TIER_ID'] == tier_name:
            for annotation in tier.iter('ANNOTATION_VALUE'):
                # Get the original text
                # OPTION: use this to not end up with double spaces between words
                source_text = annotation.text.replace(" ", "")
                # OR: use this to have double spaces between words
                # source_text = annotation.text

                insert_spaces = " ".join(source_text)

                # update the annotation
                annotation.text = str(insert_spaces)

                # feedback
                print("done")

    # Save the file to output dir
    tree.write(os.path.join("output", os.path.basename(file_)))

def main():
    for path in Path('./input').rglob('*.eaf'):
        spaceMe(path)

if __name__ == "__main__":
    main()
