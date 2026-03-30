"""JSON file I/O utilities for MDS pipeline data.

Provides safe read/write helpers that handle missing files, directory creation,
and consistent formatting.
"""

import json
from pathlib import Path


def read_json(path: Path | str) -> dict:
    """Read a JSON file and return its contents as a dictionary.

    Args:
        path: Path to the JSON file.

    Returns:
        Parsed dictionary.

    Raises:
        FileNotFoundError: With a descriptive message if the file does not exist.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"JSON file not found: {path}\n"
            f"Check that the path is correct and the file has been created."
        )
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def write_json(data: dict, path: Path | str, indent: int = 2) -> None:
    """Write a dictionary to a JSON file, creating parent directories as needed.

    Args:
        data: The dictionary to serialise.
        path: Destination file path.
        indent: JSON indentation level (default 2 spaces).
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=indent)
        fh.write("\n")  # ensure trailing newline


def read_json_safe(path: Path | str, default: dict | None = None) -> dict:
    """Read a JSON file, returning *default* instead of raising if it is missing.

    Args:
        path: Path to the JSON file.
        default: Value returned when the file does not exist. Defaults to ``{}``.

    Returns:
        Parsed dictionary, or *default* if the file was not found.
    """
    if default is None:
        default = {}
    try:
        return read_json(path)
    except FileNotFoundError:
        return default
