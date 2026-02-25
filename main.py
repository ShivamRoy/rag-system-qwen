# main.py
import os
from src.load_pdf import extract_text_from_pdf
from src.chunk_text import chunk_text
from src.embed_store import create_index_from_text_chunks
from src.query_engine import retrieve_top_k, construct_prompt, run_ollama

def build_index(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    print(f"📄 Loading PDF: {pdf_path}")
    text = extract_text_from_pdf(pdf_path)
    print(f"✅ Extracted {len(text)} characters")
    
    print("🔪 Chunking text...")
    chunks = chunk_text(text)
    print(f"✅ Created {len(chunks)} chunks")
    
    print("💾 Creating embeddings and saving index...")
    create_index_from_text_chunks(chunks)
    print("✅ Index created successfully!")

def query_system(query):
    if not os.path.exists("embeddings/faiss.index"):
        raise FileNotFoundError("Index not found! Please run build_index() first.")
    
    print(f"🔍 Searching for: {query}")
    contexts = retrieve_top_k(query)
    prompt = construct_prompt(contexts, query)
    response = run_ollama(prompt)
    print("\n📌 Answer:")
    print(response)

if __name__ == "__main__":
    # Check if index exists, if not build it
    if not os.path.exists("embeddings/faiss.index"):
        print("⚠️  Index not found. Building index...")
        build_index("data/About Shoolini University.pdf")
    
    # Ask your question
    user_query = input("\n❓ Ask a question about the PDF: ")
    query_system(user_query)
