# 🚀 Project चलाने के लिए Step-by-Step Guide

## Step 1: Dependencies Install करें

```bash
cd /Users/shivamtomar/Code/rag-qwen
python3 -m pip install -r requirements.txt
```

**Note:** अगर `pip` नहीं है तो:
```bash
python3 -m ensurepip --upgrade
python3 -m pip install -r requirements.txt
```

## Step 2: Ollama Model Check करें

आपके पास `qwen:latest` model है, जो perfect है! अगर नहीं है तो:
```bash
ollama pull qwen:latest
```

## Step 3: Project Run करें

```bash
python3 main.py
```

## क्या होगा?

1. **पहली बार run करने पर:**
   - PDF से text extract होगा
   - Text chunks में divide होगा
   - Embeddings create होंगे
   - FAISS index बनेगा (यह 2-5 मिनट ले सकता है)

2. **फिर आपसे question पूछा जाएगा:**
   - आप कोई भी question type करें
   - System relevant chunks find करेगा
   - Qwen model से answer generate होगा

## Example Questions:

- "What is Shoolini University?"
- "What courses are offered?"
- "Where is the university located?"

## Troubleshooting:

### अगर dependencies install नहीं हो रही:
```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

### अगर Ollama नहीं चल रहा:
```bash
# Ollama service start करें
ollama serve
# दूसरे terminal में project run करें
```

### अगर model नहीं मिल रहा:
```bash
ollama pull qwen:latest
```

## Quick Test:

```bash
# Terminal में ये commands run करें:
cd /Users/shivamtomar/Code/rag-qwen
python3 -m pip install -r requirements.txt
python3 main.py
```

