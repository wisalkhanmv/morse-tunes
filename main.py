import gradio as gr
from scipy.io.wavfile import write
from morse_tunes.morse import text_to_morse
from morse_tunes.audio import morse_to_numpy
import numpy as np

def convert_and_generate_audio(text):
    """Converts text to Morse code and generates a NumPy audio array."""
    morse_code = text_to_morse(text)
    audio_data = morse_to_numpy(morse_code)
    return morse_code, (44100, audio_data)

# Define the Gradio interface
interface = gr.Interface(
    fn=convert_and_generate_audio,
    inputs=gr.Textbox(label="Input Text", placeholder="Enter text to convert to Morse code"),
    outputs=[
        gr.Textbox(label="Morse Code"),
        gr.Audio(label="Morse Code Audio", type="numpy"),
    ],
    title="MorseTunes",
    description="Convert text to Morse code and generate audio that can be played in the browser.",
)

# Launch the Gradio app
if __name__ == "__main__":
    interface.launch()
