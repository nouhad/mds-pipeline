# 3D2G04A_3DScripting: Day 05
# Capstone: Validator Tool
# Description: Core validation logic. Run naming and namespace checks on the current Maya scene.

from mds.maya import validate
from mds.maya.scene import listDagObjects
from mds import io


class SceneValidator:

    def __init__(self):
        self.results = []

    def checkNaming(self):
        failing = [n for n in listDagObjects() if not validate.validateName(n)]
        return {"check": "naming_convention", "status": "pass" if not failing else "fail", "nodes": failing}

    def checkNamespaces(self):
        failing = validate.checkNoNamespaces(listDagObjects())
        return {"check": "no_namespaces", "status": "pass" if not failing else "fail", "nodes": failing}

    def runAllChecks(self):
        self.results = [self.checkNaming(), self.checkNamespaces()]
        return self.results

    def exportReport(self, path):
        io.writeJson({"results": self.results}, path)
        print(f"Report saved to {path}")

