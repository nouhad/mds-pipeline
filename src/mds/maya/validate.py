"""Maya node validation utilities.

Name-based checks (``validate_name``, ``check_no_namespaces``) do **not** require Maya
and can be run in any Python environment.

Transform checks (``check_frozen_transforms``) use ``maya.cmds`` when available, and
return a safe default when Maya is not present.
"""

try:
    import maya.cmds as cmds  # type: ignore[import]
except ImportError:
    cmds = None  # type: ignore[assignment]

from mds import naming

# Default values for a frozen transform
_DEFAULT_TRANSLATE = [0.0, 0.0, 0.0]
_DEFAULT_ROTATE = [0.0, 0.0, 0.0]
_DEFAULT_SCALE = [1.0, 1.0, 1.0]


def validate_name(node: str) -> bool:
    """Check whether a node's short name conforms to the MDS naming convention.

    The short name is the portion of *node* after the last ``|`` (pipe), which
    strips the DAG long-name prefix.

    Does **not** require Maya.

    Args:
        node: Node name or long DAG path, e.g. ``"|group1|geo_sphere_001"``.

    Returns:
        ``True`` if the short name is valid, ``False`` otherwise.
    """
    short_name = node.split("|")[-1]
    return naming.is_valid_name(short_name)


def check_no_namespaces(nodes: list[str]) -> list[str]:
    """Return nodes that contain a namespace separator (``:``) in their name.

    Namespaces are not permitted in publish-ready assets. Use this check before
    exporting to flag nodes that still carry a namespace.

    Does **not** require Maya.

    Args:
        nodes: List of node name strings to check.

    Returns:
        Subset of *nodes* whose names contain ``":"``.
    """
    return [n for n in nodes if ":" in n]


def check_frozen_transforms(node: str) -> bool:
    """Return True if the node's transforms are frozen (at identity values).

    Checks translate (0,0,0), rotate (0,0,0), and scale (1,1,1).

    If Maya is not available this function returns ``True`` so that non-Maya
    environments treat the check as passing (i.e. skipped rather than failed).

    Args:
        node: Short or long Maya node name.

    Returns:
        ``True`` if transforms are at default values or Maya is unavailable,
        ``False`` if any channel differs from the identity.
    """
    if cmds is None:
        return True

    def _near(a: float, b: float, tol: float = 1e-5) -> bool:
        return abs(a - b) < tol

    translate = cmds.getAttr(f"{node}.translate")[0]
    rotate = cmds.getAttr(f"{node}.rotate")[0]
    scale = cmds.getAttr(f"{node}.scale")[0]

    for actual, expected in zip(translate, _DEFAULT_TRANSLATE):
        if not _near(actual, expected):
            return False
    for actual, expected in zip(rotate, _DEFAULT_ROTATE):
        if not _near(actual, expected):
            return False
    for actual, expected in zip(scale, _DEFAULT_SCALE):
        if not _near(actual, expected):
            return False
    return True
