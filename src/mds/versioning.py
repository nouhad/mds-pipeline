"""Version string utilities for MDS pipeline outputs.

Versions follow the format ``v###`` (e.g. ``v001``, ``v042``).
"""

import re

from mds import config

_VERSION_RE = re.compile(config.VERSION_PATTERN)


def parse_version(version_str: str) -> int:
    """Parse a version string to an integer.

    Args:
        version_str: A version string such as ``"v007"``.

    Returns:
        The integer part of the version, e.g. ``7``.

    Raises:
        ValueError: If *version_str* does not match ``v###``.

    Examples:
        >>> parse_version("v007")
        7
    """
    match = _VERSION_RE.match(version_str)
    if not match:
        raise ValueError(
            f"Invalid version string '{version_str}': must match '{config.VERSION_PATTERN}'"
        )
    return int(match.group(1))


def format_version(number: int) -> str:
    """Format an integer as a version string.

    Args:
        number: Non-negative integer version number.

    Returns:
        Zero-padded version string, e.g. ``"v003"``.

    Examples:
        >>> format_version(3)
        'v003'
    """
    return f"v{number:03d}"


def next_version(existing_versions: list[str]) -> str:
    """Return the next version string after the highest in *existing_versions*.

    Args:
        existing_versions: A list of version strings, e.g. ``["v001", "v003"]``.
            May be empty or contain versions in any order.

    Returns:
        The next version string, e.g. ``"v004"`` if ``"v003"`` was the highest.
        Returns ``"v001"`` when the list is empty.

    Examples:
        >>> next_version(["v001", "v002"])
        'v003'
        >>> next_version([])
        'v001'
    """
    if not existing_versions:
        return config.DEFAULT_VERSION
    highest = max(parse_version(v) for v in existing_versions)
    return format_version(highest + 1)
