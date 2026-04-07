# 3D2G04A_3DScripting: Day 02
# Task 01: Batch Rename
# Description: Get the current selection and rename each object using the MDS naming convention.

import maya.cmds as cmds

from mds.naming import buildName
from mds.maya.scene import getSelection


# Task 1: Get the current selection.
selected = getSelection()

# Task 2: Loop through selected objects and rename each one.
prefix = "geo"
descriptor = "object"

for index, oldName in enumerate(selected, start=1):
    newName = cmds.rename(oldName, buildName(prefix, descriptor, index))
    print(f"{oldName}  ->  {newName}")

