# Day 01 – Python Basics & Maya Hello World

## Learning Goals

By the end of Day 01 you will be able to:

- Run Python code inside Maya via the Script Editor or VS Code.
- Use `print`, variables, and basic string formatting.
- Access Maya commands via `maya.cmds`.
- Import and use functions from the `mds` package.

---

## Tasks Checklist

### task_01_hello_maya.py

Print basic information about the current Maya session.

- [ ] Print a greeting that includes your own name.
- [ ] Print the Maya version using `cmds.about(version=True)`.
- [ ] Print the current scene name using `mds.maya.scene.get_scene_name()`.

Open `exercises/day01/task_01_hello_maya.py` and follow the `TODO` markers.

---

### task_02_selection_report.py

Print a formatted report of the currently selected objects.

- [ ] Get the selection using `mds.maya.scene.get_selection()`.
- [ ] Print the total count of selected objects.
- [ ] Print the name of each selected object.
- [ ] For each object, also print its Maya type using `cmds.objectType()`.

Open `exercises/day01/task_02_selection_report.py` and follow the `TODO` markers.

---

## Submission Steps

1. Create your branch: `git checkout -b day01/your-name`
2. Complete both tasks.
3. Make at least **3 commits** (one after each logical step – don't commit everything at once).
4. Push: `git push -u origin day01/your-name`
5. Open a PR titled `Day 01 – First Last – exercises` and request a review.

See [docs/04_submission_rules.md](../../docs/04_submission_rules.md) for full rules.

---

## Stretch Goals

These are optional – attempt them after completing the core tasks.

- **Filter by type**: modify task_02 to only show objects of a specific type
  (e.g. print meshes separately from transforms).
- **Poly face count**: for each mesh in the selection, print the number of faces
  using `cmds.polyEvaluate(f=True)`.
- **Format as a table**: align the columns in your printed output neatly using
  f-string padding, e.g. `f"{name:<40} {obj_type:<20}"`.
