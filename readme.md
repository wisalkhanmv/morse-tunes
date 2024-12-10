# morse-tunes

**MorseTunes** is a Python library and Gradio-based app that lets you convert text to Morse code and optionally play the Morse code as audio. Use it as a Python library, command-line tool, or through a web-based Gradio interface.

## Features

- **Text to Morse Code Conversion:** Converts any text into the equivalent Morse code.
- **Audio Playback:** Plays Morse code as audio tunes (dot and dash sounds).
- **Interactive Web App:** Use a Gradio interface for a user-friendly experience.
- **Simple to Use:** Works as a standalone Python library or through a Gradio app.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/wisalkhanmv/morsetunes.git
   cd morsetunes
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Gradio Web App

Run the Gradio app to interact with **MorseTunes** in your browser:

```bash
python main.py
```

Open the provided link in your browser (default is `http://127.0.0.1:7860`) to use the app. Enter text to convert it into Morse code and optionally play the audio.

### Python Code Integration

Use **MorseTunes** as a Python library in your projects.

#### Example: Convert Text to Morse Code

```python
from morse_tunes.morse import text_to_morse

text = "Hello World"
morse_code = text_to_morse(text)
print(f"Morse Code: {morse_code}")
```

#### Example: Play Morse Code as Audio

```python
from morse_tunes.audio import play_morse

morse_code = "... --- ..."
play_morse(morse_code)
```

### Command Line Tool

If you want a command-line interface, you can use the `main.py` file as a simple script:

```bash
python main.py
```

## How It Works

1. **Text Conversion:** The library converts each letter in your text to its Morse code equivalent using a predefined dictionary.
2. **Audio Playback:** The library generates sounds using `winsound` (Windows). Each dot (`.`) is a short beep, and each dash (`-`) is a longer beep.
3. **Gradio App:** The interactive interface uses the Gradio library to make it easy to use in a web browser.

## Development

Feel free to contribute! Clone the repository and make your changes.

```bash
git clone https://github.com/yourusername/morsetunes.git
cd morsetunes
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy coding and learning with MorseTunes!

```

```
