#!/bin/bash

echo "🔧 Creating virtual environment..."
python3 -m venv venv || { echo "❌ Failed to create virtualenv"; exit 1; }

echo "✅ Virtual environment created at ./venv"

echo "📦 Activating virtual environment and installing requirements..."
source venv/bin/activate

# Create requirements.txt if it doesn't exist
if [ ! -f requirements.txt ]; then
  echo "flask" > requirements.txt
  echo "opencv-python-headless" >> requirements.txt
fi

pip install --upgrade pip
pip install -r requirements.txt || { echo "❌ Failed to install packages"; exit 1; }

echo "✅ All packages installed."
echo "🎥 You can now run: source venv/bin/activate && python stream_server.py"

