# 3D2G04A_3DScripting: Day 01
# Task 02: Transform and Shape Nodes
# Description: Create a sphere and a cube, then print the transform node and shape node for each object.

import maya.cmds as cmds


# Task 1: Create a sphere and store its transform node in a variable.
sphereTransform = cmds.polySphere()[0]

# Task 2: Create a cube and store its transform node in a variable.
cubeTransform, polyCubeNode = cmds.polyCube()

# Task 3: Print the transform node and shape node for each object.
sphereShape = cmds.listRelatives(sphereTransform, shapes=True)[0]
cubeShape = cmds.listRelatives(cubeTransform, shapes=True)[0]

print("Sphere transform:", sphereTransform)
print("Sphere shape:", sphereShape)

print("Cube transform:", cubeTransform)
print("Cube shape:", cubeShape)
