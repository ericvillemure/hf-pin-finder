import numpy as np
import sounddevice as sd
import wave
import tempfile
from faster_whisper import WhisperModel

# Whisper Model Configuration
model_size = "large-v3"
model = WhisperModel(model_size, device="cpu", compute_type="int8")

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
    temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    print(temp_wav.name)
    with wave.open(temp_wav.name, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)  # 16-bit PCM
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())
    return temp_wav.name

def transcribe_audio(file_path):
    segments, info = model.transcribe(file_path, language='fr', beam_size=5)
    
    print(f"Detected language: {info.language} (probability {info.language_probability:.2f})\n")
    # for segment in segments:
    #     print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

# Main Execution
while True:
    audio_data = record_audio()
    audio_file = save_as_wav(audio_data, SAMPLE_RATE)
    transcribe_audio(audio_file)

