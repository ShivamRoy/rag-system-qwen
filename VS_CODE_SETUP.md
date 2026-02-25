# 🎨 VS Code में Project चलाने के लिए

## VS Code Terminal में Activate करें:

### Method 1: VS Code Integrated Terminal

1. **VS Code में Terminal खोलें:**
   - `Ctrl + `` (backtick) या
   - Menu: `Terminal` → `New Terminal`

2. **Terminal में ये command run करें:**
   ```bash
   source .venv/bin/activate
   ```

3. **Check करें** - prompt में `(.venv)` दिखेगा:
   ```bash
   (.venv) shivamtomar@Shivams-MacBook-Pro rag-qwen % 
   ```

4. **Project run करें:**
   ```bash
   streamlit run app.py
   ```

### Method 2: VS Code Python Interpreter Select करें

1. **VS Code में:**
   - `Cmd + Shift + P` (Mac) या `Ctrl + Shift + P` (Windows/Linux)
   - Type: `Python: Select Interpreter`
   - Select: `.venv/bin/python` या `venv/bin/python`

2. **अब VS Code automatically virtual environment use करेगा**

## VS Code में Run करने के तरीके:

### Option A: Terminal से (Recommended)

```bash
# Terminal में (VS Code bottom panel)
source .venv/bin/activate
streamlit run app.py
```

### Option B: VS Code Run Configuration

`.vscode/launch.json` file बनाएं (अगर नहीं है):

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Streamlit App",
            "type": "python",
            "request": "launch",
            "module": "streamlit",
            "args": [
                "run",
                "app.py"
            ],
            "console": "integratedTerminal",
            "justMyCode": true
        }
    ]
}
```

फिर `F5` दबाएं या Run button click करें।

### Option C: VS Code Tasks

`.vscode/tasks.json` file बनाएं:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Run Streamlit",
            "type": "shell",
            "command": "${workspaceFolder}/.venv/bin/streamlit",
            "args": ["run", "app.py"],
            "problemMatcher": []
        }
    ]
}
```

## Quick Commands for VS Code Terminal:

```bash
# Activate और run (one-liner)
source .venv/bin/activate && streamlit run app.py

# या step by step
source .venv/bin/activate
streamlit run app.py
```

## VS Code Tips:

1. **Terminal automatically project folder में खुलेगा**
2. **Multiple terminals** open कर सकते हैं (`+` button)
3. **Terminal split** कर सकते हैं (right-click → Split Terminal)

## Troubleshooting:

### अगर `.venv` नहीं दिख रहा:
```bash
# VS Code terminal में
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### अगर Python interpreter select नहीं हो रहा:
- `Cmd/Ctrl + Shift + P` → `Python: Select Interpreter`
- `.venv/bin/python` select करें

### VS Code में terminal path check करें:
```bash
pwd  # Should show: /Users/shivamtomar/Code/rag-qwen
```

