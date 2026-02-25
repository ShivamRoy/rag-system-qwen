import streamlit as st
import os
from src.load_pdf import extract_text_from_pdf
from src.chunk_text import chunk_text
from src.embed_store import create_index_from_text_chunks
from src.query_engine import retrieve_top_k, construct_prompt, run_ollama
from src.agentic_engine import AgenticEngine

# Page configuration
st.set_page_config(
    page_title="RAG Q&A System",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
    }
    .answer-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'index_built' not in st.session_state:
    st.session_state.index_built = os.path.exists("embeddings/faiss.index")
if 'query_mode' not in st.session_state:
    st.session_state.query_mode = "auto"  # "auto", "rag", "direct"
if 'agentic_engine' not in st.session_state:
    st.session_state.agentic_engine = AgenticEngine()

# Header
st.markdown('<p class="main-header">🤖 Agentic RAG Q&A System</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Intelligent AI that switches between PDF-based RAG and Direct Generation</p>', unsafe_allow_html=True)

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Check index status
    if st.session_state.index_built:
        st.success("✅ Index is ready!")
    else:
        st.warning("⚠️ Index not found")
    
    st.divider()
    
    # Build index section
    st.subheader("📚 Build Index")
    
    # Default PDF path
    default_pdf = "data/About Shoolini University.pdf"
    
    if st.button("🔨 Build Index from Default PDF"):
        if os.path.exists(default_pdf):
            with st.spinner("Building index... This may take a few minutes."):
                try:
                    text = extract_text_from_pdf(default_pdf)
                    chunks = chunk_text(text)
                    create_index_from_text_chunks(chunks)
                    st.session_state.index_built = True
                    st.success(f"✅ Index built successfully! Created {len(chunks)} chunks.")
                    st.rerun()
                except Exception as e:
                    st.error(f"Error building index: {str(e)}")
        else:
            st.error(f"PDF file not found: {default_pdf}")
    
    # Upload new PDF
    st.divider()
    st.subheader("📄 Upload New PDF")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Save uploaded file
        upload_path = f"data/{uploaded_file.name}"
        os.makedirs("data", exist_ok=True)
        
        with open(upload_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        if st.button(f"🔨 Build Index from {uploaded_file.name}"):
            with st.spinner("Building index... This may take a few minutes."):
                try:
                    text = extract_text_from_pdf(upload_path)
                    chunks = chunk_text(text)
                    create_index_from_text_chunks(chunks)
                    st.session_state.index_built = True
                    st.success(f"✅ Index built successfully! Created {len(chunks)} chunks.")
                    st.rerun()
                except Exception as e:
                    st.error(f"Error building index: {str(e)}")
    
    st.divider()
    
    # Query Mode Toggle
    st.subheader("🔄 Query Mode")
    mode_options = {
        "auto": "🤖 Auto (Agentic Decision)",
        "rag": "📄 RAG (PDF-based)",
        "direct": "✨ Direct Generative AI"
    }
    
    selected_mode = st.radio(
        "Select query mode:",
        options=list(mode_options.keys()),
        format_func=lambda x: mode_options[x],
        index=list(mode_options.keys()).index(st.session_state.query_mode) if st.session_state.query_mode in mode_options else 0,
        key="mode_selector"
    )
    st.session_state.query_mode = selected_mode
    
    # Mode descriptions
    if selected_mode == "auto":
        st.info("🤖 **Auto Mode**: AI decides whether to use PDF context or general knowledge")
    elif selected_mode == "rag":
        st.info("📄 **RAG Mode**: Always uses PDF document context for answers")
    else:
        st.info("✨ **Direct Mode**: Uses general AI knowledge (no PDF context)")
    
    st.divider()
    st.info("💡 **Tip:** Build the index first before asking questions in RAG mode!")

# Main content area
# Check if RAG mode needs index
if st.session_state.query_mode == "rag" and not st.session_state.index_built:
    st.warning("⚠️ RAG mode requires index! Please build the index first using the sidebar.")
    st.info("""
    **Steps to get started:**
    1. Go to the sidebar on the left
    2. Click "Build Index from Default PDF" or upload a new PDF
    3. Wait for the index to be created
    4. Start asking questions!
    """)
else:
    # Mode indicator
    mode_display = {
        "auto": "🤖 Auto Mode (Agentic)",
        "rag": "📄 RAG Mode (PDF-based)",
        "direct": "✨ Direct Mode (Generative AI)"
    }
    st.info(f"**Current Mode:** {mode_display[st.session_state.query_mode]}")
    
    # Chat interface
    st.subheader("💬 Ask Questions")
    
    # Display chat history with mode indicators
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if "mode" in message:
                mode_badge = {
                    "RAG": "📄",
                    "Direct Generative AI": "✨"
                }
                st.caption(f"{mode_badge.get(message['mode'], '🤖')} {message['mode']}")
            st.markdown(message["content"])
            if "contexts" in message and message["contexts"]:
                with st.expander(f"📄 Retrieved Contexts ({len(message['contexts'])} found)", expanded=False):
                    for i, ctx in enumerate(message["contexts"], 1):
                        st.markdown(f"**Context {i}:**")
                        st.text(ctx[:200] + "..." if len(ctx) > 200 else ctx)
                        st.divider()
    
    # Question input
    placeholder_text = {
        "auto": "Ask any question (AI will decide the best approach)...",
        "rag": "Ask a question about the PDF...",
        "direct": "Ask any question (using general AI knowledge)..."
    }
    
    if prompt := st.chat_input(placeholder_text[st.session_state.query_mode]):
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get answer using agentic engine
        with st.chat_message("assistant"):
            spinner_text = {
                "auto": "🤖 Analyzing and generating answer...",
                "rag": "🔍 Searching PDF and generating answer...",
                "direct": "✨ Generating answer with AI..."
            }
            
            with st.spinner(spinner_text[st.session_state.query_mode]):
                try:
                    # Process query with agentic engine
                    force_mode = None if st.session_state.query_mode == "auto" else st.session_state.query_mode
                    result = st.session_state.agentic_engine.process_query(prompt, force_mode=force_mode)
                    
                    # Display mode badge
                    mode_badge = {
                        "RAG": "📄",
                        "Direct Generative AI": "✨"
                    }
                    st.caption(f"{mode_badge.get(result['mode'], '🤖')} **{result['mode']}**")
                    
                    # Show contexts if RAG mode
                    if result["contexts"]:
                        with st.expander(f"📄 Retrieved Contexts ({result['context_count']} found)", expanded=False):
                            for i, ctx in enumerate(result["contexts"], 1):
                                st.markdown(f"**Context {i}:**")
                                st.text(ctx[:200] + "..." if len(ctx) > 200 else ctx)
                                st.divider()
                    
                    # Display answer
                    st.markdown(result["response"])
                    
                    # Add to history with metadata
                    message_data = {
                        "role": "assistant",
                        "content": result["response"],
                        "mode": result["mode"],
                        "contexts": result["contexts"]
                    }
                    st.session_state.messages.append(message_data)
                    
                except Exception as e:
                    error_msg = f"❌ Error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})
    
    # Clear chat button
    if st.session_state.messages:
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            st.rerun()

