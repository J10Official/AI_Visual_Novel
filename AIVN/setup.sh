#!/bin/bash

echo "=== Generative Visual Novel Setup ==="
echo

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    exit 1
fi

echo "✓ Python 3 found"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "✓ Virtual environment ready"

# Activate virtual environment
source venv/bin/activate

echo "✓ Virtual environment activated"

# Install requirements
echo "Installing Python packages..."
pip install -r requirements.txt

echo "✓ Dependencies installed"

# Check for .env file
if [ ! -f ".env" ]; then
    echo
    echo "⚠️  Warning: .env file not found!"
    echo "Please create a .env file with your Gemini API key:"
    echo "GEMINI_API_KEY=your_api_key_here"
    echo
    echo "You can copy .env.example to .env and edit it:"
    echo "cp .env.example .env"
    echo
else
    echo "✓ .env file found"
fi

echo
echo "=== Setup Complete ==="
echo
echo "To run the application:"
echo "1. Make sure your .env file has a valid GEMINI_API_KEY"
echo "2. Run: source venv/bin/activate"
echo "3. Run: python app.py"
echo "4. Open http://localhost:5000 in your browser"
echo