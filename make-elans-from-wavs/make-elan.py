import os
import librosa
import re
import num2words
from pympi.Elan import Eaf


def make_elan(source_parent_dir, target_parent_dir):
    """
    Make elan files based on filenames of wav files
    Written for the TIDIGITS corpus, so some things are specific to the name formats of that corpus
    """

    for dirname, dirnames, filenames in os.walk(source_parent_dir):

        # print path to all subdirectories first.
        for subdirname in dirnames:
            print(os.path.join(dirname, subdirname))

        # print path to all filenames.
        for filename in filenames:
            if '.wav' in filename:
                parent, gender, child = dirname.split(os.path.sep)
                basename, ext = os.path.splitext(os.path.basename(filename))
                print(parent, gender, child, filename)

                source_path = os.path.join(source_parent_dir, gender, child)
                target_path = os.path.join(target_parent_dir, gender, child)

                if not os.path.exists(target_path):
                    print(target_path)
                    os.makedirs(target_path)

                # Audio file duration - use this as end timeslot
                duration = int(librosa.get_duration(filename=os.path.join(source_path, filename))*1000)

                # Make file annotation from filename (minus the suffix)
                annotation = " ".join([char for char in basename[:-1]])
                # These are specific to the TIDIGITS naming convention
                annotation = annotation.replace("o", "oh")
                annotation = annotation.replace("z", "zero")

                text = re.sub(r"(\d+)", lambda x: num2words.num2words(int(x.group(0))), annotation)

                print(filename, duration, annotation, text)

                # Make elan
                output_eaf = Eaf()
                output_eaf.add_tier('tx')
                output_eaf.insert_annotation('tx', 0, duration, text)
                output_eaf.add_linked_file(os.path.join(target_path, f'{basename}.wav'))

                output_eaf.to_file(os.path.join(target_path, f'{basename}.eaf'))


if __name__ == "__main__":
    source_parent_dir = 'wav'
    target_parent_dir = 'wav'
    make_elan(source_parent_dir, target_parent_dir)
