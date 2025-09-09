#!/bin/bash

# SAPMaster Solutions Website Startup Script
# Compatible with macOS and Python 3.9.6 / Streamlit 1.49.0

echo "🚀 Starting SAPMaster Solutions Website..."
echo "📋 System Information:"
echo "   Python Version: $(python3.9 --version 2>/dev/null || python3 --version 2>/dev/null || python --version)"
echo "   Streamlit Version: $(streamlit --version 2>/dev/null || echo 'Streamlit not installed')"
echo "   Operating System: $(uname -s)"
echo ""

# Check if virtual environment exists
if [ -d "sap_website_env" ]; then
    echo "🔧 Activating virtual environment..."
    source sap_website_env/bin/activate
else
    echo "⚠️  Virtual environment not found. Consider creating one:"
    echo "   python3.9 -m venv sap_website_env"
    echo "   source sap_website_env/bin/activate"
    echo "   pip install -r requirements.txt"
    echo ""
fi

# Check if requirements are installed
echo "📦 Checking dependencies..."
if command -v streamlit &> /dev/null; then
    echo "✅ Streamlit is installed"
else
    echo "❌ Streamlit not found. Installing..."
    pip install -r requirements.txt
fi

echo ""
echo "🌐 Starting Streamlit server..."
echo "📍 Website will be available at: http://localhost:8501"
echo "🛑 Press Ctrl+C to stop the server"
echo ""

# Start the Streamlit application
streamlit run app.py --server.headless true --server.port 8501
