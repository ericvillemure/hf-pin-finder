import httpx
import os
from pathlib import Path
from openai import OpenAI
from analyzeTextFromMic import record_audio, save_as_wav, transcribe_audio
import wave

whisper_base_url = "http://ABSORB-DLFT044:8000/v1"

client = OpenAI(
    # This is the default and can be omitted
    api_key="unused",
    base_url=whisper_base_url
)


# filename = 'C:\\Users\\ERIC~1.VIL\\AppData\\Local\\Temp\\tmp1f90fdm1.wav'
# with Path(filename).open("rb") as audio_file:
#     response = client.audio.transcriptions.create(
#         model="Systran/faster-whisper-small",
#         file=audio_file,
#         language="fr",
#         prompt="Tu es un systeme de reconaissance vocale qui analyse les message audio provenant d'un systaime de telephone main-libre sur un vehicule."
#     )

#     print(response.text)

print("5, 1, 0, 1 est incorrect. Veuillez réessayer.")

audio_data = record_audio(duration=6)
audio_file = save_as_wav(audio_data)
print(audio_file)

with Path(audio_file).open("rb") as audio_file:
    response = client.audio.transcriptions.create(
        model="Systran/faster-whisper-small",
        response_format="verbose_json",
        file=audio_file,
        language="fr",
        prompt="Tu es un systeme de reconaissance vocale qui analyse les message audio provenant d'un systeme de telephone main-libre sur un vehicule."
    )

    print(response)

