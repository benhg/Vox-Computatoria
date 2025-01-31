#!/bin/bash

# Directory containing downloaded models
MODEL_DIR="piper_voices"

# Ensure the directory exists
if [ ! -d "$MODEL_DIR" ]; then
    echo "Error: $MODEL_DIR does not exist. Please run the model download script first."
    exit 1
fi

# Change to the model directory
cd "$MODEL_DIR"

# Loop through all .onnx models and download the corresponding config
for model in *.onnx; do
    if [[ -f "$model" ]]; then
        base_name="${model%.onnx}"
        config_url="https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/${base_name//_//}.onnx.json?download=true"
        echo "Downloading config: $config_url"
        curl -O "$config_url"
    fi
done

echo "Download completed! Config files are saved in $MODEL_DIR."
