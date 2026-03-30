"""Day 01 – Task 02 – Selection Report.

Print a formatted report of the objects currently selected in Maya.
Practice using mds.maya.scene and basic loops/string formatting.
"""

try:
    import maya.cmds as cmds  # type: ignore[import]
except ImportError:
    cmds = None  # type: ignore[assignment]

from mds.maya import scene


def main() -> None:
    """Print a report of the current Maya selection."""

    # ------------------------------------------------------------------
    # TODO 1: Get the current selection.
    #         Use mds.maya.scene.get_selection() – this is already
    #         imported above as `scene`.
    # ------------------------------------------------------------------
    selected = []  # replace with the real call

    # ------------------------------------------------------------------
    # TODO 2: Print the total count and the list of selected objects.
    #         Example output:
    #           Selected: 3 object(s)
    #           - pSphere1
    #           - pCube1
    #           - nurbsCircle1
    # ------------------------------------------------------------------
    print(f"Selected: {len(selected)} object(s)")
    for obj in selected:
        print(f"  - {obj}")

    # ------------------------------------------------------------------
    # TODO 3: For each selected object, also print its Maya type.
    #         Hint: cmds.objectType(obj) returns the type string.
    #         Guard against cmds being None.
    #         Example output:
    #           - pSphere1  [type: transform]
    # ------------------------------------------------------------------
    # Replace the loop above (or extend it) to include the type.


if __name__ == "__main__":
    main()
