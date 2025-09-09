# Create a simple startup script for easy running
startup_script = '''#!/bin/bash

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
'''

# Save the startup script
with open('start_website.sh', 'w', encoding='utf-8') as f:
    f.write(startup_script)

# Make the script executable (for Unix-like systems)
import os
try:
    os.chmod('start_website.sh', 0o755)
    print("✅ Created start_website.sh - Executable startup script")
except:
    print("✅ Created start_website.sh - Startup script (make executable with: chmod +x start_website.sh)")

# Create a quick start guide
quick_start = '''# Quick Start Guide

## 🚀 3-Step Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Website
```bash
streamlit run app.py
```

### Step 3: Open Browser
Navigate to: http://localhost:8501

## 🎯 Alternative Methods

### Method 1: Using the Startup Script (macOS/Linux)
```bash
chmod +x start_website.sh
./start_website.sh
```

### Method 2: With Virtual Environment
```bash
python3.9 -m venv sap_website_env
source sap_website_env/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

### Method 3: Direct Command
```bash
python3.9 -m streamlit run app.py --server.port 8501
```

## 📱 Accessing Different Pages

Once running, use the sidebar navigation to access:
- **Home** - Landing page
- **Services** - Detailed service information  
- **Portfolio** - Case studies and demos
- **About** - Company information

## 🔧 Troubleshooting

**Issue: Command not found**
```bash
# Try these alternatives:
python3 -m streamlit run app.py
python -m streamlit run app.py
/usr/bin/python3 -m streamlit run app.py
```

**Issue: Port already in use**
```bash
streamlit run app.py --server.port 8502
```

**Issue: Module not found**
```bash
pip install --upgrade streamlit==1.49.0
pip install -r requirements.txt
```

Happy coding! 🎉
'''

with open('QUICK_START.md', 'w', encoding='utf-8') as f:
    f.write(quick_start)

print("✅ Created QUICK_START.md - Simple setup guide")

# List all created files
print("\n📁 Created Files:")
print("   ├── app.py (Main landing page)")
print("   ├── requirements.txt (Dependencies)")
print("   ├── pages/")
print("   │   ├── Services.py (Services page)")
print("   │   ├── Portfolio.py (Portfolio page)")
print("   │   └── About.py (About page)")
print("   ├── README.md (Detailed documentation)")
print("   ├── QUICK_START.md (Quick setup guide)")
print("   └── start_website.sh (Startup script)")

print("\n🎉 Website creation complete!")
print("💡 Run: streamlit run app.py")
print("🌐 Then visit: http://localhost:8501")