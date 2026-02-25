# 🤖 Agentic Features - RAG vs Direct Generative AI

## 🎯 New Features Added:

### 1. **Agentic Decision Making**
- AI automatically decides whether to use RAG (PDF context) or Direct Generation
- Intelligent analysis of questions
- Keyword-based + LLM-based decision making

### 2. **Mode Toggle Button** 🔄
Three modes available:

#### 🤖 **Auto Mode (Agentic)**
- AI decides the best approach
- Uses RAG if question needs PDF context
- Uses Direct AI if general knowledge question
- Most intelligent and flexible

#### 📄 **RAG Mode (PDF-based)**
- Always uses PDF document context
- Retrieves relevant chunks from saved index
- Best for questions about the uploaded PDF
- Requires index to be built first

#### ✨ **Direct Mode (Generative AI)**
- Uses general AI knowledge only
- No PDF context needed
- Works even without index
- Best for general questions

## 🚀 How It Works:

### Agentic Flow:

```
User Question
    ↓
🤖 AI Analyzes Question
    ↓
    ├─→ Needs PDF? → 📄 RAG Mode
    │                  ↓
    │              Retrieve from Index
    │                  ↓
    │              Generate Answer
    │
    └─→ General Knowledge? → ✨ Direct Mode
                              ↓
                          Generate Answer
```

### Code Structure:

```
src/agentic_engine.py
├── AgenticEngine class
│   ├── should_use_rag() - Decision making
│   ├── process_rag_query() - RAG processing
│   ├── process_direct_query() - Direct AI
│   └── process_query() - Main entry point
```

## 💡 Usage Examples:

### Auto Mode (Recommended):
```
Question: "What is Shoolini University?"
→ AI decides: Needs PDF → Uses RAG Mode

Question: "What is the capital of France?"
→ AI decides: General knowledge → Uses Direct Mode
```

### RAG Mode:
```
Question: "Tell me about the courses offered"
→ Always uses PDF context
→ Shows retrieved contexts
```

### Direct Mode:
```
Question: "Explain quantum computing"
→ Uses general AI knowledge
→ No PDF needed
```

## 🎨 UI Features:

1. **Mode Toggle** in sidebar
   - Radio buttons for easy switching
   - Real-time mode indicator
   - Mode descriptions

2. **Mode Badges** in chat
   - Shows which mode was used
   - Visual indicators (📄 for RAG, ✨ for Direct)

3. **Context Display**
   - Expandable context sections
   - Shows retrieved chunks in RAG mode
   - Context count display

## 🔧 Technical Details:

### Agentic Decision Logic:

1. **Keyword Analysis**: Checks for PDF-related keywords
2. **LLM Decision**: Uses Ollama to analyze question intent
3. **Fallback**: Uses keyword-based decision if LLM fails

### RAG Processing:
- Retrieves top-k relevant chunks
- Constructs context-aware prompt
- Generates answer with PDF context

### Direct Processing:
- Uses system prompt for general knowledge
- No retrieval needed
- Faster response time

## 📊 Benefits:

✅ **Intelligent**: AI decides the best approach  
✅ **Flexible**: Switch modes anytime  
✅ **Efficient**: Uses RAG only when needed  
✅ **User-friendly**: Clear mode indicators  
✅ **Fast**: Direct mode for quick general questions  

## 🎯 Use Cases:

- **Auto Mode**: Best for mixed questions
- **RAG Mode**: Document-specific queries
- **Direct Mode**: General knowledge, coding help, explanations

## 🔄 Switching Modes:

1. Go to sidebar
2. Select desired mode from radio buttons
3. Mode changes immediately
4. Next question uses selected mode

---

**Powered by Local Ollama** - All processing happens locally! 🚀

