import os
import subprocess
from flask import Flask, render_template, request, send_file, abort

app = Flask(__name__)

# Define the directory where the Piper models are stored
MODEL_DIR = "piper_voices"
DATA_DIR = "/home/glick/Desktop/reader-app/piper_voices"
DOWNLOAD_DIR = "/home/glick/Desktop/reader-app/piper_voices"

# List all available Piper models
def get_available_models():
    models = [f.split(".onnx")[0] for f in os.listdir(MODEL_DIR) if f.endswith(".onnx")]
    return sorted(models)

# Get models for dropdown
available_models = get_available_models()

@app.route("/text-to-speech", methods=["GET"])
def text_to_speech_form():
    return render_template("text_form.html", voices=available_models)

@app.route("/webpage-to-speech", methods=["GET"])
def webpage_to_speech_form():
    return render_template("webpage_form.html", voices=available_models)

@app.route("/generate-audio", methods=["POST"])
def generate_audio():
    text = request.form.get("text")
    model_name = request.form.get("voice")

    if not text:
        return "Error: No text provided", 400
    if not model_name or model_name not in available_models:
        return "Error: Invalid model selected", 400

    model_path = model_name
    output_path = f"{DATA_DIR}/output.wav"

    # Run Piper TTS
    try:
        cmd = " ".join(["echo", f"'{text}'", "|", "piper", "--cuda", "--model", model_path, "--output_file", output_path, "--data-dir", DATA_DIR, "--download-dir", DOWNLOAD_DIR])
        #print("cmd: ", cmd)
        result = subprocess.run(
            ["echo", f"'{text}'", "|", "piper", "--cuda", "--model", model_path, "--output_file", output_path, "--data-dir", DATA_DIR, "--download-dir", DOWNLOAD_DIR],
            shell=True
        )
    except subprocess.CalledProcessError:
        return "Error: Failed to generate speech", 500

    return send_file(output_path, as_attachment=True, download_name="speech.wav", mimetype="audio/wav")

@app.route("/generate-audio-from-url", methods=["POST"])
def generate_audio_from_url():
    url = request.form.get("url")
    model_name = request.form.get("voice")

    if not url:
        return "Error: No URL provided", 400
    if not model_name or model_name not in available_models:
        return "Error: Invalid model selected", 400

    # Fetch webpage text
    try:
        import requests
        from bs4 import BeautifulSoup
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        text = " ".join([p.text for p in soup.find_all("p")])[:500]  # Limit text length
    except Exception as e:
        return f"Error fetching URL: {str(e)}", 500

    model_path = os.path.join(MODEL_DIR, model_name)
    output_path = "output.wav"

    # Run Piper TTS
    try:
        subprocess.run(
            ["piper", "--cuda", "--model", model_path, "--output_file", output_path, text],
            check=True,
        )
    except subprocess.CalledProcessError:
        return "Error: Failed to generate speech", 500

    return send_file(output_path, as_attachment=True, download_name="speech.wav", mimetype="audio/wav")

if __name__ == "__main__":
    app.run(debug=True)
