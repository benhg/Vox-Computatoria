# Vox Computatoria

A Flask-based web application that converts text and web articles into speech using Piper TTS. This app supports local, GPU-accelerated speech synthesis and allows users to generate spoken audio from manual input or website content.

## Features
- Convert text to speech using high-quality Piper TTS models.
- Extract and convert articles from web pages into speech.
- Supports CUDA acceleration for faster synthesis (if available).
- Uses browser cookies to bypass paywalls on certain sites (e.g., The New Yorker).
- Supports multiple voices/models for customization.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/benhg/reader-app.git
cd reader-app
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Download Piper Models
You'll need Piper TTS models to generate speech. Run:
```bash
bash download_piper_models.sh
bash download_piper_configs.sh
```

This will download English (US/UK) models into piper_voices/.

## Usage

### Run the Flask Server
```bash
python app.py
```
The app will be available at:

http://127.0.0.1:5000/

Deploy this app however you want. It's a Flask app. For example, here is a systemd file you may want to use:

```
[Unit]
Description=Reader App (Flask + Piper)
After=network.target

[Service]
User=glick
WorkingDirectory=/home/glick/Desktop/reader-app/src
ExecStart=/home/glick/Desktop/reader/bin/gunicorn -w 2 -b 0.0.0.0:5123 app:app
ExecStop=/bin/kill -TERM $MAINPID
Restart=always
PIDFile=/run/reader-app.pid
KillMode=mixed
TimeoutStopSec=5


[Install]
WantedBy=multi-user.target
```


### Text-to-Speech

Open http://127.0.0.1:5000/text-to-speech

Enter text, select a voice, and submit.

Download the generated speech as a .wav file.

Webpage-to-Speech

Open http://127.0.0.1:5000/webpage-to-speech

Enter a URL, select a voice, and submit.

The webpage text will be extracted and converted into speech.

### API Endpoints

POST /generate-audio

Input: text, voice
Output: .wav file

POST /generate-audio-from-url

Input: url, voice
Output: .wav file

POST /generate-audio-from-article

Input: url, voice
Output: .wav file

(Uses browser cookies to fetch full articles)

Configuration
1. Changing the Piper Model Directory
By default, the app looks for models in:
```
MODEL_DIR = "piper_voices"
```

To change this, update MODEL_DIR in config.py.

Other configuration options such as browser, supported domains, etc. are also in config.py

2. Using GPU Acceleration

Piper supports CUDA for faster processing. The app automatically uses GPU if available.

3. Customizing Headers & Cookies

The app mimics a real browser to fetch articles:

```python
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
```
It also uses browser cookies via browser_cookie3 to access sites like The New Yorker.

Troubleshooting
1. Piper Not Found?
Make sure piper is installed and accessible: `which piper`
If missing, install it from Piper [GitHub](https://github.com/piper-tts).

2. Output File Not Found?

If output.wav isn't being generated, check:

- File paths (piper_voices/output.wav).
- Run piper manually to confirm it's working: `piper --model piper_voices/en_US-amy-medium.onnx --output_file output.wav --text "Hello world"`

3. Debugging Issues?
Run Flask with debugging enabled:
```
python app.py
Check the console for errors.
```

# Responsible Use – Don't Be That Person

This application is meant for personal use only by individuals who have actually paid for subscriptions to the content they are accessing. If you don’t have a subscription, you shouldn’t be using this tool to get around paywalls—end of story.

Under no circumstances should you deploy this publicly where others could use your subscription to access paywalled content. Doing so effectively hands out your paid access for free, which isn’t just unfair to you—it’s essentially stealing from the publication. Newsrooms and writers rely on subscriptions to stay afloat, and circumventing that system by sharing access is not only ethically questionable but could also violate the publication’s terms of service.

If you intend to use this for personal reading, keep it private. Don’t expose it to the public internet, don’t let others piggyback off your subscription, and don’t pretend you didn’t know better.

# Contributing

Pull requests are welcome! Please open an issue first if you'd like to discuss substantial changes.
