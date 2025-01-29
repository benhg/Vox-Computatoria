# reader-app
A web app that reads things out loud for me 


## Requirements:
- CUDA12
- CUDNN9
- Piper-tts python package and C deps


## Voice Structures

I am not going to upload all the voices to GitHub, because I think redistributing them would violate the license. But I will show my directory structure so that you can set yours up to match mine

```
.
├── app.py
├── data
├── Desktop
│└── reader
│    └── voices
│        ├── en_US-lessac-medium.onnx
│        └── en_US-lessac-medium.onnx.json
├── piper_voices
│├── dioco-medium.onnx.json
│├── download_models.sh
│├── download_piper_configs.sh
│├── download_piper_models.sh
│├── en_GB-alan-low.onnx
│├── en_GB-alan-low.onnx.json
│├── en_GB-alan-medium.onnx
│├── en_GB-alan-medium.onnx.json
│├── en_GB-alba-medium.onnx
│├── en_GB-alba-medium.onnx.json
│├── en_GB-aru-medium.onnx
│├── en_GB-aru-medium.onnx.json
│├── en_GB-cori-high.onnx
│├── en_GB-cori-high.onnx.json
│├── en_GB-cori-medium.onnx
│├── en_GB-cori-medium.onnx.json
│├── en_GB-jenny_dioco-medium.onnx
│├── en_GB-jenny_dioco-medium.onnx.json
│├── en_GB-northern_english_male-medium.onnx
│├── en_GB-northern_english_male-medium.onnx.json
│├── en_GB-semaine-medium.onnx
│├── en_GB-semaine-medium.onnx.json
│├── en_GB-southern_english_female-low.onnx
│├── en_GB-southern_english_female-low.onnx.json
│├── en_GB-vctk-medium.onnx
│├── en_GB-vctk-medium.onnx.json
│├── english_configs.txt
│├── english_models.txt
│├── english_urls.txt
│├── en_US-amy-low.onnx
│├── en_US-amy-low.onnx.json
│├── en_US-amy-medium.onnx
│├── en_US-amy-medium.onnx.json
│├── en_US-arctic-medium.onnx
│├── en_US-arctic-medium.onnx.json
│├── en_US-bryce-medium.onnx
│├── en_US-bryce-medium.onnx.json
│├── en_US-danny-low.onnx
│├── en_US-danny-low.onnx.json
│├── en_US-hfc_female-medium.onnx
│├── en_US-hfc_female-medium.onnx.json
│├── en_US-hfc_male-medium.onnx
│├── en_US-hfc_male-medium.onnx.json
│├── en_US-joe-medium.onnx
│├── en_US-joe-medium.onnx.json
│├── en_US-john-medium.onnx
│├── en_US-john-medium.onnx.json
│├── en_US-kathleen-low.onnx
│├── en_US-kathleen-low.onnx.json
│├── en_US-kristin-medium.onnx
│├── en_US-kristin-medium.onnx.json
│├── en_US-kusal-medium.onnx
│├── en_US-kusal-medium.onnx.json
│├── en_US-l2arctic-medium.onnx
│├── en_US-l2arctic-medium.onnx.json
│├── en_US-lessac-high.onnx
│├── en_US-lessac-high.onnx.json
│├── en_US-lessac-low.onnx
│├── en_US-lessac-low.onnx.json
│├── en_US-lessac-medium.onnx
│├── en_US-lessac-medium.onnx.json
│├── en_US-libritts-high.onnx
│├── en_US-libritts-high.onnx.json
│├── en_US-libritts_r-medium.onnx
│├── en_US-libritts_r-medium.onnx.json
│├── en_US-ljspeech-high.onnx
│├── en_US-ljspeech-high.onnx.json
│├── en_US-ljspeech-medium.onnx
│├── en_US-ljspeech-medium.onnx.json
│├── en_US-norman-medium.onnx
│├── en_US-norman-medium.onnx.json
│├── en_US-ryan-high.onnx
│├── en_US-ryan-high.onnx.json
│├── en_US-ryan-low.onnx
│├── en_US-ryan-low.onnx.json
│├── en_US-ryan-medium.onnx
│├── en_US-ryan-medium.onnx.json
│├── female-low.onnx.json
│├── female-medium.onnx.json
│├── GB-alan-low.onnx.json
│├── GB-alan-medium.onnx.json
│├── GB-alba-medium.onnx.json
│├── GB-aru-medium.onnx.json
│├── GB-cori-high.onnx.json
│├── GB-cori-medium.onnx.json
│├── GB-semaine-medium.onnx.json
│├── GB-vctk-medium.onnx.json
│├── male-medium.onnx.json
│├── r-medium.onnx.json
│├── US-amy-low.onnx.json
│├── US-amy-medium.onnx.json
│├── US-arctic-medium.onnx.json
│├── US-bryce-medium.onnx.json
│├── US-danny-low.onnx.json
│├── US-joe-medium.onnx.json
│├── US-john-medium.onnx.json
│├── US-kathleen-low.onnx.json
│├── US-kristin-medium.onnx.json
│├── US-kusal-medium.onnx.json
│├── US-l2arctic-medium.onnx.json
│├── US-lessac-high.onnx.json
│├── US-lessac-low.onnx.json
│├── US-lessac-medium.onnx.json
│├── US-libritts-high.onnx.json
│├── US-ljspeech-high.onnx.json
│├── US-ljspeech-medium.onnx.json
│├── US-norman-medium.onnx.json
│├── US-ryan-high.onnx.json
│├── US-ryan-low.onnx.json
│├── US-ryan-medium.onnx.json
│└── app.cpython-311.pyc
├── README.md
├── requirements.txt
└── templates
    ├── text_form.html
    └── webpage_form.html

8 directories, 121 files

```