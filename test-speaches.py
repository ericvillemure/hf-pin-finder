import httpx
import os
from pathlib import Path
from openai import OpenAI
from analyzeTextFromMic import record_audio, save_as_wav
from pathlib import Path

from config import whisper_base_url

client = OpenAI(
    # This is the default and can be omitted
    api_key="unused",
    base_url=whisper_base_url
)

print("5, 1, 0, 1 est incorrect. Veuillez réessayer.")

audio_data = record_audio(duration=6)
audio_file = save_as_wav(audio_data)
print(audio_file)
response = client.audio.transcriptions.create(
    model="Systran/faster-whisper-small",
    response_format="verbose_json",
    file=Path(audio_file),
    language="fr",
)

print(response)