"""Reference script: running repo code from inside Maya.

Copy the relevant sections into Maya's Script Editor (Python tab) or add them
to your userSetup.py. Adjust the repo path to match your local installation.

This is a reference/template – it is not meant to be run directly from the
command line.
"""

# ---------------------------------------------------------------------------
# Step 1 – Make the src/ directory visible to Maya's Python interpreter.
# ---------------------------------------------------------------------------

import sys

# Change this to the absolute path of the mds-pipeline/src folder on your machine.
REPO_SRC = r"C:\Users\you\projects\mds-pipeline\src"  # Windows example
# REPO_SRC = "/Users/you/projects/mds-pipeline/src"   # macOS / Linux example

if REPO_SRC not in sys.path:
    sys.path.insert(0, REPO_SRC)

# ---------------------------------------------------------------------------
# Step 2 – Import the mds modules you need.
# ---------------------------------------------------------------------------

from mds.maya import scene  # noqa: E402  (after sys.path setup)
from mds import naming       # noqa: E402

# ---------------------------------------------------------------------------
# Step 3 – Use them safely inside a try/except block.
# ---------------------------------------------------------------------------

try:
    scene_name = scene.get_scene_name()
    print(f"Current scene: {scene_name or '(unsaved)'}")

    selected = scene.get_selection()
    print(f"Selected objects ({len(selected)}):")
    for obj in selected:
        print(f"  - {obj}")

except Exception as exc:
    # Always guard Maya code so a crash in your tool doesn't break the scene.
    print(f"Error: {exc}")
    raise

# ---------------------------------------------------------------------------
# Notes
# ---------------------------------------------------------------------------
# - Never use a bare 'except:' without specifying the exception type.
# - Use cmds.undoInfo(openChunk=True) / closeChunk=True) to make batched
#   operations undoable with a single Ctrl+Z.
# - Test your logic outside Maya first using the pytest test suite.
