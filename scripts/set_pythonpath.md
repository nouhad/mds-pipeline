# Setting PYTHONPATH

## Why Is This Needed?

Python finds packages by searching the directories listed in `sys.path`. The `mds`
package lives inside `src/mds/`, which is **not** on the path by default. You must add
`src/` to `PYTHONPATH` so that `import mds` works without installing the package.

---

## Linux / macOS

Run once per terminal session:
```bash
export PYTHONPATH="$PWD/src:$PYTHONPATH"
```

To make it permanent, add it to `~/.bashrc` (Bash) or `~/.zshrc` (Zsh):
```bash
echo 'export PYTHONPATH="$HOME/projects/mds-pipeline/src:$PYTHONPATH"' >> ~/.zshrc
source ~/.zshrc
```

---

## Windows – Command Prompt (cmd)

```cmd
set PYTHONPATH=%CD%\src;%PYTHONPATH%
```

To make it permanent, set it via **System Properties → Environment Variables**.

---

## Windows – PowerShell

```powershell
$env:PYTHONPATH = "src;" + $env:PYTHONPATH
```

For persistence across sessions, add to your PowerShell profile:
```powershell
notepad $PROFILE
# Add this line:
# $env:PYTHONPATH = "C:\path\to\mds-pipeline\src;" + $env:PYTHONPATH
```

---

## VS Code

VS Code is already configured – no extra steps needed. The setting
`"python.analysis.extraPaths": ["src"]` in `.vscode/settings.json` tells Pylance
about the `src/` directory, and the pytest configuration passes `PYTHONPATH=src`
automatically via the CI workflow.

If tests aren't being discovered, ensure you have the **ms-python.python** extension
installed and a Python interpreter selected (bottom-left status bar in VS Code).

---

## Maya – `userSetup.py`

Add the following to your `userSetup.py` (runs once when Maya starts):

```python
import sys

# Change this path to wherever you cloned the repo:
repo_src = r"C:\Users\you\projects\mds-pipeline\src"

if repo_src not in sys.path:
    sys.path.insert(0, repo_src)
```

File locations:
- **Windows**: `C:\Users\<you>\Documents\maya\scripts\userSetup.py`
- **macOS**: `~/Library/Preferences/Autodesk/maya/scripts/userSetup.py`
- **Linux**: `~/maya/scripts/userSetup.py`

Restart Maya after editing `userSetup.py`.

---

## Verifying the Setup

In any Python environment (terminal, Maya Script Editor, VS Code terminal):

```python
import mds
print(mds.__version__)  # Should print: 0.1.0
```
