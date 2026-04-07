# 3D2G04A_3DScripting: Day 02
# Task 01: Batch Rename
# Description: Get the current selection and rename each object using the MDS naming convention.

import maya.cmds as cmds

from mds.naming import build_name
from mds.maya.scene import get_selection


# Task 1: Get the current selection.
selected = get_selection()

# Task 2: Loop through selected objects and rename each one.
prefix = "geo"
descriptor = "object"

for index, old_name in enumerate(selected, start=1):
    new_name = cmds.rename(old_name, build_name(prefix, descriptor, index))
    print(f"{old_name}  ->  {new_name}")

