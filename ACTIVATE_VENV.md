# 🔧 Virtual Environment Activate करने के लिए

## Simple Command:

```bash
cd /Users/shivamtomar/Code/rag-qwen
source venv/bin/activate
```

## क्या होगा:

जब आप `source venv/bin/activate` run करेंगे:
- Terminal prompt में `(venv)` दिखेगा
- इसका मतलब है virtual environment active है
- अब आप `pip install` और `python3` commands use कर सकते हैं

## Example:

```bash
# Before activation
shivamtomar@MacBook ~ % 

# After activation  
(venv) shivamtomar@MacBook ~ % 
```

## Complete Steps:

```bash
# 1. Project directory में जाएं
cd /Users/shivamtomar/Code/rag-qwen

# 2. Virtual environment activate करें
source venv/bin/activate

# 3. Check करें (optional)
which python3  # Should show venv path

# 4. Project run करें
streamlit run app.py
```

## Deactivate करने के लिए:

जब काम खत्म हो जाए, तो:
```bash
deactivate
```

## Quick One-Liner:

```bash
cd /Users/shivamtomar/Code/rag-qwen && source venv/bin/activate && streamlit run app.py
```

## Troubleshooting:

### अगर `venv` folder नहीं है:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### अगर activation नहीं हो रहा:
```bash
# Check if venv exists
ls -la venv/

# If not, create it
python3 -m venv venv
source venv/bin/activate
```

