# 3D2G04A_3DScripting: Day 01
# Task 02: Transform and Shape Nodes
# Description: Create a sphere and a cube, then print the transform node and shape node for each object.

import maya.cmds as cmds


# Task 1: Create a sphere and store its transform node in a variable.
sphere_transform = cmds.polySphere()[0]

# Task 2: Create a cube and store its transform node in a variable.
cube_transform = cmds.polyCube()[0]

# Task 3: Print the transform node and shape node for each object.
sphere_shape = cmds.listRelatives(sphere_transform, shapes=True)[0]
cube_shape = cmds.listRelatives(cube_transform, shapes=True)[0]

print("Sphere transform:", sphere_transform)
print("Sphere shape:", sphere_shape)

print("Cube transform:", cube_transform)
print("Cube shape:", cube_shape)
