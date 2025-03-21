#After more thinking this step is not needed.  I can simply generate/download 10 .wav files with numbers and play them to generate a 4 digit PIN.  There is a problam with voices other than lessac that was not fixed

import csv
import wave
from piper.voice import PiperVoice
# https://github.com/rhasspy/piper/blob/master/VOICES.md
model = "data/voices/en_US-lessac-medium.onnx"
voice = PiperVoice.load(model)

NUMBER_OF_PINS = 10

with open('data/four-digit-pin-codes-sorted-by-frequency-withcount.csv', newline='') as csvfile:
    cr = csv.reader(csvfile, delimiter=',')
    my_list = list(cr)
    for row in my_list[:NUMBER_OF_PINS]:
        text = ' '.join(row[0])
        #https://github.com/rhasspy/piper?tab=readme-ov-file
        wav_file = wave.open(f"./data/synthesized-pins/{row[0]}.wav", "w")
        audio = voice.synthesize(text, wav_file)


