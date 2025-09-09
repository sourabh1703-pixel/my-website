# Quick Start Guide

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
