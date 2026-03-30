# Day 04 – Building Tools with PySide

## Learning Goals

By the end of Day 04 you will be able to:

- Create a simple Qt window using `mds.ui.base_window.BaseWindow`.
- Add widgets (buttons, labels, text fields) to a layout.
- Connect Qt signals to Python methods.
- Wrap an existing pipeline function in a UI so artists can use it without
  typing any code.

---

## Tasks Checklist

### task_01_simple_ui.py

Build a minimal window with one button.

- [ ] Subclass `BaseWindow` and implement `build_ui()`.
- [ ] Add a `QPushButton` with the label `"Hello from UI"`.
- [ ] Connect the button's `clicked` signal to a method that prints a message.
- [ ] Instantiate the window and call `show_window()`.

Open `exercises/day04/task_01_simple_ui.py` and follow the `TODO` markers.

---

### task_02_ui_wraps_tool.py

Wrap the Day 02 batch rename functionality in a proper UI.

- [ ] Add a `QLineEdit` for the **prefix** and one for the **descriptor**.
- [ ] Add a `QPushButton` labelled `"Rename"`.
- [ ] On click: get the Maya selection, call `build_name` for each object,
  rename, and print a report.
- [ ] Add a `QLabel` that updates to show `"X objects renamed"` after each run.

Open `exercises/day04/task_02_ui_wraps_tool.py` and follow the `TODO` markers.

---

## Submission Steps

1. Branch: `git checkout -b day04/your-name`
2. Complete both tasks (test in Maya where PySide2/PySide6 is available).
3. At least **3 meaningful commits**.
4. Push and open a PR titled `Day 04 – First Last – exercises`.

---

## Stretch Goals

- **Type filter dropdown**: add a `QComboBox` to task_02 so the user can choose
  which object type to rename (e.g. "transform", "mesh", "nurbsCurve").
- **Save/load settings**: persist the prefix and descriptor fields to a JSON file
  using `mds.io.write_json`, and reload them when the window opens.
- **Clear button**: add a second button that resets both text fields to their defaults.
