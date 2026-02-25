#!/bin/bash

# RAG Project Runner Script
echo "🚀 RAG Project Setup & Run Script"
echo "=================================="

# Check if we're in the right directory
if [ ! -f "requirements.txt" ]; then
    echo "❌ Error: requirements.txt not found. Please run from project root."
    exit 1
fi

# Step 1: Test current setup
echo ""
echo "📋 Step 1: Testing current setup..."
python3 test_project.py

# Step 2: Ask to install dependencies
echo ""
read -p "Do you want to install missing dependencies? (y/n): " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "📦 Installing dependencies..."
    python3 -m pip install --user -r requirements.txt || {
        echo "⚠️  --user flag failed, trying with --break-system-packages..."
        python3 -m pip install -r requirements.txt --break-system-packages
    }
fi

# Step 3: Choose interface
echo ""
echo "Choose interface to run:"
echo "1) Web Interface (Streamlit) - Recommended"
echo "2) Command Line Interface"
read -p "Enter choice (1 or 2): " choice

if [ "$choice" == "1" ]; then
    echo ""
    echo "🌐 Starting Streamlit web interface..."
    echo "   Open http://localhost:8501 in your browser"
    streamlit run app.py
elif [ "$choice" == "2" ]; then
    echo ""
    echo "💻 Starting command line interface..."
    python3 main.py
else
    echo "❌ Invalid choice"
    exit 1
fi

