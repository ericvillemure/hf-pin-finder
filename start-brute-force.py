import os.path
import urllib.request
import csv
import subprocess
import time
from playsound import playsound
from analyzeTextFromMic import record_audio, save_as_wav, transcribe_audio
import json
import datetime

csv_file = "data/four-digit-pin-codes-sorted-by-frequency-withcount.csv"
csv_url = "https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/four-digit-pin-codes-sorted-by-frequency-withcount.csv"
rpi_base_url = "http://raspberrypi.local:8000"
results_file = "data/results.json"

import pygame

pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)

if (not os.path.exists(csv_file)):
    print('Downloading csv file')
    urllib.request.urlretrieve(csv_url, csv_file)

if (os.path.exists(results_file)):
    print('Opening results.json file')
    results = json.load(open(results_file))

else:
    results = {}

def clickLeft():
    print("clickLeft")
    url = f'{rpi_base_url}/servo/left-click'
    req = urllib.request.Request(url=url, method='PUT')
    with urllib.request.urlopen(req) as f:
        pass

def clickRight():
    print("clickRight")
    url = f'{rpi_base_url}/servo/right-click'
    req = urllib.request.Request(url=url, method='PUT')
    attempts = 0

    while attempts < 5:
        try:
            urllib.request.urlopen(req, timeout=3)
            break
        except:
            attempts += 1

def micToText(seconds):
    audio_data = record_audio(duration=seconds)
    audio_file = save_as_wav(audio_data)
    print(audio_file)
    # audio_file = "C:\\Users\\ERIC~1.VIL\\Downloads\\locked.mp3" if seconds == 5 else "C:\\Users\\ERIC~1.VIL\\Downloads\\wrong.mp3"
    return transcribe_audio(audio_file), audio_file

retries = 0

with open(csv_file, newline='') as csvfile:
    cr = csv.reader(csvfile, delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print(f"Working on PIN {row[0]} {datetime.datetime.now()}")
        if (row[0] in results):
            print(f"Skipping {row[0]}")
            continue

        if (retries == 0):
            clickRight()
            (text,_) = micToText(5)
            print(text)
            if ("Le système est verrouillé" not in text):
                raise Exception("System should be locked")

        clickRight()
        time.sleep(0.2)
        for index in range(4):
            # too slow subprocess.run(["C:\\Users\\eric.villemure\\Downloads\\ffmpeg-master-latest-win64-gpl-shared\\bin\\ffplay", "-nodisp", "-autoexit", f"./data/digits/fr-CA/{row[0][index]}.mp3"])
            pygame.mixer.music.load(f"./data/digits/fr-CA/{row[0][index]}.mp3")
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy() == True:
                pass
        (text, audio_file) = micToText(8)
        results[row[0]] = {
            "PIN": row[0],
            "popularity": row[1],
            "retries": retries,
            "response": text,
            "audio": audio_file,
            "date": f'{datetime.datetime.now()}'
        }
        json.dump(results, open(results_file, 'w'))

        print(f'"{text}"')
        #On the third retry the PIN is not said outloud but a sound is played instead so we are expecting text == '' when failed or something else when PIN found
        #Otherwise check if the spelled out number is the same as the one that was played aka row[0]
        if ((retries == 2 and text != '') or 
            (retries != 2 and "est incorrect" not in text and "est incorrigible" not in text)):
            print(f"Password found {row[0]}")
            exit()
        elif (retries == 2):
            retries = 0 #starting over
        else:
            retries = retries + 1
