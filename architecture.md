# System Architecture

This project is a privacy-first Retrieval-Augmented Generation (RAG) system designed for answering questions from enterprise documents.

## High-level Flow

1. User uploads a PDF document.
2. The system extracts text from the document.
3. The text is split into smaller chunks.
4. Each chunk is converted into vector embeddings.
5. Embeddings are stored in a FAISS vector database.
6. When a user asks a question:
   - The query is embedded.
   - Relevant chunks are retrieved from the vector database.
   - Retrieved context is passed to a local LLM.
   - The LLM generates an accurate and context-aware response.

## Key Design Goals
- Privacy-first architecture
- Local LLM inference
- Scalable and modular backend
- Enterprise-ready document intelligence