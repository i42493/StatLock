#!/bin/bash

# StatLock Setup Script
# This script helps set up the StatLock AI sports betting chatbot

echo "================================================"
echo "  StatLock - AI Sports Betting Chatbot Setup"
echo "================================================"
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Found Python version: $python_version"

# Check if Python 3.8+ is installed
python3 -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)"
if [ $? -ne 0 ]; then
    echo "Error: Python 3.8 or higher is required"
    exit 1
fi
echo "✓ Python version is compatible"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt
if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed successfully"
else
    echo "✗ Failed to install dependencies"
    exit 1
fi
echo ""

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "✓ .env file created"
    echo ""
    echo "IMPORTANT: Please edit .env and add your OpenAI API key"
    echo "You can get an API key from: https://platform.openai.com/api-keys"
    echo ""
    read -p "Press Enter to open .env file in editor (or Ctrl+C to skip)..."
    ${EDITOR:-nano} .env
else
    echo "✓ .env file already exists"
fi
echo ""

echo "================================================"
echo "  Setup Complete!"
echo "================================================"
echo ""
echo "Next steps:"
echo "1. Make sure your OPENAI_API_KEY is set in the .env file"
echo "2. Run the chatbot:"
echo "   - Interactive mode: python main.py"
echo "   - Demo mode: python main.py --demo"
echo ""
echo "For more examples, see EXAMPLES.md"
echo ""
echo "To activate the virtual environment in the future, run:"
echo "  source venv/bin/activate"
echo ""
