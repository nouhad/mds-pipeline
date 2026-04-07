# 3D2G04A_3DScripting: Day 03
# Task 02: Import Folder OBJs
# Description: Find all .obj files in a folder, import each one into Maya, and rename using MDS naming.

from pathlib import Path

import maya.cmds as cmds

from mds.naming import buildName


# Task 1: Set the folder path and list all .obj files.
OBJ_FOLDER = Path.home() / "Desktop" / "test_objs"
objFiles = sorted(OBJ_FOLDER.glob("*.obj"))
print(f"Found {len(objFiles)} .obj file(s) in {OBJ_FOLDER}")

# Task 2: Import each OBJ file and Task 3: rename the imported transform.
for index, objPath in enumerate(objFiles, start=1):
    nodes = cmds.file(str(objPath), i=True, type="OBJ", returnNewNodes=True)
    transforms = [n for n in nodes if cmds.objectType(n) == "transform"]

    if not transforms:
        print(f"  Warning: no transform found for {objPath.name}")
        continue

    descriptor = objPath.stem.lower().replace(" ", "_").replace("-", "_")
    newName = cmds.rename(transforms[0], buildName("geo", descriptor, index))
    print(f"  Imported as: {newName}")

