from gtts import gTTS
import os

# Liste des chiffres avec leur écriture en français
chiffres = [
    ("0", "zéro"),
    ("1", "un"),
    ("2", "deux"),
    ("3", "trois"),
    ("4", "quatre"),
    ("5", "cinq"),
    ("6", "six"),
    ("7", "sept"),
    ("8", "huit"),
    ("9", "neuf")
]

folder = "data/digits/fr-CA"
os.makedirs(folder,exist_ok=True)

# Génération et sauvegarde des fichiers MP3
for digit, word in chiffres:
    tts = gTTS(text=word, lang='fr')
    filename = f"{folder}/{digit}.mp3"
    tts.save(filename)
    print(f"Fichier {filename} généré avec le mot '{word}'")