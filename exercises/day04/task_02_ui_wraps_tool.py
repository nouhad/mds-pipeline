"""Day 04 – Task 02 – UI Wraps Tool.

Build a UI that wraps the Day 02 batch rename functionality so that artists
can run it without typing any code. Demonstrates combining BaseWindow with
Maya operations and live status feedback via a QLabel.
"""

try:
    from PySide2.QtWidgets import QLineEdit, QLabel  # type: ignore[import]
except ImportError:
    try:
        from PySide6.QtWidgets import QLineEdit, QLabel  # type: ignore[import]
    except ImportError:
        QLineEdit = None  # type: ignore[assignment,misc]
        QLabel = None  # type: ignore[assignment,misc]

try:
    import maya.cmds as cmds  # type: ignore[import]
except ImportError:
    cmds = None  # type: ignore[assignment]

try:
    from mds.ui.base_window import BaseWindow, QPushButton
    _UI_AVAILABLE = True
except Exception:
    _UI_AVAILABLE = False
    BaseWindow = object  # type: ignore[assignment,misc]

from mds.maya.scene import get_selection
from mds.naming import build_name


# ------------------------------------------------------------------
# TODO 1: Subclass BaseWindow and implement build_ui() to create:
#           - A QLineEdit for the prefix  (default text: "geo")
#           - A QLineEdit for the descriptor (default text: "object")
#           - A QPushButton labelled "Rename Selected"
#           - A QLabel showing rename status (initially empty)
# ------------------------------------------------------------------
class BatchRenameWindow(BaseWindow):
    """UI wrapper for the batch rename pipeline tool."""

    def build_ui(self) -> None:
        """Build the rename UI widgets."""
        if QLineEdit is None or QLabel is None:
            return

        # Prefix field
        self._prefix_field = QLineEdit("geo")
        self._prefix_field.setPlaceholderText("Prefix (e.g. geo)")
        self._layout.addWidget(self._prefix_field)

        # Descriptor field
        self._descriptor_field = QLineEdit("object")
        self._descriptor_field.setPlaceholderText("Descriptor (e.g. sphere)")
        self._layout.addWidget(self._descriptor_field)

        # Rename button
        rename_btn = QPushButton("Rename Selected")
        self._layout.addWidget(rename_btn)

        # Status label
        self._status_label = QLabel("")
        self._layout.addWidget(self._status_label)

        # ------------------------------------------------------------------
        # TODO 2: Connect rename_btn.clicked to self._on_rename.
        # ------------------------------------------------------------------
        rename_btn.clicked.connect(self._on_rename)

    def _on_rename(self) -> None:
        """Read UI fields, rename selected objects, and update the status label."""

        prefix = self._prefix_field.text().strip()
        descriptor = self._descriptor_field.text().strip()

        # --------------------------------------------------------------
        # TODO 2 (continued): Get the current Maya selection.
        #         Rename each object using build_name(prefix, descriptor, index).
        #         If cmds is available, call cmds.rename(old, new).
        #         Collect the rename pairs for the report.
        # --------------------------------------------------------------
        selected = get_selection()

        if not selected:
            self._status_label.setText("Nothing selected.")
            return

        rename_pairs: list[tuple[str, str]] = []
        for index, old_name in enumerate(selected, start=1):
            try:
                new_name_proposed = build_name(prefix, descriptor, index)
            except ValueError as exc:
                print(f"  Skipping {old_name}: {exc}")
                continue

            if cmds is not None:
                new_name = cmds.rename(old_name, new_name_proposed)
            else:
                new_name = new_name_proposed

            rename_pairs.append((old_name, new_name))
            print(f"  {old_name}  →  {new_name}")

        # ------------------------------------------------------------------
        # TODO 3: Update self._status_label to display "X objects renamed".
        # ------------------------------------------------------------------
        self._status_label.setText(f"{len(rename_pairs)} object(s) renamed.")


def main() -> None:
    """Show the BatchRenameWindow."""
    if not _UI_AVAILABLE:
        print("Qt is not installed – cannot show UI.")
        return

    window = BatchRenameWindow(title="MDS Batch Rename")
    window.show_window()
    return window


if __name__ == "__main__":
    main()
