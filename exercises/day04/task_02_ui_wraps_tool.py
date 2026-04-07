# 3D2G04A_3DScripting: Day 04
# Task 02: UI Wraps Tool
# Description: Build a UI with prefix and descriptor fields that renames selected Maya objects using build_name.

import maya.cmds as cmds

try:
    from PySide2.QtWidgets import QLineEdit, QLabel
except ImportError:
    from PySide6.QtWidgets import QLineEdit, QLabel

from mds.ui.base_window import BaseWindow, QPushButton
from mds.maya.scene import get_selection
from mds.naming import build_name


class BatchRenameWindow(BaseWindow):

    def build_ui(self):
        self._prefix_field = QLineEdit("geo")
        self._layout.addWidget(self._prefix_field)

        self._descriptor_field = QLineEdit("object")
        self._layout.addWidget(self._descriptor_field)

        rename_btn = QPushButton("Rename Selected")
        rename_btn.clicked.connect(self._on_rename)
        self._layout.addWidget(rename_btn)

        self._status_label = QLabel("")
        self._layout.addWidget(self._status_label)

    def _on_rename(self):
        prefix = self._prefix_field.text().strip()
        descriptor = self._descriptor_field.text().strip()
        selected = get_selection()

        if not selected:
            self._status_label.setText("Nothing selected.")
            return

        for index, old_name in enumerate(selected, start=1):
            new_name = cmds.rename(old_name, build_name(prefix, descriptor, index))
            print(f"  {old_name}  ->  {new_name}")

        self._status_label.setText(f"{len(selected)} object(s) renamed.")


window = BatchRenameWindow(title="MDS Batch Rename")
window.show_window()

