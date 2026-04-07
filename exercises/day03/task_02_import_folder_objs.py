# 3D2G04A_3DScripting: Day 03
# Task 02: Import Folder OBJs
# Description: Find all .obj files in a folder, import each one into Maya, and rename using MDS naming.

from pathlib import Path

import maya.cmds as cmds

from mds.naming import build_name


# Task 1: Set the folder path and list all .obj files.
OBJ_FOLDER = Path.home() / "Desktop" / "test_objs"
obj_files = sorted(OBJ_FOLDER.glob("*.obj"))
print(f"Found {len(obj_files)} .obj file(s) in {OBJ_FOLDER}")

# Task 2: Import each OBJ file and Task 3: rename the imported transform.
for index, obj_path in enumerate(obj_files, start=1):
    nodes = cmds.file(str(obj_path), i=True, type="OBJ", returnNewNodes=True)
    transforms = [n for n in nodes if cmds.objectType(n) == "transform"]

    if not transforms:
        print(f"  Warning: no transform found for {obj_path.name}")
        continue

    descriptor = obj_path.stem.lower().replace(" ", "_").replace("-", "_")
    new_name = cmds.rename(transforms[0], build_name("geo", descriptor, index))
    print(f"  Imported as: {new_name}")

