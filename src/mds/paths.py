"""Path construction utilities for MDS pipeline projects.

All paths are built relative to the project root, which can be overridden via
the MDS_PROJECT_ROOT environment variable.
"""

import os
from pathlib import Path

from mds import config


def getProjectRoot() -> Path:
    """Return the filesystem root for all MDS projects.

    Checks the ``MDS_PROJECT_ROOT`` environment variable first.
    Falls back to ``config.DEFAULT_PROJECT_ROOT`` if the variable is not set.

    Returns:
        Absolute path to the project root directory.
    """
    envRoot = os.environ.get("MDS_PROJECT_ROOT")
    if envRoot:
        return Path(envRoot)
    return config.DEFAULT_PROJECT_ROOT


def shotDir(seq: str, shot: str) -> Path:
    """Return the directory for a specific shot.

    Args:
        seq: Sequence number string, e.g. ``"010"``.
        shot: Shot number string, e.g. ``"0010"``.

    Returns:
        Path of the form ``<project_root>/sq010/sh0010``.
    """
    return getProjectRoot() / f"{config.SEQ_TOKEN}{seq}" / f"{config.SHOT_TOKEN}{shot}"


def playblastDir(seq: str, shot: str, version: str) -> Path:
    """Return the versioned playblast output directory for a shot.

    Args:
        seq: Sequence number string, e.g. ``"010"``.
        shot: Shot number string, e.g. ``"0010"``.
        version: Version string, e.g. ``"v001"``.

    Returns:
        Path of the form ``<shot_dir>/outputs/playblasts/<version>``.
    """
    return (
        shotDir(seq, shot)
        / config.FOLDER_OUTPUTS
        / config.FOLDER_PLAYBLASTS
        / version
    )


def cacheDir(seq: str, shot: str, version: str) -> Path:
    """Return the versioned cache output directory for a shot.

    Args:
        seq: Sequence number string, e.g. ``"010"``.
        shot: Shot number string, e.g. ``"0010"``.
        version: Version string, e.g. ``"v001"``.

    Returns:
        Path of the form ``<shot_dir>/outputs/cache/<version>``.
    """
    return (
        shotDir(seq, shot)
        / config.FOLDER_OUTPUTS
        / config.FOLDER_CACHE
        / version
    )


def ensureDir(path: Path) -> Path:
    """Create *path* (and any missing parents) if it does not already exist.

    Args:
        path: Directory path to create.

    Returns:
        The same *path* that was passed in, for convenient chaining.
    """
    path.mkdir(parents=True, exist_ok=True)
    return path
