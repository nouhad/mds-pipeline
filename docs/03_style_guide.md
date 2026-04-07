# Style Guide

All code in this repo (exercises and `src/mds/`) follows PEP 8 with these additions.

## Naming

- Functions, methods, variables, files: `snake_case` — e.g. `build_name()`, `scene_name`, `naming.py`
- Classes: `PascalCase` — e.g. `SceneValidator`, `BaseWindow`
- Module-level constants: `UPPER_SNAKE_CASE` — e.g. `DEFAULT_VERSION`, `SEQ_TOKEN`
- Private/internal: leading underscore — e.g. `_parse_internal()`

Avoid abbreviations unless universally understood (`obj`, `idx`, `num` are fine).

## Docstrings

Use Google-style docstrings. Every public function, class, and module must have one.

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

## Type Hints

Use type hints on all public function signatures:

```python
def parse_version(version_str: str) -> int: ...
def next_version(existing_versions: list[str]) -> str: ...
def read_json_safe(path: Path | str, default: dict | None = None) -> dict: ...
```

Use `X | Y` over `Optional[X]` (Python 3.10+).

## Line Length

Maximum 88 characters. VS Code shows a ruler at column 88.

## Imports

Three groups, blank line between each, alphabetical within each:

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

No wildcard imports (`from module import *`).

## Error Handling

Never use a bare `except:`. Always catch a specific exception. Provide a clear message:

```python
raise ValueError(f"Invalid name '{name}': must match {VALID_NAME_PATTERN}")
```

Use guarded imports (`try/except ImportError`) for optional dependencies like Maya or PySide. See `src/mds/maya/scene.py` for the pattern.

## Miscellaneous

- Use `pathlib.Path` over `os.path`.
- Use f-strings for formatting.
- Keep functions under ~30 lines. Split if they grow longer.