# 3D2G04A_3DScripting: Day 05
# Capstone: Validator Tool
# Description: Core validation logic. Run naming and namespace checks on the current Maya scene.

from mds.maya import validate
from mds.maya.scene import list_dag_objects
from mds import io


class SceneValidator:

    def __init__(self):
        self.results = []

    def check_naming(self):
        failing = [n for n in list_dag_objects() if not validate.validate_name(n)]
        return {"check": "naming_convention", "status": "pass" if not failing else "fail", "nodes": failing}

    def check_namespaces(self):
        failing = validate.check_no_namespaces(list_dag_objects())
        return {"check": "no_namespaces", "status": "pass" if not failing else "fail", "nodes": failing}

    def run_all_checks(self):
        self.results = [self.check_naming(), self.check_namespaces()]
        return self.results

    def export_report(self, path):
        io.write_json({"results": self.results}, path)
        print(f"Report saved to {path}")

