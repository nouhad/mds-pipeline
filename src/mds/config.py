"""Pipeline-wide constants for the MDS shared library.

Import this module rather than hardcoding strings or paths elsewhere in the codebase.
"""

import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Naming validation
# ---------------------------------------------------------------------------

VALID_NAME_PATTERN: str = r"^[a-z][a-z0-9_]*$"
"""Names must start with a lowercase letter and contain only lowercase
alphanumeric characters and underscores."""

_VALID_NAME_RE = re.compile(VALID_NAME_PATTERN)

# ---------------------------------------------------------------------------
# Project root
# ---------------------------------------------------------------------------

DEFAULT_PROJECT_ROOT: Path = Path.home() / "projects" / "mds"
"""Default filesystem root for all MDS projects.

Override at runtime by setting the MDS_PROJECT_ROOT environment variable.
"""

# ---------------------------------------------------------------------------
# Sequence / shot tokens
# ---------------------------------------------------------------------------

SEQ_TOKEN: str = "sq"
"""Prefix prepended to the sequence number, e.g. ``sq010``."""

SHOT_TOKEN: str = "sh"
"""Prefix prepended to the shot number, e.g. ``sh0010``."""

# ---------------------------------------------------------------------------
# Versioning
# ---------------------------------------------------------------------------

DEFAULT_VERSION: str = "v001"
VERSION_PATTERN: str = r"^v(\d{3})$"
"""Version strings must match ``v###``, e.g. ``v001``, ``v042``."""

# ---------------------------------------------------------------------------
# Standard output folder names
# ---------------------------------------------------------------------------

FOLDER_OUTPUTS: str = "outputs"
FOLDER_PLAYBLASTS: str = "playblasts"
FOLDER_CACHE: str = "cache"
