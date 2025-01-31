#!/bin/bash

# Directory containing the .json files
DIR="."

# Ensure the directory exists
if [ ! -d "$DIR" ]; then
    echo "Error: Directory $DIR does not exist."
    exit 1
fi

# Change to the directory
cd "$DIR"

# Rename all .json files to remove "?download=true.json"
for file in *.json\?download=true.json; do
    if [[ -f "$file" ]]; then
        new_name="${file%\?download=true.json}"  # Remove "?download=true.json"
        mv "$file" "$new_name"
        echo "Renamed: $file -> $new_name"
    fi
done

echo "Renaming complete!"
