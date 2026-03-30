"""Naming utilities for MDS pipeline assets.

Provides validation, construction, and tokenisation of standardised asset names.
All names must satisfy VALID_NAME_PATTERN (see mds.config).
"""

import re

from mds import config

_VALID_RE = re.compile(config.VALID_NAME_PATTERN)


def is_valid_name(name: str) -> bool:
    """Return True if *name* matches the MDS naming convention.

    A valid name starts with a lowercase letter and contains only lowercase
    alphanumeric characters and underscores.

    Args:
        name: The name string to validate.

    Returns:
        True if valid, False otherwise.

    Examples:
        >>> is_valid_name("geo_sphere_001")
        True
        >>> is_valid_name("GeoSphere")
        False
    """
    if not name:
        return False
    return bool(_VALID_RE.match(name))


def build_name(prefix: str, descriptor: str, index: int) -> str:
    """Build a standardised three-part asset name.

    Args:
        prefix: Short category token, e.g. ``"geo"``.
        descriptor: Human-readable descriptor, e.g. ``"sphere"``.
        index: One-based integer index (padded to three digits).

    Returns:
        Formatted name string, e.g. ``"geo_sphere_001"``.

    Raises:
        ValueError: If *prefix* or *descriptor* do not match VALID_NAME_PATTERN.

    Examples:
        >>> build_name("geo", "sphere", 1)
        'geo_sphere_001'
    """
    if not is_valid_name(prefix):
        raise ValueError(
            f"Invalid prefix '{prefix}': must match '{config.VALID_NAME_PATTERN}'"
        )
    if not is_valid_name(descriptor):
        raise ValueError(
            f"Invalid descriptor '{descriptor}': must match '{config.VALID_NAME_PATTERN}'"
        )
    return f"{prefix}_{descriptor}_{index:03d}"


def tokenise_name(name: str) -> list[str]:
    """Split a name string on underscores and return the list of tokens.

    Args:
        name: An asset name such as ``"geo_sphere_001"``.

    Returns:
        List of token strings, e.g. ``["geo", "sphere", "001"]``.

    Examples:
        >>> tokenise_name("geo_sphere_001")
        ['geo', 'sphere', '001']
    """
    return name.split("_")
