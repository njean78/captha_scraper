#!/usr/bin/env python
from os import environ, path

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
#C:\CARIGE\Projects\captha_scraper\it-IT\pocketsphinx-data\it-IT
MODELDIR = "C:/Users/NJean/Miniconda3/envs/deeplearning/lib/site-packages/pocketsphinx/model"
DATADIR = "C:/Users/NJean/Miniconda3/envs/deeplearning/lib/site-packages/pocketsphinx/data"

# Create a decoder with certain model

def main():

    config = Decoder.default_config()
    config.set_string('-hmm', path.join(MODELDIR, 'en-us'))
    config.set_string('-lm', path.join(MODELDIR, 'en-us.lm.bin'))
    config.set_string('-dict', path.join(MODELDIR, 'cmudict-en-us.dict'))
    decoder = Decoder(config)

    # Decode streaming data.
    decoder = Decoder(config)
    decoder.start_utt()
    stream = open(path.join(DATADIR, 'goforward.raw'), 'rb')
    while True:
        buf = stream.read(1024)
        if buf:
            decoder.process_raw(buf, False, False)
        else:
            break
    decoder.end_utt()
    print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])

if __name__ == "__main__":
    main()
