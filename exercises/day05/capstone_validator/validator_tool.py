"""Day 05 – Capstone – Validator Tool.

Core validation logic with no UI dependency. Runs a series of named checks
against the current Maya scene and collects pass/fail results.

Each check method returns a dict with the shape::

    {
        "check":  "<check_name>",
        "status": "pass" | "fail",
        "nodes":  [<failing_node>, ...],  # empty list on pass
    }

Usage example (inside Maya or with a mocked scene)::

    from exercises.day05.capstone_validator.validator_tool import SceneValidator

    v = SceneValidator()
    results = v.run_all_checks()
    v.export_report("/path/to/report.json")
"""

from mds.maya import validate, scene
from mds.maya.scene import list_dag_objects
from mds import io


class SceneValidator:
    """Run a suite of validation checks on the current Maya scene.

    Attributes:
        results: List of result dicts populated by :meth:`run_all_checks`.
    """

    def __init__(self) -> None:
        self.results: list[dict] = []

    def run_all_checks(self) -> list[dict]:
        """Run all registered checks and return the combined results.

        Returns:
            List of result dicts (one per check). Also stored in
            ``self.results`` for later export.
        """
        self.results = []

        # ------------------------------------------------------------------
        # TODO: Add calls to each check method here.
        #       Each method returns a result dict – append it to self.results.
        #       Example:
        #           self.results.append(self.check_naming())
        #           self.results.append(self.check_namespaces())
        # ------------------------------------------------------------------

        return self.results

    def check_naming(self) -> dict:
        """Check that all DAG object names conform to the MDS naming convention.

        Uses :func:`mds.maya.validate.validate_name` on every node returned by
        :func:`mds.maya.scene.list_dag_objects`.

        Returns:
            Result dict. ``"nodes"`` contains the names of failing nodes.
        """
        dag_objects = list_dag_objects()

        # ------------------------------------------------------------------
        # TODO: Iterate over dag_objects and collect nodes that fail
        #       validate.validate_name().
        #       Return a result dict with "check", "status", and "nodes".
        # ------------------------------------------------------------------
        failing: list[str] = []
        # for node in dag_objects:
        #     if not validate.validate_name(node):
        #         failing.append(node)

        return {
            "check": "naming_convention",
            "status": "pass" if not failing else "fail",
            "nodes": failing,
        }

    def check_namespaces(self) -> dict:
        """Check that no DAG objects carry a namespace.

        Uses :func:`mds.maya.validate.check_no_namespaces`.

        Returns:
            Result dict. ``"nodes"`` contains namespaced node names.
        """
        dag_objects = list_dag_objects()

        # ------------------------------------------------------------------
        # TODO: Call validate.check_no_namespaces(dag_objects) to get the
        #       list of nodes that contain ":".
        #       Build and return the result dict.
        # ------------------------------------------------------------------
        failing: list[str] = []
        # failing = validate.check_no_namespaces(dag_objects)

        return {
            "check": "no_namespaces",
            "status": "pass" if not failing else "fail",
            "nodes": failing,
        }

    def export_report(self, path) -> None:
        """Write ``self.results`` to a JSON file.

        Args:
            path: Destination file path (str or :class:`pathlib.Path`).
                  Parent directories are created automatically.
        """
        # ------------------------------------------------------------------
        # TODO: Use mds.io.write_json to save self.results to `path`.
        #       Wrap the list in a dict with a top-level "results" key:
        #           {"results": self.results}
        # ------------------------------------------------------------------
        print(f"TODO: export report to {path}")
        # io.write_json({"results": self.results}, path)
