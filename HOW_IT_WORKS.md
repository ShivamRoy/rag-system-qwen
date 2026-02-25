# 🔄 System कैसे काम करता है?

## ✅ हां, बिल्कुल यही तरीका है!

### 📊 Complete Flow:

```
┌─────────────────────────────────────────────────────────┐
│  STEP 1: PDF Processing (एक बार)                        │
├─────────────────────────────────────────────────────────┤
│  1. PDF से text extract होता है                          │
│  2. Text को chunks में divide किया जाता है              │
│  3. हर chunk का embedding बनता है (vector)              │
│  4. Embeddings FAISS index में SAVE हो जाते हैं          │
│  5. Chunks metadata में SAVE हो जाते हैं                 │
│                                                          │
│  📁 Saved Files:                                        │
│     - embeddings/faiss.index (20KB)                     │
│     - embeddings/meta.pkl (6KB)                         │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  STEP 2: Question Answering (बार-बार)                   │
├─────────────────────────────────────────────────────────┤
│  1. User question आता है                                 │
│  2. Question का embedding बनता है                       │
│  3. Saved index से similar chunks मिलते हैं              │
│  4. Top 3 relevant chunks retrieve होते हैं             │
│  5. Chunks + Question → LLM को भेजा जाता है             │
│  6. LLM answer generate करता है                         │
│                                                          │
│  ⚡ Fast: PDF फिर से read नहीं होता!                     │
│  💾 Uses: Saved embeddings/index से काम करता है         │
└─────────────────────────────────────────────────────────┘
```

## 🎯 Key Points:

### ✅ **एक बार Processing:**
- PDF सिर्फ **एक बार** read होती है
- Embeddings **एक बार** बनते हैं
- Data **permanently save** हो जाता है

### ✅ **बार-बार Querying:**
- हर question के लिए PDF **फिर से read नहीं** होती
- Saved index से **fast search** होता है
- सिर्फ relevant chunks retrieve होते हैं

## 📁 Saved Data Structure:

```
embeddings/
├── faiss.index    # Vector embeddings (20KB)
└── meta.pkl       # Text chunks metadata (6KB)
```

## 🔍 Code Flow:

### Step 1: Index Building (एक बार)
```python
# main.py - build_index()
1. extract_text_from_pdf()      # PDF से text
2. chunk_text()                  # Chunks में divide
3. create_index_from_text_chunks() # Embeddings + Save
   → embeddings/faiss.index
   → embeddings/meta.pkl
```

### Step 2: Querying (बार-बार)
```python
# main.py - query_system()
1. retrieve_top_k(query)         # Saved index से search
   → load_faiss_index()          # Saved files load
   → Similar chunks find
2. construct_prompt()            # Context + Question
3. run_ollama()                  # LLM से answer
```

## 💡 Advantages:

1. **Fast**: PDF हर बार read नहीं होती
2. **Efficient**: सिर्फ relevant chunks use होते हैं
3. **Scalable**: बड़ी PDFs के लिए भी fast
4. **Persistent**: Index save रहता है, restart पर भी काम करता है

## 🔄 When to Rebuild Index:

Index rebuild करना होगा अगर:
- नई PDF add करनी हो
- PDF update हो
- Index corrupt हो जाए

अन्यथा, **एक बार build = हमेशा use!**

## 📊 Example:

```
First Run:
  PDF Read → Chunks → Embeddings → Save (2-5 min)
  
Next Runs:
  Question → Load Index → Search → Answer (2-5 sec)
  
No PDF Reading Again! ✅
```

