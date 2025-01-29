from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os
import requests
from bs4 import BeautifulSoup
import tempfile

app = Flask(__name__)

# Available voices (gTTS only supports languages, not specific voices)
VOICES = {
    "English (US)": "en",
    "English (UK)": "en-uk",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

@app.route("/text-to-speech", methods=["GET"])
def text_to_speech_form():
    return render_template("text_form.html", voices=VOICES)

@app.route("/webpage-to-speech", methods=["GET"])
def webpage_to_speech_form():
    return render_template("webpage_form.html", voices=VOICES)

@app.route("/generate-audio", methods=["POST"])
def generate_audio():
    text = request.form.get("text")
    language = request.form.get("voice", "en")

    if not text:
        return "Error: No text provided", 400

    tts = gTTS(text, lang=language)
    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_audio.name)
    
    return send_file(temp_audio.name, as_attachment=True, download_name="speech.mp3", mimetype="audio/mpeg")

@app.route("/generate-audio-from-url", methods=["POST"])
def generate_audio_from_url():
    url = request.form.get("url")
    language = request.form.get("voice", "en")

    if not url:
        return "Error: No URL provided", 400

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        text = " ".join([p.text for p in soup.find_all("p")])[:500]  # Limit text length
    except Exception as e:
        return f"Error fetching URL: {str(e)}", 500

    tts = gTTS(text, lang=language)
    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_audio.name)

    return send_file(temp_audio.name, as_attachment=True, download_name="speech.mp3", mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(debug=True)
