"""Day 02 – Task 02 – Grid Layout.

Create a uniform grid of Maya poly spheres, named with the MDS convention.
Demonstrates nested loops, positional transforms, and build_name usage.
"""

try:
    import maya.cmds as cmds  # type: ignore[import]
except ImportError:
    cmds = None  # type: ignore[assignment]

from mds.naming import build_name


def main() -> None:
    """Create a grid of spheres and name them using MDS conventions."""

    # ------------------------------------------------------------------
    # TODO 1: Define grid dimensions and spacing.
    #         Change these values to experiment.
    # ------------------------------------------------------------------
    rows = 3        # number of rows (Z axis)
    columns = 4     # number of columns (X axis)
    spacing = 3.0   # distance between sphere centres

    if cmds is None:
        print("Maya not available – this script must be run inside Maya.")
        return

    created: list[str] = []
    index = 1

    # ------------------------------------------------------------------
    # TODO 2: Use nested loops to create a sphere at each grid position.
    #         - Outer loop: rows   (use variable `row`)
    #         - Inner loop: columns (use variable `col`)
    #         - Calculate x = col * spacing
    #         - Calculate z = row * spacing
    #         - Create sphere: transform, _ = cmds.polySphere()
    #         - Position it:   cmds.xform(transform, translation=[x, 0, z])
    # ------------------------------------------------------------------
    for row in range(rows):
        for col in range(columns):
            x = col * spacing
            z = row * spacing
            transform, _ = cmds.polySphere()
            cmds.xform(transform, translation=[x, 0, z])

            # ----------------------------------------------------------
            # TODO 3: Rename the sphere using mds.naming.build_name.
            #         Suggested prefix = "geo", descriptor = "sphere"
            #         Use `index` as the index and increment it each time.
            # ----------------------------------------------------------
            new_name = build_name("geo", "sphere", index)
            cmds.rename(transform, new_name)
            created.append(new_name)
            index += 1

    print(f"Created {len(created)} spheres in a {rows}×{columns} grid.")
    print("Spheres:", created)


if __name__ == "__main__":
    main()
