# 🎓 Viva Preparation - Agentic RAG System with Qwen LLM

## 📋 Project Overview

**Project Name:** Agentic RAG (Retrieval-Augmented Generation) System with Local LLM  
**Technology Stack:** Python, Streamlit, Ollama, FAISS, Sentence Transformers  
**Core Concept:** Intelligent document Q&A system that switches between RAG and Direct Generative AI modes

---

## 🔧 Technical Stack & Versions

### Core Technologies Used:

| Technology | Version | Purpose | Why This Version? |
|------------|---------|---------|-------------------|
| **Python** | 3.13.3 | Base language | Latest stable, better performance |
| **LangChain** | 1.1.3 | Text processing framework | Modular architecture, active development |
| **LangChain Text Splitters** | 1.0.0 | Text chunking | Required for LangChain 1.x compatibility |
| **Streamlit** | 1.52.1 | Web interface | Easy to use, rapid prototyping, no frontend code needed |
| **Sentence Transformers** | 5.1.2 | Embedding generation | State-of-the-art embeddings, efficient |
| **FAISS** | 1.13.1 (CPU) | Vector similarity search | Fast similarity search, Facebook's optimized library |
| **PyTorch** | 2.9.1 | Deep learning backend | Required by sentence-transformers |
| **Transformers** | 4.57.3 | HuggingFace transformers | Model loading and inference |
| **PyMuPDF (fitz)** | Latest | PDF text extraction | Better than PyPDF2, handles complex PDFs |
| **Ollama** | Latest | Local LLM inference | No API keys needed, completely local, lightweight |

### Model Used:
- **Qwen:latest** (via Ollama) - Alibaba's open-source LLM, lightweight, good performance

---

## ❓ Viva Questions & Answers

### 1. **What is your project about?**

**Answer:**
My project is an **Agentic RAG (Retrieval-Augmented Generation) System** that provides intelligent question-answering capabilities for PDF documents. The system has three modes:
- **Auto Mode (Agentic)**: AI automatically decides whether to use PDF context or general knowledge
- **RAG Mode**: Uses PDF document context for answers
- **Direct Mode**: Uses general AI knowledge without PDF context

The system processes PDFs once, creates vector embeddings, stores them in FAISS index, and then uses these embeddings to retrieve relevant context for answering questions.

---

### 2. **Why did you choose LangChain version 1.1.3? Why not 0.x or 2.x?**

**Answer:**
I chose **LangChain 1.1.3** because:
- **Modular Architecture**: Version 1.x introduced modular packages (langchain-core, langchain-text-splitters), making it more maintainable
- **Better Performance**: Improved efficiency compared to 0.x versions
- **Active Development**: Version 1.x is actively maintained with regular updates
- **Compatibility**: Works well with modern Python versions (3.8+)
- **Why not 0.x**: Version 0.x had monolithic structure, less efficient, and is being phased out
- **Why not 2.x**: Version 2.x is still in development/beta, 1.1.3 is stable and production-ready

---

### 3. **Why did you use FAISS-CPU instead of FAISS-GPU or other vector databases?**

**Answer:**
I chose **FAISS-CPU (1.13.1)** because:
- **No GPU Required**: Works on any machine without GPU, making it accessible
- **Sufficient Performance**: For this use case (small to medium documents), CPU is fast enough
- **Easy Setup**: No CUDA installation needed, simpler deployment
- **Cost-Effective**: No need for expensive GPU hardware
- **Why not FAISS-GPU**: Requires CUDA setup, GPU hardware, more complex configuration
- **Why not Pinecone/Weaviate**: These are cloud services requiring API keys, internet connection, and paid subscriptions. FAISS is free, local, and open-source.

---

### 4. **Why Sentence Transformers 5.1.2? Why not OpenAI embeddings or other embedding models?**

**Answer:**
I chose **Sentence Transformers 5.1.2** with **intfloat/e5-small-v2** model because:
- **Local Processing**: No API calls, works offline, no cost per request
- **Privacy**: Data never leaves the local machine
- **Fast**: Optimized for local inference
- **Good Quality**: e5-small-v2 provides excellent embeddings for semantic search
- **Why not OpenAI embeddings**: Requires API key, internet connection, costs money per request, data privacy concerns
- **Why not BERT/RoBERTa directly**: Sentence Transformers provides easier API, better optimized for semantic similarity tasks

---

### 5. **Why Streamlit 1.52.1? Why not Flask, Django, or React?**

**Answer:**
I chose **Streamlit 1.52.1** because:
- **Rapid Development**: Can build web UI in minutes without HTML/CSS/JavaScript
- **Python-Only**: Everything in Python, no frontend framework needed
- **Interactive**: Built-in widgets, real-time updates
- **Perfect for ML/AI**: Designed specifically for data science and ML applications
- **Why not Flask/Django**: Requires HTML templates, more boilerplate code, overkill for this use case
- **Why not React**: Requires JavaScript knowledge, separate frontend/backend, more complex setup

---

### 6. **Why Ollama and Qwen model? Why not OpenAI GPT, Anthropic Claude, or other APIs?**

**Answer:**
I chose **Ollama with Qwen:latest** because:
- **Completely Local**: No API keys, no internet required, runs on your machine
- **Free**: No per-request costs, unlimited usage
- **Privacy**: Data never sent to external servers
- **Lightweight**: Qwen is optimized for local inference, smaller model size
- **Fast**: Local inference is faster than API calls for small models
- **Why not OpenAI GPT**: Requires API key, costs money, internet needed, data privacy concerns
- **Why not Claude/Other APIs**: Same issues - cost, privacy, dependency on external services

---

### 7. **Why PyMuPDF (fitz) instead of PyPDF2 for PDF extraction?**

**Answer:**
I chose **PyMuPDF (fitz)** because:
- **Better Text Extraction**: Handles complex PDFs, tables, and formatted text better
- **Faster**: More efficient than PyPDF2
- **Better Layout Preservation**: Maintains document structure
- **Handles Images**: Can extract images if needed in future
- **Why not PyPDF2**: Older library, struggles with complex PDFs, slower, less maintained

---

### 8. **What is RAG and why did you implement it?**

**Answer:**
**RAG (Retrieval-Augmented Generation)** is a technique that combines:
1. **Retrieval**: Finding relevant information from a knowledge base (PDF in our case)
2. **Augmentation**: Adding that context to the prompt
3. **Generation**: Using LLM to generate answer based on retrieved context

**Why RAG?**
- **Accuracy**: Answers are based on actual document content, not just model's training data
- **Up-to-date**: Can answer questions about recent documents not in model's training
- **Reduced Hallucination**: Model has actual context to base answers on
- **Domain-Specific**: Can work with specialized documents (medical, legal, etc.)

---

### 9. **What is the difference between RAG mode and Direct mode in your system?**

**Answer:**

**RAG Mode:**
- Uses PDF document context
- Retrieves relevant chunks from FAISS index
- Answers based on document content
- Shows retrieved contexts
- Best for document-specific questions

**Direct Mode:**
- Uses general AI knowledge only
- No PDF context needed
- Faster response time
- No index required
- Best for general knowledge questions

**Auto Mode (Agentic):**
- AI decides automatically
- Analyzes question to determine if PDF context is needed
- Most intelligent and flexible approach

---

### 10. **How does the agentic decision-making work?**

**Answer:**
The agentic engine uses a two-step process:

1. **Keyword Analysis**: Checks for PDF-related keywords (pdf, document, about, what is, etc.)

2. **LLM-Based Decision**: Uses Ollama to analyze the question and decide:
   - If question needs PDF context → Uses RAG mode
   - If question is general knowledge → Uses Direct mode

3. **Fallback**: If LLM decision fails, falls back to keyword-based decision

This makes the system intelligent enough to automatically choose the best approach for each question.

---

### 11. **Explain the complete flow of your system.**

**Answer:**

**Index Building Phase (One-time):**
1. PDF → Text extraction using PyMuPDF
2. Text → Chunking using LangChain RecursiveCharacterTextSplitter
3. Chunks → Embeddings using Sentence Transformers (e5-small-v2)
4. Embeddings → Stored in FAISS index
5. Metadata → Saved as pickle file

**Query Phase (Repeated):**
1. User question → Embedding generation
2. Embedding → FAISS similarity search
3. Top-k chunks → Retrieved
4. Chunks + Question → Prompt construction
5. Prompt → Ollama (Qwen model)
6. Response → Generated answer

**Agentic Flow:**
- Question analyzed → Mode decision (RAG/Direct)
- If RAG: Follows query phase above
- If Direct: Directly sends to Ollama without retrieval

---

### 12. **Why did you use FAISS IndexFlatL2? Why not other FAISS index types?**

**Answer:**
I used **IndexFlatL2** because:
- **Simplicity**: Easiest to implement and understand
- **Exact Search**: Returns exact nearest neighbors (no approximation)
- **Sufficient for Small-Medium Data**: For typical PDF documents, exact search is fast enough
- **No Training Required**: Works immediately without index training
- **Why not IVF (Inverted File Index)**: More complex, requires training, better for very large datasets (millions of vectors)
- **Why not HNSW (Hierarchical Navigable Small World)**: More memory, better for billion-scale data, overkill for our use case

---

### 13. **What is the chunk size and overlap you used? Why?**

**Answer:**
- **Chunk Size**: 500 characters
- **Chunk Overlap**: 50 characters

**Why these values?**
- **500 characters**: Good balance between context preservation and embedding quality. Too small loses context, too large dilutes relevance
- **50 characters overlap**: Ensures continuity between chunks, prevents information loss at boundaries
- **Why not larger chunks**: Larger chunks (1000+) can include irrelevant information, reducing retrieval precision
- **Why not smaller chunks**: Smaller chunks (200-) lose context and semantic meaning

---

### 14. **How do you handle errors in your system?**

**Answer:**
The system handles errors at multiple levels:

1. **File Not Found**: Checks if PDF exists before processing
2. **Index Not Found**: Validates index exists before querying
3. **Ollama Errors**: Catches subprocess errors, shows warnings
4. **Import Errors**: Graceful fallback if modules missing
5. **User Input**: Validates user queries before processing

All errors are caught with try-except blocks and user-friendly error messages are displayed.

---

### 15. **What are the advantages of your system?**

**Answer:**

1. **Completely Local**: No API keys, no internet needed, full privacy
2. **Cost-Effective**: Free to run, no per-request costs
3. **Fast**: Local processing is faster than API calls
4. **Intelligent**: Agentic decision-making for optimal mode selection
5. **Flexible**: Three modes (Auto, RAG, Direct) for different use cases
6. **User-Friendly**: Streamlit interface, easy to use
7. **Scalable**: Can handle multiple PDFs, rebuild index as needed
8. **Open Source**: All technologies are open-source

---

### 16. **What are the limitations of your system?**

**Answer:**

1. **Model Size**: Qwen is smaller than GPT-4, so answers may be less detailed
2. **Local Processing**: Requires local machine resources (CPU/RAM)
3. **Index Building**: Takes time for large PDFs (2-5 minutes)
4. **Single PDF**: Currently processes one PDF at a time (can be extended)
5. **No Multi-turn Context**: Doesn't maintain conversation context across queries (can be added)

---

### 17. **How would you improve this system?**

**Answer:**

1. **Multi-PDF Support**: Process and query multiple PDFs simultaneously
2. **Conversation Memory**: Maintain context across multiple questions
3. **Better Chunking**: Semantic chunking instead of character-based
4. **Hybrid Search**: Combine keyword and semantic search
5. **Streaming Responses**: Show answers as they generate
6. **Model Selection**: Allow users to choose different Ollama models
7. **Export Functionality**: Export conversations and answers
8. **Better UI**: More interactive visualizations

---

### 18. **Why Python 3.13.3? Why not older versions?**

**Answer:**
- **Latest Features**: Better performance, new language features
- **Library Compatibility**: All modern libraries support Python 3.8+
- **Performance**: Python 3.13 has performance improvements
- **Why not 3.7 or older**: Many libraries (LangChain, Streamlit) require Python 3.8+
- **Why not 3.9/3.10**: 3.13 is latest stable, but 3.9+ would also work fine

---

### 19. **What is the difference between your system and ChatGPT?**

**Answer:**

| Feature | My System | ChatGPT |
|---------|-----------|---------|
| **Data Source** | Your PDF documents | Internet training data |
| **Privacy** | Completely local | Data sent to OpenAI |
| **Cost** | Free | Paid subscription |
| **Customization** | Can use any PDF | Limited to training data |
| **Offline** | Works offline | Requires internet |
| **API Keys** | Not needed | Required |
| **Domain-Specific** | Can answer about your documents | General knowledge only |

---

### 20. **Explain the architecture of your system.**

**Answer:**

**Architecture Layers:**

1. **Presentation Layer**: Streamlit web interface (app.py)
2. **Business Logic Layer**: 
   - Agentic Engine (agentic_engine.py) - Decision making
   - Query Engine (query_engine.py) - RAG processing
3. **Data Processing Layer**:
   - PDF Loader (load_pdf.py)
   - Text Chunker (chunk_text.py)
   - Embedding Generator (embed_store.py)
4. **Storage Layer**: FAISS index + Pickle metadata
5. **LLM Layer**: Ollama with Qwen model

**Data Flow:**
User → Streamlit UI → Agentic Engine → (RAG/Direct) → Ollama → Response → UI

---

### 21. **What is the time complexity of your retrieval system?**

**Answer:**
- **FAISS IndexFlatL2**: O(n*d) where n = number of vectors, d = dimension
- **For our use case**: Typically n = 50-200 chunks, d = 384 (e5-small-v2 dimension)
- **Search Time**: < 1 second for typical documents
- **Why efficient**: FAISS uses optimized C++ backend, very fast for our scale

---

### 22. **Why did you choose e5-small-v2 embedding model?**

**Answer:**
- **Size**: Small model (fast inference)
- **Quality**: Good semantic understanding
- **Multilingual**: Supports multiple languages
- **Efficiency**: 384 dimensions (smaller than larger models, faster)
- **Why not larger models**: Larger models (e5-large) are slower, more memory, overkill for this use case
- **Why not OpenAI embeddings**: Requires API, costs money, privacy concerns

---

### 23. **How does your system handle different types of questions?**

**Answer:**

**Document-Specific Questions** (e.g., "What is Shoolini University?"):
- Auto mode → Detects needs PDF → Uses RAG
- Retrieves relevant chunks
- Answers based on PDF content

**General Knowledge Questions** (e.g., "What is Python?"):
- Auto mode → Detects general question → Uses Direct
- No PDF retrieval
- Answers from model's training data

**Mixed Questions**: System intelligently handles both types automatically.

---

### 24. **What security measures did you implement?**

**Answer:**
1. **Local Processing**: All data stays on local machine
2. **No API Keys**: No external service authentication needed
3. **No Data Transmission**: Nothing sent to external servers
4. **File Validation**: Checks file existence and format
5. **Error Handling**: Prevents crashes, shows user-friendly errors

---

### 25. **How would you deploy this system?**

**Answer:**

**Current**: Local development (Streamlit local server)

**Production Options**:
1. **Streamlit Cloud**: Free hosting for Streamlit apps
2. **Docker Container**: Package everything in Docker
3. **Local Server**: Deploy on local network
4. **Cloud VM**: AWS/GCP/Azure with Ollama installed

**Requirements for Deployment**:
- Python environment
- Ollama installed
- All dependencies
- Sufficient RAM/CPU for model inference

---

## 🎯 Key Points to Remember

1. **All processing is LOCAL** - No cloud, no APIs, complete privacy
2. **Three modes** - Auto (Agentic), RAG, Direct
3. **One-time indexing** - PDF processed once, queried many times
4. **FAISS for fast search** - Optimized vector similarity
5. **Ollama for LLM** - Local, free, no API keys
6. **Streamlit for UI** - Easy, Python-only web interface

---

## 📚 Technical Terms to Know

- **RAG**: Retrieval-Augmented Generation
- **Embedding**: Vector representation of text
- **FAISS**: Facebook AI Similarity Search
- **Chunking**: Splitting text into smaller pieces
- **Vector Similarity**: Finding similar text using embeddings
- **Agentic**: AI that makes decisions autonomously
- **LLM**: Large Language Model
- **Ollama**: Local LLM inference framework

---

## 🚀 Quick Demo Points

1. Show PDF upload and index building
2. Demonstrate RAG mode with PDF question
3. Show Direct mode with general question
4. Demonstrate Auto mode (agentic decision)
5. Show retrieved contexts
6. Explain the architecture

---

**Good Luck with your Viva! 🎓**

