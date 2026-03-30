# Day 05 – Capstone: Scene Validator

## Overview

Day 05 brings everything together. You will build a **complete, production-style scene
validation tool** that:

1. Inspects every DAG object in the scene.
2. Runs a series of automated checks.
3. Displays the results in a Qt UI.
4. Can export a JSON report.

This mirrors the kind of tooling used at real VFX and games studios to enforce quality
standards before assets are published.

---

## Learning Goals

- Combine `naming`, `paths`, `versioning`, `io`, and `ui` into one cohesive tool.
- Separate logic (validator_tool.py) from presentation (validator_ui.py).
- Write clean, reusable, documented code.
- Think about extensibility: how would you add a new check?

---

## Tasks Checklist

### validator_tool.py (core logic – no UI)

- [ ] Implement `SceneValidator.check_naming()` using `mds.maya.validate.validate_name`.
- [ ] Implement `SceneValidator.check_namespaces()` using `mds.maya.validate.check_no_namespaces`.
- [ ] Implement `SceneValidator.run_all_checks()` to call both checks and return results.
- [ ] Implement `SceneValidator.export_report()` to save results as JSON.

### validator_ui.py (PySide UI)

- [ ] Subclass `BaseWindow`, implement `build_ui()` with a "Run Checks" button and
  a `QTextEdit` for output.
- [ ] Implement `on_run_checks()` to run the validator and display results.

---

## Submission Steps

1. Branch: `git checkout -b day05/your-name`
2. Complete both files inside `exercises/day05/capstone_validator/`.
3. At least **3 meaningful commits** showing progression.
4. Push and open a PR titled `Day 05 – First Last – exercises`.

---

## Stretch Goals

- **Export button**: add a `QPushButton` in the UI that calls `export_report()` and
  saves the JSON to the shot's output directory using `mds.paths`.
- **Colour-coded results**: use HTML formatting in `QTextEdit.setHtml()` to show
  passing checks in green and failing checks in red.
- **Additional checks**: add a `check_history_deleted` or `check_no_intermediate_objects`
  method to `SceneValidator`.
