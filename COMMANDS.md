# 🚀 Project चलाने के लिए Commands

## Step 1: Dependencies Install करें

```bash
cd /Users/shivamtomar/Code/rag-qwen
python3 -m pip install --user -r requirements.txt
```

**अगर --user flag काम न करे, तो:**
```bash
python3 -m pip install -r requirements.txt --break-system-packages
```

या virtual environment use करें:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Step 2: Test करें (Optional)

```bash
python3 test_project.py
```

यह script बताएगा कि सब कुछ ready है या नहीं।

## Step 3: Project Run करें

### Option A: Web Interface (Recommended)
```bash
streamlit run app.py
```
फिर browser में खोलें: `http://localhost:8501`

### Option B: Command Line
```bash
python3 main.py
```

## Quick Test Commands

```bash
# 1. Dependencies check
python3 test_project.py

# 2. Install dependencies
python3 -m pip install --user -r requirements.txt

# 3. Run web interface
streamlit run app.py

# 4. या command line
python3 main.py
```

## Troubleshooting

### अगर pip install नहीं हो रहा:
```bash
# Virtual environment use करें
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

### अगर Ollama नहीं चल रहा:
```bash
# Check Ollama
ollama list

# Model pull करें (अगर नहीं है)
ollama pull qwen:latest
```

### Port already in use (Streamlit):
```bash
streamlit run app.py --server.port 8502
```

