"""Version string utilities for MDS pipeline outputs.

Versions follow the format ``v###`` (e.g. ``v001``, ``v042``).
"""

import re

from mds import config

_versionRe = re.compile(config.VERSION_PATTERN)


def parseVersion(versionStr: str) -> int:
    """Parse a version string to an integer.

    Args:
        versionStr: A version string such as ``"v007"``.

    Returns:
        The integer part of the version, e.g. ``7``.

    Raises:
        ValueError: If *versionStr* does not match ``v###``.

    Examples:
        >>> parseVersion("v007")
        7
    """
    match = _versionRe.match(versionStr)
    if not match:
        raise ValueError(
            f"Invalid version string '{versionStr}': must match '{config.VERSION_PATTERN}'"
        )
    return int(match.group(1))


def formatVersion(number: int) -> str:
    """Format an integer as a version string.

    Args:
        number: Non-negative integer version number.

    Returns:
        Zero-padded version string, e.g. ``"v003"``.

    Examples:
        >>> formatVersion(3)
        'v003'
    """
    return f"v{number:03d}"


def nextVersion(existingVersions: list[str]) -> str:
    """Return the next version string after the highest in *existingVersions*.

    Args:
        existingVersions: A list of version strings, e.g. ``["v001", "v003"]``.
            May be empty or contain versions in any order.

    Returns:
        The next version string, e.g. ``"v004"`` if ``"v003"`` was the highest.
        Returns ``"v001"`` when the list is empty.

    Examples:
        >>> nextVersion(["v001", "v002"])
        'v003'
        >>> nextVersion([])
        'v001'
    """
    if not existingVersions:
        return config.DEFAULT_VERSION
    highest = max(parseVersion(v) for v in existingVersions)
    return formatVersion(highest + 1)
