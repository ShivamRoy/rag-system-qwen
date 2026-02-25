#!/usr/bin/env python3
"""
Quick test script to verify project setup
"""
import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("🔍 Testing imports...")
    missing = []
    
    try:
        import sentence_transformers
        print("  ✅ sentence-transformers")
    except ImportError:
        print("  ❌ sentence-transformers - MISSING")
        missing.append("sentence-transformers")
    
    try:
        import faiss
        print("  ✅ faiss-cpu")
    except ImportError:
        print("  ❌ faiss-cpu - MISSING")
        missing.append("faiss-cpu")
    
    try:
        import langchain
        print("  ✅ langchain")
    except ImportError:
        print("  ❌ langchain - MISSING")
        missing.append("langchain")
    
    try:
        import fitz
        print("  ✅ PyMuPDF")
    except ImportError:
        print("  ❌ PyMuPDF - MISSING")
        missing.append("PyMuPDF")
    
    try:
        import streamlit
        print("  ✅ streamlit")
    except ImportError:
        print("  ⚠️  streamlit - MISSING (optional for web UI)")
        missing.append("streamlit (optional)")
    
    return missing

def test_files():
    """Test if required files exist"""
    print("\n📁 Testing files...")
    
    files_to_check = [
        ("data/About Shoolini University.pdf", "PDF file"),
        ("embeddings/faiss.index", "FAISS index"),
        ("embeddings/meta.pkl", "Metadata file"),
        ("src/load_pdf.py", "Load PDF module"),
        ("src/chunk_text.py", "Chunk text module"),
        ("src/embed_store.py", "Embed store module"),
        ("src/query_engine.py", "Query engine module"),
    ]
    
    missing_files = []
    for filepath, desc in files_to_check:
        if os.path.exists(filepath):
            print(f"  ✅ {desc}: {filepath}")
        else:
            print(f"  ❌ {desc}: {filepath} - MISSING")
            missing_files.append(filepath)
    
    return missing_files

def test_ollama():
    """Test if Ollama is available"""
    print("\n🤖 Testing Ollama...")
    import subprocess
    try:
        result = subprocess.run(["ollama", "list"], 
                              capture_output=True, 
                              text=True, 
                              timeout=5)
        if result.returncode == 0:
            if "qwen" in result.stdout.lower():
                print("  ✅ Ollama is installed and Qwen model found")
                return True
            else:
                print("  ⚠️  Ollama installed but Qwen model not found")
                print("     Run: ollama pull qwen:latest")
                return False
        else:
            print("  ❌ Ollama command failed")
            return False
    except FileNotFoundError:
        print("  ❌ Ollama not found in PATH")
        return False
    except Exception as e:
        print(f"  ❌ Error checking Ollama: {e}")
        return False

def main():
    print("=" * 50)
    print("🧪 RAG Project Test Script")
    print("=" * 50)
    
    missing_modules = test_imports()
    missing_files = test_files()
    ollama_ok = test_ollama()
    
    print("\n" + "=" * 50)
    print("📊 Summary")
    print("=" * 50)
    
    if missing_modules:
        print(f"\n❌ Missing {len(missing_modules)} module(s)")
        print("   Install with:")
        print("   python3 -m pip install --user -r requirements.txt")
        print("   OR")
        print("   python3 -m pip install --user " + " ".join([m for m in missing_modules if m != "streamlit (optional)"]))
    else:
        print("\n✅ All required modules installed!")
    
    if missing_files:
        print(f"\n❌ Missing {len(missing_files)} file(s)")
        print("   Some files may need to be created or downloaded")
    else:
        print("\n✅ All required files present!")
    
    if not ollama_ok:
        print("\n⚠️  Ollama setup needed")
        print("   Install from: https://ollama.ai")
        print("   Then run: ollama pull qwen:latest")
    else:
        print("\n✅ Ollama ready!")
    
    print("\n" + "=" * 50)
    
    if not missing_modules and not missing_files and ollama_ok:
        print("🎉 Project is ready to run!")
        print("\nTo run:")
        print("  Command line: python3 main.py")
        print("  Web UI:      streamlit run app.py")
        return 0
    else:
        print("⚠️  Some setup needed before running")
        return 1

if __name__ == "__main__":
    sys.exit(main())

