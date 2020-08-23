# Make ELANs from WAVs

Processing scripts to generate Elan files matching a nested folders of WAVs. The WAV filenames are used as the annotation value, and written forms of digits are converted to spoken forms. 

Written for the TIDIGITS corpus, so there are some specific naming manipulations in here that you won't need for your own data, including splitting filenames into individual characters. E.g., for file `123.wav` the script will create an Elan file `123.eaf` with annotation `one two three`.

Includes script to convert FLAC audio to WAV. 

This was written to convert the TIDIGITS corpus audio for Elpis-ready format.

To use it, drop your audio in the flac dir and run `flac2wav.py` to convert FLAC audio to WAV.

Then run the `make-elan.py` script to generate Elan files. 

If you want files to be in a single directory rather than nested, you can run `flatten.py`, which will move files into a single dir, renaming the files to incorporate the original dir structure in the filenames.
