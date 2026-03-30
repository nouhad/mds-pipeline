# Day 02 – Batch Operations & Loops

## Learning Goals

By the end of Day 02 you will be able to:

- Iterate over lists of Maya DAG objects.
- Rename multiple nodes programmatically using the MDS naming convention.
- Build grid-based object layouts with nested loops.
- Use `mds.naming.build_name` to generate standardised names.

---

## Tasks Checklist

### task_01_batch_rename.py

Select several objects in your Maya scene before running this script.

- [ ] Retrieve the current selection with `mds.maya.scene.get_selection()`.
- [ ] Loop through each selected object and rename it using
  `mds.naming.build_name(prefix, descriptor, index)`.
- [ ] Print a report showing `old_name → new_name` for every object.

Open `exercises/day02/task_01_batch_rename.py` and follow the `TODO` markers.

---

### task_02_grid_layout.py

Create a grid of Maya spheres arranged in rows and columns.

- [ ] Define `rows`, `columns`, and `spacing` variables.
- [ ] Use nested loops to create a sphere at each grid position with `cmds.polySphere()`.
- [ ] Position each sphere correctly using `cmds.xform()`.
- [ ] Name each sphere with `mds.naming.build_name`.

Open `exercises/day02/task_02_grid_layout.py` and follow the `TODO` markers.

---

## Submission Steps

1. Branch: `git checkout -b day02/your-name`
2. Complete both tasks.
3. Commit at least **3 times** (e.g. after task_01 loop, after rename report, after task_02).
4. Push and open a PR titled `Day 02 – First Last – exercises`.

---

## Stretch Goals

- **Custom prefix**: prompt the user for a prefix string using Python's `input()` (or a
  Maya `promptDialog`), then use that prefix in `build_name`.
- **Undo chunk**: wrap the rename operations in a Maya undo chunk so they can be undone
  with a single Ctrl+Z:
  ```python
  cmds.undoInfo(openChunk=True)
  # ... your code ...
  cmds.undoInfo(closeChunk=True)
  ```
- **Skip invalids**: if `build_name` raises a `ValueError`, catch it, print a warning,
  and continue with the next object instead of crashing.
