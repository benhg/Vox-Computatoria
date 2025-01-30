import os
import subprocess
import requests
import browser_cookie3
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, send_file, abort

app = Flask(__name__)

# Define the directory where the Piper models are stored
MODEL_DIR = "piper_voices"
DATA_DIR = "/home/glick/Desktop/reader-app/piper_voices"
DOWNLOAD_DIR = "/home/glick/Desktop/reader-app/piper_voices"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}


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

def text_to_speech(text, model_name):
    model_path = model_name
    output_path = f"{DATA_DIR}/output.wav"

    if not text:
        return "Error: No text provided", 400
    if not model_name or model_name not in available_models:
        return "Error: Invalid model selected", 400

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
    return output_path

@app.route("/generate-audio-from-article", methods=["POST"])
def generate_audio_from_article():
    url = request.form.get("url")
    model_name = request.form.get("voice")

    if not url:
        return "Error: No URL provided", 400

    text = fetch_article(url)

    print(text)

    output_path = text_to_speech(text)
    if "Error" in output_path:
        return output_path

    return send_file(output_path, as_attachment=True, download_name="speech.wav", mimetype="audio/wav")



def get_chrome_cookies():
    return {cookie.name: cookie.value for cookie in browser_cookie3.chrome(domain_name="newyorker.com")}


def fetch_article(url):
    session = requests.Session()
    session.cookies.update(get_chrome_cookies())
    session.headers.update(HEADERS)

    response = session.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.select("p")  # Adjust as needed
        text = "\n".join(p.get_text() for p in paragraphs)
        return text
    else:
        print(f"Error: {response.status_code}")
        return None


@app.route("/generate-audio", methods=["POST"])
def generate_audio():
    text = request.form.get("text")
    model_name = request.form.get("voice")

    output_path = text_to_speech(text, model_name)
    if "Error" in output_path:
        return output_path

    return send_file(output_path, as_attachment=True, download_name="speech.wav", mimetype="audio/wav")

@app.route("/generate-audio-from-url", methods=["POST"])
def generate_audio_from_url():
    url = request.form.get("url")
    model_name = request.form.get("voice")

    if not url:
        return "Error: No URL provided", 400

    # Fetch webpage text
    try:
        import requests
        from bs4 import BeautifulSoup
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        text = " ".join([p.text for p in soup.find_all("p")])[:500]  # Limit text length
    except Exception as e:
        return f"Error fetching URL: {str(e)}", 500

    output_path = text_to_speech(text)
    if "Error" in output_path:
        return output_path

    return send_file(output_path, as_attachment=True, download_name="speech.wav", mimetype="audio/wav")

if __name__ == "__main__":
    app.run(debug=True)
