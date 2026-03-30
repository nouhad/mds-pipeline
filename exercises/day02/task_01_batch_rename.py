"""Day 02 – Task 01 – Batch Rename.

Rename the currently selected Maya objects so they follow the MDS naming convention.
Uses mds.naming.build_name to generate standardised names and prints a rename report.
"""

try:
    import maya.cmds as cmds  # type: ignore[import]
except ImportError:
    cmds = None  # type: ignore[assignment]

from mds.naming import build_name
from mds.maya.scene import get_selection


def main() -> None:
    """Rename selected objects and print a before/after report."""

    # ------------------------------------------------------------------
    # TODO 1: Get the current selection.
    #         Use get_selection() imported above.
    #         Store the result in a variable called `selected`.
    # ------------------------------------------------------------------
    selected = []  # replace with real call

    if not selected:
        print("Nothing selected – please select objects in Maya first.")
        return

    # ------------------------------------------------------------------
    # TODO 2: Loop through selected objects and rename each one.
    #         Use build_name(prefix, descriptor, index) where:
    #           prefix     = "geo"          (or let the user choose – stretch goal)
    #           descriptor = "object"       (or derive from the original name)
    #           index      = loop counter starting at 1
    #
    #         Rename using:  new_name = cmds.rename(old_name, proposed_name)
    #         Note: cmds.rename() returns the actual new name (Maya may adjust it).
    #
    #         Guard against cmds being None.
    # ------------------------------------------------------------------
    prefix = "geo"
    descriptor = "object"

    rename_pairs: list[tuple[str, str]] = []

    for index, old_name in enumerate(selected, start=1):
        proposed_name = build_name(prefix, descriptor, index)
        if cmds is not None:
            new_name = cmds.rename(old_name, proposed_name)
        else:
            new_name = proposed_name  # simulation outside Maya
        rename_pairs.append((old_name, new_name))

    # ------------------------------------------------------------------
    # TODO 3: Print a report of old_name → new_name pairs.
    #         Example:
    #           pSphere1  →  geo_object_001
    #           pCube1    →  geo_object_002
    # ------------------------------------------------------------------
    print("\n--- Rename Report ---")
    for old, new in rename_pairs:
        print(f"  {old}  →  {new}")
    print(f"Renamed {len(rename_pairs)} object(s).")


if __name__ == "__main__":
    main()
