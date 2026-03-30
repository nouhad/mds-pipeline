# Capstone Validator

A reusable scene validation tool built during Day 05.

---

## What It Checks

| Check | Module | Description |
|---|---|---|
| Naming convention | `mds.maya.validate.validate_name` | All DAG nodes must match `^[a-z][a-z0-9_]*$` |
| No namespaces | `mds.maya.validate.check_no_namespaces` | Nodes must not contain `:` in their name |
| Frozen transforms | `mds.maya.validate.check_frozen_transforms` | Translate/rotate must be 0, scale must be 1 |

---

## How to Use

### From Maya's Script Editor

```python
import sys
sys.path.insert(0, r"C:\path\to\mds-pipeline\src")

from exercises.day05.capstone_validator.validator_ui import ValidatorWindow
win = ValidatorWindow()
win.show_window()
```

### Headless (no UI) – useful for automated checks

```python
from exercises.day05.capstone_validator.validator_tool import SceneValidator

v = SceneValidator()
results = v.run_all_checks()
for r in results:
    status = "✓" if r["status"] == "pass" else "✗"
    print(f"  {status} {r['check']}: {r['nodes']}")

v.export_report("/path/to/report.json")
```

---

## How to Extend With New Checks

1. Add a new method to `SceneValidator` following this pattern:

```python
def check_my_new_rule(self) -> dict:
    """Check that all nodes satisfy my new rule.

    Returns:
        Result dict with keys "check", "status", and "nodes".
    """
    dag_objects = scene.list_dag_objects()
    failing = [n for n in dag_objects if not my_condition(n)]
    return {
        "check": "my_new_rule",
        "status": "pass" if not failing else "fail",
        "nodes": failing,
    }
```

2. Call it inside `run_all_checks()`:

```python
self.results.append(self.check_my_new_rule())
```

That's it – the UI will automatically display the new check result.
