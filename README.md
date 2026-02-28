# Privacy-First Document Intelligence System

This project is a Retrieval-Augmented Generation (RAG) based AI system designed to answer questions from PDFs using local LLMs. The focus is on privacy, scalability, and enterprise-grade workflows aligned with European compliance standards (GDPR).

## 🚀 Features
- PDF ingestion and text extraction
- Chunking and embedding
- Vector search using FAISS
- Local inference using Ollama
- Privacy-first architecture
- Supports multiple document types
- Designed for enterprise use cases such as finance, legal, and compliance

## 🧠 Architecture
1. PDF ingestion
2. Text chunking
3. Embedding generation
4. Vector database indexing
5. Semantic retrieval
6. Context-aware LLM response

## 💡 Use Cases
- Contract and invoice analysis
- Knowledge management
- Customer support automation
- Compliance and audit workflows

## ⚙️ Tech Stack
- Python
- FastAPI
- FAISS
- Ollama
- Local LLMs

## 🔐 Why Local LLM?
This system avoids sending sensitive data to external APIs, making it suitable for enterprise and European environments.

## 📌 Future Improvements
- Hybrid search
- Reranking
- Observability and monitoring
- Async processing
- Scalable deployments


# RAG System with Qwen LLM

A Retrieval-Augmented Generation (RAG) system that uses Qwen model via Ollama to answer questions from PDF documents.

## 🎯 Project Overview

This project implements a complete RAG pipeline:
1. **PDF Loading**: Extracts text from PDF files
2. **Text Chunking**: Splits text into manageable chunks
3. **Embedding Generation**: Creates vector embeddings using sentence-transformers
4. **Vector Storage**: Stores embeddings in FAISS index
5. **Retrieval**: Finds relevant chunks for user queries
6. **Generation**: Uses Qwen LLM to generate answers based on retrieved context

## 📋 Prerequisites

- Python 3.8+
- Ollama installed and running
- Qwen model downloaded in Ollama: `ollama pull qwen:0.5b`

## 🚀 Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install and setup Ollama:**
   ```bash
   # Download Ollama from https://ollama.ai
   # Pull the Qwen model
   ollama pull qwen:0.5b
   ```

3. **Place your PDF file in the `data/` directory**

## 💻 Usage

### Option 1: Web Interface (Recommended) 🌐

Run the Streamlit web app:
```bash
streamlit run app.py
```

The web interface provides:
- 📄 PDF upload functionality
- 🔨 Index building with progress indicators
- 💬 Interactive chat interface
- 📊 View retrieved contexts
- 🎨 Beautiful, user-friendly UI

Open your browser to `http://localhost:8501` after running the command.

### Option 2: Command Line

Run the main script:
```bash
python main.py
```

The script will:
- Automatically build the index if it doesn't exist
- Prompt you to ask a question about the PDF
- Return an answer based on the document content

## 📁 Project Structure

```
rag-qwen/
├── data/              # PDF files
├── embeddings/        # FAISS index and metadata
├── src/
│   ├── load_pdf.py    # PDF text extraction
│   ├── chunk_text.py  # Text chunking
│   ├── embed_store.py # Embedding generation & storage
│   ├── query_engine.py # Query retrieval & LLM interaction
│   └── utils.py       # Utility functions
├── app.py             # Streamlit web interface
├── main.py            # Command-line entry point
└── requirements.txt   # Dependencies
```

## 🔧 Key Technologies

- **sentence-transformers**: For generating embeddings
- **FAISS**: Vector similarity search
- **Ollama**: Local LLM inference
- **Qwen**: Lightweight generative model
- **LangChain**: Text splitting utilities
- **Streamlit**: Web interface framework

## 📝 Notes

- First run will take time to build the index
- Ensure Ollama is running before querying
- The model `qwen:0.5b` is a small model suitable for local inference

