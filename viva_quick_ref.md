# ⚡ Viva Quick Reference - One Page Summary

## 🎯 Project in 30 Seconds
**Agentic RAG System** - Intelligent Q&A system that switches between PDF-based RAG and Direct AI modes. Completely local, no APIs, free.

---

## 📦 Tech Stack (Versions)

| Tech | Version | Why? |
|------|---------|------|
| Python | 3.13.3 | Latest stable |
| LangChain | 1.1.3 | Modular, stable (not 0.x old, not 2.x beta) |
| Streamlit | 1.52.1 | Easy ML UI, Python-only |
| FAISS-CPU | 1.13.1 | Local, free, fast (not GPU/cloud needed) |
| Sentence Transformers | 5.1.2 | Local embeddings (not OpenAI API) |
| Ollama + Qwen | Latest | Local LLM (not GPT API - privacy/cost) |
| PyMuPDF | Latest | Better than PyPDF2 |

---

## 🔑 Key Questions & One-Line Answers

**Q: What is RAG?**  
A: Retrieval-Augmented Generation - Retrieve relevant info from PDF, augment prompt, generate answer.

**Q: Why LangChain 1.1.3?**  
A: Stable, modular (not 0.x old, not 2.x beta), actively maintained.

**Q: Why FAISS-CPU not GPU?**  
A: No GPU needed, works on any machine, fast enough for our use case.

**Q: Why Sentence Transformers not OpenAI?**  
A: Local, free, private, no API costs.

**Q: Why Ollama not GPT API?**  
A: Completely local, free, no API keys, privacy, works offline.

**Q: Why Streamlit not Flask?**  
A: Rapid development, Python-only, perfect for ML apps.

**Q: Why PyMuPDF not PyPDF2?**  
A: Better text extraction, faster, handles complex PDFs.

**Q: What are the 3 modes?**  
A: Auto (AI decides), RAG (PDF-based), Direct (General AI).

**Q: How does agentic work?**  
A: Analyzes question → decides if needs PDF → uses RAG or Direct accordingly.

**Q: Why chunk size 500?**  
A: Balance between context and relevance (not too small/large).

---

## 🏗️ Architecture Flow

```
PDF → Extract → Chunk → Embed → FAISS Index (SAVE)
                                    ↓
User Question → Embed → Search → Retrieve → LLM → Answer
```

---

## 💡 Why Not Alternatives?

| Alternative | Why Not? |
|-------------|----------|
| OpenAI API | Cost, privacy, internet needed |
| FAISS-GPU | GPU required, complex setup |
| Pinecone/Weaviate | Cloud, API keys, paid |
| Flask/Django | More code, overkill |
| PyPDF2 | Older, less efficient |
| GPT-4 | Expensive, API dependency |

---

## 🎯 Demo Flow

1. Upload PDF → Build Index (one-time)
2. Ask PDF question → Shows RAG mode
3. Ask general question → Shows Direct mode
4. Auto mode → AI decides automatically

---

## 📊 System Specs

- **Chunk Size**: 500 chars
- **Overlap**: 50 chars
- **Embedding Model**: e5-small-v2 (384 dims)
- **Top-K Retrieval**: 3 chunks
- **Index Type**: FAISS IndexFlatL2

---

## ✅ Advantages

- ✅ Completely local (privacy)
- ✅ Free (no API costs)
- ✅ Fast (local processing)
- ✅ Intelligent (agentic decisions)
- ✅ Flexible (3 modes)

---

## ⚠️ Limitations

- Model smaller than GPT-4
- Requires local resources
- Index building takes time
- Single PDF at a time

---

**Remember: Everything is LOCAL, FREE, and PRIVATE! 🚀**

