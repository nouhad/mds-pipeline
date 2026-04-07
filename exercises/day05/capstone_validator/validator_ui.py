# 3D2G04A_3DScripting: Day 05
# Capstone: Validator UI
# Description: PySide window that runs the scene validator and displays pass/fail results.

try:
    from PySide2.QtWidgets import QTextEdit
except ImportError:
    from PySide6.QtWidgets import QTextEdit

from mds.ui.base_window import BaseWindow, QPushButton
from exercises.day05.capstone_validator.validator_tool import SceneValidator


class ValidatorWindow(BaseWindow):

    def build_ui(self):
        run_btn = QPushButton("Run Checks")
        run_btn.clicked.connect(self.on_run_checks)
        self._layout.addWidget(run_btn)

        self._output = QTextEdit()
        self._output.setReadOnly(True)
        self._layout.addWidget(self._output)

    def on_run_checks(self):
        validator = SceneValidator()
        results = validator.run_all_checks()

        lines = ["=== Scene Validation Results ===\n"]
        for r in results:
            tag = "[PASS]" if r["status"] == "pass" else "[FAIL]"
            line = f"{tag} {r['check']}"
            if r["nodes"]:
                line += f": {', '.join(r['nodes'])}"
            lines.append(line)

        output_text = "\n".join(lines)
        print(output_text)
        self._output.setPlainText(output_text)


window = ValidatorWindow(title="MDS Scene Validator")
window.show_window()

