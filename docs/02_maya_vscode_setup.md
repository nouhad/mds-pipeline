# Maya + VS Code Setup

## Why VS Code Instead of Maya's Script Editor?

Maya's built-in Script Editor is fine for quick one-liners, but it lacks:
- Proper autocomplete and type checking
- Git integration
- Multi-file navigation and refactoring
- A real debugger

For anything beyond a few lines, write your code in VS Code, keep it in this repo,
and send it to Maya via one of the methods below.

---

## Setting PYTHONPATH So Maya Sees `src/`

Maya uses its own embedded Python interpreter. You need to tell it where your `src/`
folder lives so that `import mds` works.

### In `userSetup.py` (runs every time Maya starts)

Find or create `userSetup.py`:
- **Windows**: `C:\Users\<you>\Documents\maya\scripts\userSetup.py`
- **macOS**: `~/Library/Preferences/Autodesk/maya/scripts/userSetup.py`
- **Linux**: `~/maya/scripts/userSetup.py`

Add:
```python
import sys
import os

repo_src = r"C:\path\to\mds-pipeline\src"   # adjust to your path
if repo_src not in sys.path:
    sys.path.insert(0, repo_src)
```

After saving, restart Maya and test with:
```python
import mds
print(mds.__version__)   # should print "0.1.0"
```

---

## Method 1 – Script Editor Copy/Paste (Simple, No Setup)

1. Write your script in VS Code.
2. Select all (`Ctrl+A` / `Cmd+A`), copy.
3. Paste into Maya's Script Editor (Python tab).
4. Press `Ctrl+Enter` to run.

**Pros**: zero setup, always works.
**Cons**: manual, no live reload.

---

## Method 2 – Command Port (Advanced)

This lets you send code from VS Code directly to a running Maya session.

### Step 1 – Open a command port in Maya

Add to `userSetup.mel`:
```mel
// Open a Python command port on localhost:7001
commandPort -name "localhost:7001" -sourceType "python" -echoOutput;
```

Or run it once in Maya's MEL Script Editor:
```mel
commandPort -name "localhost:7001" -sourceType "python" -echoOutput;
```

### Step 2 – Send code from VS Code

Install the VS Code extension **"MayaCode"** (or similar). Configure it to connect to
`localhost:7001`. You can then press a keybinding to send the current file or selection
to Maya.

Alternatively, use the helper script `scripts/run_in_maya.py` as a reference for
socket-based execution.

**Pros**: live workflow, no copy/paste.
**Cons**: requires Maya to be running locally; port must be open.

---

## Maya 2024 / 2025 Python 3 Compatibility Notes

| Maya Version | Python Version | PySide Version |
|---|---|---|
| Maya 2024 | Python 3.10 | PySide2 |
| Maya 2025+ | Python 3.11 | PySide6 |

Key differences:
- `maya.cmds` API is the same across both versions.
- UI code using PySide2 may need minor changes for PySide6 (e.g. `exec_()` → `exec()`).
- The `mds.ui` module handles this automatically with a fallback import chain.
- String types: everything is `str` (unicode) in Python 3 – no `unicode` vs `str` confusion.
- Use `from __future__ import annotations` if you need forward references in type hints.
