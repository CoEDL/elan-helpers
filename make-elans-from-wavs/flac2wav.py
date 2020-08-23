import os


def flac2wav(source_parent_dir, target_parent_dir):
    """
    Convert flac audio to wav
    """

    for dirname, dirnames, filenames in os.walk(source_parent_dir):

        # print path to all subdirectories first.
        for subdirname in dirnames:
            print(os.path.join(dirname, subdirname))

        # print path to all filenames.
        for filename in filenames:
            if '.flac' in filename:
                print(filename)
                parent, gender, child = dirname.split(os.path.sep)
                basename, ext = os.path.splitext(os.path.basename(filename))
                print(parent, gender, child, filename)

                source_path = os.path.join(source_parent_dir, gender, child)
                target_path = os.path.join(target_parent_dir, gender, child)

                if not os.path.exists(target_path):
                    os.makedirs(target_path)

                os.system(f'ffmpeg -hide_banner -loglevel warning -y -i {source_path}/{filename} {target_path}/{basename}.wav')


if __name__ == "__main__":
    source_parent_dir = 'flac'
    target_parent_dir = 'wav'
    flac2wav(source_parent_dir, target_parent_dir)
