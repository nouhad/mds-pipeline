"""Day 03 – Task 02 – Import Folder OBJs.

Find all .obj files inside a given folder and import each one into Maya,
renaming the imported objects using the MDS naming convention.
"""

from pathlib import Path

try:
    import maya.cmds as cmds  # type: ignore[import]
except ImportError:
    cmds = None  # type: ignore[assignment]

from mds.naming import build_name


def import_objs_from_folder(folder: str | Path, prefix: str = "geo") -> list[str]:
    """Import all OBJ files found in *folder* and return their new names.

    Args:
        folder: Path to the directory containing .obj files.
        prefix: Naming prefix for imported objects (default ``"geo"``).

    Returns:
        List of new node names created in the scene.
    """
    folder = Path(folder)

    # ------------------------------------------------------------------
    # TODO 1: Use pathlib to list all .obj files in `folder`.
    #         Hint: folder.glob("*.obj") returns a generator of Path objects.
    #         Sort the results so the import order is deterministic.
    #         Print how many files were found.
    # ------------------------------------------------------------------
    obj_files: list[Path] = []  # replace with real glob call
    print(f"Found {len(obj_files)} .obj file(s) in {folder}")

    if cmds is None:
        print("Maya not available – skipping import.")
        return []

    imported_names: list[str] = []

    for index, obj_path in enumerate(obj_files, start=1):
        # --------------------------------------------------------------
        # TODO 2: Import the OBJ file using cmds.file().
        #         Hint:
        #           nodes = cmds.file(
        #               str(obj_path),
        #               i=True,           # import
        #               type="OBJ",
        #               returnNewNodes=True,
        #           )
        #         `nodes` is a list of all nodes created by the import.
        # --------------------------------------------------------------
        print(f"  Importing: {obj_path.name}")
        nodes: list[str] = []  # replace with real cmds.file() call

        # Get the transform node (usually the first item in nodes)
        transforms = [n for n in nodes if cmds.objectType(n) == "transform"]
        if not transforms:
            print(f"    Warning: no transform found for {obj_path.name}")
            continue

        transform = transforms[0]

        # --------------------------------------------------------------
        # TODO 3: Rename the imported transform using mds.naming.build_name.
        #         Use `prefix` and the stem of the filename as the descriptor.
        #         Hint: obj_path.stem gives the filename without extension.
        #         Make the descriptor valid (lowercase, no spaces) first.
        # --------------------------------------------------------------
        descriptor = obj_path.stem.lower().replace(" ", "_").replace("-", "_")
        new_name = build_name(prefix, descriptor, index)
        final_name = cmds.rename(transform, new_name)
        imported_names.append(final_name)
        print(f"    Imported as: {final_name}")

    print(f"Import complete – {len(imported_names)} object(s) imported.")
    return imported_names


def main() -> None:
    """Entry point – edit OBJ_FOLDER to point at your test assets."""

    # Change this to a folder containing some .obj files for testing.
    OBJ_FOLDER = Path.home() / "Desktop" / "test_objs"

    if not OBJ_FOLDER.exists():
        print(f"Folder not found: {OBJ_FOLDER}")
        print("Create the folder and add some .obj files, then run again.")
        return

    import_objs_from_folder(OBJ_FOLDER)


if __name__ == "__main__":
    main()
