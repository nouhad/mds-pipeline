"""Base window class for MDS tools.

Qt compatibility notes:
- Maya 2024 ships with **PySide2** (Qt 5).
- Maya 2025+ ships with **PySide6** (Qt 6).

This module tries PySide2 first, then PySide6.  If neither is installed (e.g. in a
headless CI environment) a ``_DummyWidget`` base class is used so that the module
can still be imported and tools can be tested without a display.

To create a custom tool window, subclass ``BaseWindow`` and override
``buildUi()``::

    class MyTool(BaseWindow):
        def buildUi(self):
            btn = QPushButton("Do Thing")
            btn.clicked.connect(self._doThing)
            self._layout.addWidget(btn)

        def _doThing(self):
            print("doing the thing")

    # In Maya or a standalone Qt application:
    win = MyTool(title="My Tool")
    win.showWindow()
"""

try:
    from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton  # type: ignore[import]

    _QT_AVAILABLE = True
    _QT_VERSION = "PySide2"
except ImportError:
    try:
        from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton  # type: ignore[import]

        _QT_AVAILABLE = True
        _QT_VERSION = "PySide6"
    except ImportError:
        _QT_AVAILABLE = False
        _QT_VERSION = None

        class QWidget:  # type: ignore[no-redef]
            """Dummy base class used when no Qt installation is present."""

            def __init__(self, parent=None):
                self._parent = parent

            def setWindowTitle(self, title: str) -> None:  # noqa: N802
                pass

            def show(self) -> None:
                pass

        class QVBoxLayout:  # type: ignore[no-redef]
            def __init__(self, parent=None):
                pass

            def addWidget(self, widget) -> None:  # noqa: N802
                pass

        class QPushButton:  # type: ignore[no-redef]
            def __init__(self, label: str = "", parent=None):
                self.label = label

            @property
            def clicked(self):
                return _DummySignal()

        class _DummySignal:
            def connect(self, slot) -> None:
                pass


class BaseWindow(QWidget):
    """Reusable base class for all MDS tool windows.

    Subclass this and implement :meth:`buildUi` to add widgets to
    ``self._layout``.

    Args:
        title: Window title bar text.
        parent: Optional Qt parent widget (use Maya's main window in production).
    """

    def __init__(self, title: str = "MDS Tool", parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self._layout = QVBoxLayout(self)
        self.buildUi()

    def buildUi(self) -> None:
        """Populate the window with widgets.

        Raises:
            NotImplementedError: Subclasses must override this method.
        """
        raise NotImplementedError(
            f"{type(self).__name__} must implement buildUi()"
        )

    def showWindow(self) -> None:
        """Make the window visible."""
        self.show()
