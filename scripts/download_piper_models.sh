

#!/bin/bash

# Define the base URL for the Piper voices repository
BASE_URL="https://raw.githubusercontent.com/rhasspy/piper/master/VOICES.md"

# Fetch the VOICES.md file
curl -s $BASE_URL -o VOICES.md

# Check if the VOICES.md file was downloaded successfully
if [ ! -f VOICES.md ]; then
    echo "Failed to download VOICES.md. Please check your internet connection or the URL."
    exit 1
fi

# Create a directory to store the downloaded voices
mkdir -p piper_voices
cd piper_voices

# Extract and download only the English (US and UK) model files (.onnx)
grep -A 2 -E 'English \(US\)|English \(UK\)' ../VOICES.md | grep -Eo '(http|https)://[^ ]+' | grep '\.onnx$' | while read -r url; do
    echo "Downloading $url..."
    curl -O $url?download=true
done

# Clean up
cd ..
rm VOICES.md

echo "Download completed. All model files (.onnx) are saved in the 'piper_voices' directory."
