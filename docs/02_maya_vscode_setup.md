# Maya + VS Code Setup

Maya's Script Editor is fine for one-liners but lacks autocomplete, type checking, Git integration, and a real debugger. Write your code in VS Code and send it to Maya via one of the methods below.

## Setting PYTHONPATH in Maya

Maya has its own Python interpreter. Add your `src/` path to `userSetup.py` so `import mds` works.

Find or create `userSetup.py`:
- Windows: `C:\Users\<you>\Documents\maya\scripts\userSetup.py`
- macOS: `~/Library/Preferences/Autodesk/maya/scripts/userSetup.py`
- Linux: `~/maya/scripts/userSetup.py`

Add:
```python
import sys
repo_src = r"C:\path\to\mds-pipeline\src"   # adjust to your path
if repo_src not in sys.path:
    sys.path.insert(0, repo_src)
```

Restart Maya and verify:
```python
import mds
print(mds.__version__)   # should print "0.1.0"
```

## Method 1 – Copy/Paste

Write your script in VS Code, copy it, paste into Maya's Script Editor (Python tab), and press `Ctrl+Enter`. No setup required, but manual.

## Method 2 – Command Port

Add to `userSetup.mel` to open a port on startup:
```mel
commandPort -name "localhost:7001" -sourceType "python" -echoOutput;
```

Then install the **MayaCode** VS Code extension, point it at `localhost:7001`, and use its keybinding to send code directly from VS Code to Maya. See `scripts/run_in_maya.py` for a socket-based alternative. Requires Maya running locally with the port open.

## Maya 2024 / 2025 Notes

Maya 2024 uses Python 3.10 and PySide2. Maya 2025+ uses Python 3.11 and PySide6. The `mds.ui` module handles the PySide version difference with a fallback import. The `maya.cmds` API is the same across both.