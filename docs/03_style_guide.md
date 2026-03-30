# Style Guide

All code in this repository (exercises and `src/mds/`) must follow these conventions.
They are based on PEP 8, with a few MDS-specific additions.

---

## Naming

| Kind | Convention | Example |
|---|---|---|
| Functions & methods | `snake_case` | `build_name()`, `get_selection()` |
| Variables | `snake_case` | `scene_name`, `node_list` |
| Classes | `PascalCase` | `SceneValidator`, `BaseWindow` |
| Constants (module-level) | `UPPER_SNAKE_CASE` | `DEFAULT_VERSION`, `SEQ_TOKEN` |
| Private / internal | leading underscore | `_parse_internal()` |
| Files & modules | `snake_case` | `naming.py`, `base_window.py` |

Never use abbreviations unless they are universally understood (e.g. `obj`, `idx`, `num`).

---

## Docstrings

Use **Google style** docstrings. Every public function, class, and module must have one.

```python
def build_name(prefix: str, descriptor: str, index: int) -> str:
    """Build a standardised asset name.

    Args:
        prefix: Short category token, e.g. "geo".
        descriptor: Human-readable descriptor, e.g. "sphere".
        index: One-based integer index.

    Returns:
        Formatted name string, e.g. "geo_sphere_001".

    Raises:
        ValueError: If prefix or descriptor do not match VALID_NAME_PATTERN.
    """
```

---

## Type Hints

Type hints are optional but strongly encouraged. Use them for all public function
signatures:

```python
def parse_version(version_str: str) -> int: ...
def next_version(existing_versions: list[str]) -> str: ...
```

For Python 3.10+ union syntax use `X | Y` rather than `Optional[X]`:
```python
def read_json_safe(path: Path | str, default: dict | None = None) -> dict: ...
```

---

## Line Length

Maximum **88 characters** per line (compatible with the Black formatter).
VS Code is configured to show a ruler at column 88.

---

## Imports

Order imports in three groups, separated by blank lines, alphabetically within each group:

```python
# 1. Standard library
import os
import re
from pathlib import Path

# 2. Third-party
import pytest

# 3. Local / project
from mds import config
from mds.naming import build_name
```

Never use wildcard imports (`from module import *`).

---

## Error Handling

- **Never use a bare `except:`** clause. Always catch a specific exception or at minimum
  `Exception`.
- Provide a helpful message when raising:
  ```python
  raise ValueError(f"Invalid name '{name}': must match {VALID_NAME_PATTERN}")
  ```
- Use guarded imports (`try/except ImportError`) when a dependency (Maya, PySide) may
  not be present. See `src/mds/maya/scene.py` for the canonical pattern.

---

## Miscellaneous

- Prefer `pathlib.Path` over `os.path` string manipulation.
- Use f-strings for formatting; avoid `%` and `.format()` where an f-string is clearer.
- Keep functions short and focused: if a function is longer than ~30 lines, consider
  splitting it.
