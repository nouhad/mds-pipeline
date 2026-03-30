"""Maya scene query utilities.

All ``maya.cmds`` calls are wrapped in guarded functions. When this module is
imported outside of a running Maya session, ``cmds`` is set to ``None`` and every
function returns a safe empty value instead of raising an ImportError.

This design lets you write and test logic in a plain Python environment (or in CI)
without needing a Maya licence.
"""

try:
    import maya.cmds as cmds  # type: ignore[import]
except ImportError:
    cmds = None  # type: ignore[assignment]


def get_scene_name() -> str:
    """Return the full path of the currently open Maya scene file.

    Returns:
        Scene file path string, or ``""`` if Maya is not available or no file
        is open.
    """
    if cmds is None:
        return ""
    return cmds.file(query=True, sceneName=True) or ""


def list_dag_objects(type_filter: str = "") -> list[str]:
    """Return a list of DAG objects in the current scene.

    Args:
        type_filter: Optional Maya node type string to filter by (e.g. ``"mesh"``).
            When empty, all DAG nodes are returned.

    Returns:
        List of node name strings, or ``[]`` if Maya is not available.
    """
    if cmds is None:
        return []
    kwargs: dict = {"dag": True, "long": False}
    if type_filter:
        kwargs["type"] = type_filter
    result = cmds.ls(**kwargs)
    return result if result else []


def get_selection() -> list[str]:
    """Return the names of currently selected objects.

    Returns:
        List of selected node name strings, or ``[]`` if Maya is not available
        or nothing is selected.
    """
    if cmds is None:
        return []
    result = cmds.ls(selection=True)
    return result if result else []


def open_scene(path: str) -> bool:
    """Open a Maya scene file, discarding unsaved changes.

    This function forcibly opens *path* without prompting to save the current
    scene. Use with care – unsaved work will be lost.

    Args:
        path: Absolute path to the ``.ma`` or ``.mb`` file.

    Returns:
        ``True`` if the scene was opened successfully, ``False`` if Maya is not
        available.
    """
    if cmds is None:
        return False
    cmds.file(path, open=True, force=True)
    return True
