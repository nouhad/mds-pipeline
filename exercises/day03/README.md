# Day 03 – Paths, Versions & File I/O

## Learning Goals

By the end of Day 03 you will be able to:

- Use `pathlib.Path` to construct and inspect file system paths.
- Parse and generate version strings using `mds.versioning`.
- Read and write JSON metadata files using `mds.io`.
- Import OBJ files into Maya programmatically.

---

## Tasks Checklist

### task_01_paths_and_versions.py

Practice the path and versioning utilities without needing Maya.

- [ ] Use `mds.paths.shot_dir("010", "0010")` to construct a shot path.
- [ ] Use `mds.versioning.next_version(["v001", "v002"])` to get the next version.
- [ ] Write a JSON metadata file using `mds.io.write_json()`.
- [ ] Read it back and print the contents.

Open `exercises/day03/task_01_paths_and_versions.py` and follow the `TODO` markers.

---

### task_02_import_folder_objs.py

Find all `.obj` files in a folder and import them into Maya.

- [ ] Use `pathlib.Path.glob("*.obj")` to list OBJ files.
- [ ] For each file, use `cmds.file()` to import it.
- [ ] Rename each imported object with `mds.naming.build_name`.

Open `exercises/day03/task_02_import_folder_objs.py` and follow the `TODO` markers.

---

## Submission Steps

1. Branch: `git checkout -b day03/your-name`
2. Complete both tasks (task_01 runs without Maya; task_02 needs Maya).
3. At least **3 meaningful commits**.
4. Push and open a PR titled `Day 03 – First Last – exercises`.

---

## Stretch Goals

- **Sort versions**: given an unsorted list like `["v003", "v001", "v002"]`,
  sort them numerically (lowest first) using `mds.versioning.parse_version` as the key.
- **Skip already imported**: before importing each OBJ, check whether an object with
  the expected name already exists in the scene using `cmds.objExists()`, and skip it
  if so.
- **Metadata round-trip**: after importing, write a JSON file recording which OBJs were
  imported, when, and with what version string.
