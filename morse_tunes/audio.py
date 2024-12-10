import numpy as np
from pydub import AudioSegment
import io

# Define Morse code sound parameters
DOT_DURATION = 200  # milliseconds
DASH_DURATION = DOT_DURATION * 3
FREQ = 350  # Hz
SAMPLE_RATE = 44100  # Hz (CD quality)

def generate_tone(frequency, duration_ms):
    """Generates a sine wave tone as a NumPy array."""
    duration_s = duration_ms / 1000  # Convert to seconds
    t = np.linspace(0, duration_s, int(SAMPLE_RATE * duration_s), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # Generate sine wave
    return (wave * 32767).astype(np.int16)  # Convert to 16-bit PCM

def morse_to_numpy(morse_code: str):
    """Generates a NumPy array from Morse code."""
    # Initialize an empty audio array
    audio_data = np.array([], dtype=np.int16)
    
    dot = generate_tone(FREQ, DOT_DURATION)
    dash = generate_tone(FREQ, DASH_DURATION)
    silence = np.zeros(int(SAMPLE_RATE * DOT_DURATION / 1000), dtype=np.int16)  # Silence between symbols
    word_gap = np.zeros(int(SAMPLE_RATE * DOT_DURATION / 1000 * 7), dtype=np.int16)  # Silence between words

    for symbol in morse_code:
        if symbol == '.':
            audio_data = np.concatenate((audio_data, dot, silence))
        elif symbol == '-':
            audio_data = np.concatenate((audio_data, dash, silence))
        elif symbol == '/':  # Space between words
            audio_data = np.concatenate((audio_data, word_gap))

    return audio_data
