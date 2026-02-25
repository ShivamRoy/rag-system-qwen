# ✅ सही तरीका - Virtual Environment Activate करने के लिए

## ⚠️ Important:
`source` command **Python में नहीं, Terminal में** run करना है!

## Steps:

### 1. Python से बाहर निकलें:
```python
>>> exit()
```
या `Ctrl+D` दबाएं

### 2. Terminal में activate करें:

**अगर `.venv` use कर रहे हैं:**
```bash
source .venv/bin/activate
```

**या अगर `venv` use कर रहे हैं:**
```bash
source venv/bin/activate
```

### 3. Check करें:
```bash
which python3
# Should show: /Users/shivamtomar/Code/rag-qwen/.venv/bin/python3
```

## Complete Example:

```bash
# Terminal में (Python नहीं!)
shivamtomar@Shivams-MacBook-Pro rag-qwen % source .venv/bin/activate

# अब prompt बदल जाएगा:
(.venv) shivamtomar@Shivams-MacBook-Pro rag-qwen % 

# अब project run करें:
(.venv) shivamtomar@Shivams-MacBook-Pro rag-qwen % streamlit run app.py
```

## Quick Commands:

```bash
# .venv के लिए:
source .venv/bin/activate && streamlit run app.py

# venv के लिए:
source venv/bin/activate && streamlit run app.py
```

## Difference:

- **Python Interpreter (`>>>`)**: Python code run करने के लिए
- **Terminal/Shell (`%` या `$`)**: Commands run करने के लिए

`source` एक **shell command** है, Python command नहीं!

