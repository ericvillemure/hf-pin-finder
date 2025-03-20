/data Folder description

/data/voices This folder contains piper voices used by this project.  I am currently using gilles (https://github.com/rhasspy/piper?tab=readme-ov-file#voices) we need both the .onnx and .onnx.json files
/data/synthesized-pins/ contains the pins generated .wav files (from 0000.wav to 9999.wav).  Depending on how the code is changed only a subset of all possible PINs could be generated
/data/four-digit-pin-codes-sorted-by-frequency-withcount.csv This is the file found at https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/four-digit-pin-codes-sorted-by-frequency-withcount.csv and it containe all PINS by popularity.  This is used to optimize hos fast we can find a PIN because we check the most popular first

scripts

create-synthesized-pins.py this will generate the files in /data/synthesized-pins/ change the value of NUMBER_OF_PINS to generate more PINS when everything have been tested