#!/bin/bash

# Find the project directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Output location
OUTPUT_DIR="$PROJECT_DIR/data"
OUTPUT_FILE="$OUTPUT_DIR/disks.json"

# Create data directory if required
mkdir -p "$OUTPUT_DIR"

# Collect disk information
lsblk -J \
    -o NAME,PATH,SIZE,TYPE,FSTYPE,MOUNTPOINTS \
    > "$OUTPUT_FILE"

echo "Disk inventory collected successfully."
echo "Output: $OUTPUT_FILE"
