import numpy as np
import sounddevice as sd
import wave
import tempfile
from faster_whisper import WhisperModel
import time

# Whisper Model Configuration
model_size = "turbo" # "large-v3" "large-v2"
device = "cuda"
compute_type = "float16"
print(f'model_size={model_size} Device={device} compute_type={compute_type}')
model = WhisperModel(model_size, device=device, compute_type=compute_type)

# Audio Recording Parameters
SAMPLE_RATE = 16000  # Whisper expects 16kHz audio
CHANNELS = 1
DURATION = 5  # Record for 5 seconds

def record_audio(duration=DURATION, sample_rate=SAMPLE_RATE):
    print("Recording... Speak now!")
    
    # Record audio from the microphone
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=CHANNELS, dtype=np.int16)
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")
    
    return audio_data

def save_as_wav(audio_data, sample_rate):
    # temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    # print(temp_wav.name)
    file_name = "eric.wav"
    with wave.open(file_name, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)  # 16-bit PCM
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())
    return file_name

def transcribe_audio(file_path):
    print(f"Transcribing file: {file_path}\n")
    segments, info = model.transcribe(file_path, language='fr', beam_size=5)
    for segment in segments:
        print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

# Main Execution
# while True:
#     audio_data = record_audio()
#     audio_file = save_as_wav(audio_data, SAMPLE_RATE)
#     transcribe_audio(audio_file)

# audio_data = record_audio()
# audio_file = save_as_wav(audio_data, SAMPLE_RATE)
start = time.time()
transcribe_audio('eric.wav')
print(time.time() - start)
start = time.time()
transcribe_audio('eric.wav')
print(time.time() - start)

