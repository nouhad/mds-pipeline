# 3D2G04A_3DScripting: Day 01
# Task 03: Loop and Create Objects
# Description: Use a loop to create 5 cubes, space them apart along the X axis, and print each transform node name.

import maya.cmds as cmds


# Task 1: Use a loop to create 5 cubes.
# Task 2: Move each cube along the X axis so they do not overlap.
# Task 3: Print the transform node name of each cube.

cubes = []

for i in range(5):
    cubeTransform, polyCubeNode = cmds.polyCube()
    cmds.move(i * 3, 0, 0, cubeTransform)
    cubes.append(cubeTransform)
    print("Created:", cubeTransform)
