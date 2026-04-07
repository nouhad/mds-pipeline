# 3D2G04A_3DScripting: Day 02
# Task 02: Grid Layout
# Description: Use nested loops to create a grid of spheres and name each one with the MDS convention.

import maya.cmds as cmds

from mds.naming import build_name


# Task 1: Define grid dimensions and spacing.
rows = 3
columns = 4
spacing = 3.0

# Task 2: Use nested loops to create a sphere at each grid position.
# Task 3: Rename each sphere using mds.naming.build_name.
index = 1

for row in range(rows):
    for col in range(columns):
        transform, _ = cmds.polySphere()
        cmds.xform(transform, translation=[col * spacing, 0, row * spacing])
        cmds.rename(transform, build_name("geo", "sphere", index))
        index += 1

print(f"Created {rows * columns} spheres in a {rows}x{columns} grid.")

