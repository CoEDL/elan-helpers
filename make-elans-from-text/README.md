Given a folder of `.txt` files containing annotations of audio in `.wav` files, create `.eaf` ELAN files.

Annotation start-time is 0 and end-time is duration of audio.  


```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python convert.py
```


Use optional `--copy_wavs` setting to copy WAV files into the out dir