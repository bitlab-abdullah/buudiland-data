#!/bin/bash
# Development server script with CORS support

PORT=${1:-8000}
DIR=${2:-_site}

echo "Starting development server..."
echo "Port: $PORT"
echo "Directory: $DIR"

# Check if _site directory exists
if [ ! -d "$DIR" ]; then
    echo "Error: Directory '$DIR' not found."
    echo "Please run 'python scripts/build_data.py' first to build the site."
    exit 1
fi

# Make sure the Python script is executable
chmod +x serve.py

# Start the server
python3 serve.py --port $PORT --dir $DIR