"""Day 05 – Capstone – Validator UI.

PySide window that wraps SceneValidator. Displays check results in a scrollable
text area and provides a "Run Checks" button.

Requires PySide2 (Maya 2024) or PySide6 (Maya 2025+).
"""

try:
    from PySide2.QtWidgets import QTextEdit  # type: ignore[import]
except ImportError:
    try:
        from PySide6.QtWidgets import QTextEdit  # type: ignore[import]
    except ImportError:
        QTextEdit = None  # type: ignore[assignment,misc]

try:
    from mds.ui.base_window import BaseWindow, QPushButton
    _UI_AVAILABLE = True
except Exception:
    _UI_AVAILABLE = False
    BaseWindow = object  # type: ignore[assignment,misc]

from exercises.day05.capstone_validator.validator_tool import SceneValidator


class ValidatorWindow(BaseWindow):
    """Scene validation tool window.

    Shows a "Run Checks" button and a text area that displays the pass/fail
    results of each check.
    """

    def build_ui(self) -> None:
        """Create the Run Checks button and results text area."""

        # ------------------------------------------------------------------
        # TODO 1: Add a QPushButton labelled "Run Checks".
        #         Add a QTextEdit (read-only) for displaying results.
        #         Add both to self._layout.
        # ------------------------------------------------------------------
        run_btn = QPushButton("Run Checks")
        self._layout.addWidget(run_btn)

        if QTextEdit is not None:
            self._output = QTextEdit()
            self._output.setReadOnly(True)
            self._layout.addWidget(self._output)
        else:
            self._output = None

        # Connect button
        run_btn.clicked.connect(self.on_run_checks)

    def on_run_checks(self) -> None:
        """Run SceneValidator and display results in the text area."""

        # ------------------------------------------------------------------
        # TODO 2: Instantiate SceneValidator, call run_all_checks(), and
        #         format the results into a human-readable string.
        #         Display the string in self._output (QTextEdit).
        #
        #         For each result dict, show something like:
        #           [PASS] naming_convention
        #           [FAIL] no_namespaces: namespace:node1, namespace:node2
        # ------------------------------------------------------------------
        validator = SceneValidator()
        results = validator.run_all_checks()

        lines: list[str] = ["=== Scene Validation Results ===\n"]
        for r in results:
            status_tag = "[PASS]" if r["status"] == "pass" else "[FAIL]"
            line = f"{status_tag} {r['check']}"
            if r["nodes"]:
                line += f": {', '.join(r['nodes'])}"
            lines.append(line)

        if not results:
            lines.append("No checks were run. Implement run_all_checks() first.")

        output_text = "\n".join(lines)
        print(output_text)

        if self._output is not None:
            self._output.setPlainText(output_text)


def main() -> None:
    """Show the ValidatorWindow."""
    if not _UI_AVAILABLE:
        print("Qt is not installed – cannot show UI.")
        return

    window = ValidatorWindow(title="MDS Scene Validator")
    window.show_window()
    return window


if __name__ == "__main__":
    main()
