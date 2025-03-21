import csv
import subprocess

NUMBER_OF_PINS = 5

with open('data/four-digit-pin-codes-sorted-by-frequency-withcount.csv', newline='') as csvfile:
    cr = csv.reader(csvfile, delimiter=',')
    my_list = list(cr)
    for row in my_list[:NUMBER_OF_PINS]:
        for index in range(4):
            subprocess.run(["ffplay", "-nodisp", "-autoexit", f"./data/digits/fr-CA/{row[0][index]}.mp3"])
