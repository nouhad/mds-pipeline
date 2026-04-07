# 3D2G04A_3DScripting: Day 04
# Task 02: UI Wraps Tool
# Description: Build a UI with prefix and descriptor fields that renames selected Maya objects using build_name.

import maya.cmds as cmds

try:
    from PySide2.QtWidgets import QLineEdit, QLabel
except ImportError:
    from PySide6.QtWidgets import QLineEdit, QLabel

from mds.ui.baseWindow import BaseWindow, QPushButton
from mds.maya.scene import getSelection
from mds.naming import buildName


class BatchRenameWindow(BaseWindow):

    def buildUi(self):
        self._prefixField = QLineEdit("geo")
        self._layout.addWidget(self._prefixField)

        self._descriptorField = QLineEdit("object")
        self._layout.addWidget(self._descriptorField)

        renameBtn = QPushButton("Rename Selected")
        renameBtn.clicked.connect(self._onRename)
        self._layout.addWidget(renameBtn)

        self._statusLabel = QLabel("")
        self._layout.addWidget(self._statusLabel)

    def _onRename(self):
        prefix = self._prefixField.text().strip()
        descriptor = self._descriptorField.text().strip()
        selected = getSelection()

        if not selected:
            self._statusLabel.setText("Nothing selected.")
            return

        for index, old_name in enumerate(selected, start=1):
            new_name = cmds.rename(old_name, buildName(prefix, descriptor, index))
            print(f"  {old_name}  ->  {new_name}")

        self._statusLabel.setText(f"{len(selected)} object(s) renamed.")


window = BatchRenameWindow(title="MDS Batch Rename")
window.showWindow()

