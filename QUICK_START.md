# ⚡ Quick Start - Project चलाने के लिए

## ✅ Status: Project Ready!

सभी dependencies install हो गई हैं और project test pass हो गया है।

## 🚀 चलाने के लिए Commands:

### Method 1: Virtual Environment (Recommended - Already Setup!)

```bash
cd /Users/shivamtomar/Code/rag-qwen
source venv/bin/activate
streamlit run app.py
```

या command line के लिए:
```bash
source venv/bin/activate
python3 main.py
```

### Method 2: Direct Run (अगर dependencies system-wide install हैं)

```bash
cd /Users/shivamtomar/Code/rag-qwen
streamlit run app.py
```

या:
```bash
python3 main.py
```

## 📋 Complete Setup Commands (अगर fresh start करना हो):

```bash
# 1. Project directory में जाएं
cd /Users/shivamtomar/Code/rag-qwen

# 2. Virtual environment बनाएं (अगर नहीं है)
python3 -m venv venv

# 3. Virtual environment activate करें
source venv/bin/activate

# 4. Dependencies install करें
pip install -r requirements.txt

# 5. Test करें (optional)
python3 test_project.py

# 6. Run करें
streamlit run app.py
```

## 🎯 What's Working:

✅ **All Dependencies**: Installed in virtual environment  
✅ **FAISS Index**: Already built and ready  
✅ **PDF File**: Present in data/ folder  
✅ **Ollama**: Installed with Qwen model  
✅ **Retrieval System**: Tested and working  

## 🌐 Web Interface:

जब `streamlit run app.py` run करेंगे:
- Browser automatically खुलेगा
- URL: `http://localhost:8501`
- Sidebar में PDF upload और index building
- Main area में chat interface

## 💻 Command Line:

जब `python3 main.py` run करेंगे:
- Terminal में question पूछने को prompt आएगा
- Answer directly terminal में दिखेगा

## 🧪 Test Results:

```
✅ sentence-transformers - Installed
✅ faiss-cpu - Installed  
✅ langchain - Installed
✅ PyMuPDF - Installed
✅ streamlit - Installed
✅ All files present
✅ Ollama ready with Qwen model
✅ Retrieval system tested and working
```

## 🎉 Ready to Demo!

Project practical demonstration के लिए पूरी तरह ready है!

