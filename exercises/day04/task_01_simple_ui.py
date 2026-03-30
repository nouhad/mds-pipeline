"""Day 04 – Task 01 – Simple UI.

Build a minimal window with a single button that prints a message when clicked.
Demonstrates subclassing BaseWindow and connecting Qt signals.
"""

try:
    from mds.ui.base_window import BaseWindow, QPushButton
    _UI_AVAILABLE = True
except Exception:
    _UI_AVAILABLE = False
    BaseWindow = object  # type: ignore[assignment,misc]


# ------------------------------------------------------------------
# TODO 1: Subclass BaseWindow to create your own tool window.
#         The class below is a stub – fill in the implementation.
# ------------------------------------------------------------------
class HelloWindow(BaseWindow):
    """A minimal window with one button."""

    def build_ui(self) -> None:
        """Populate the window with a single greeting button.

        This method is called automatically by BaseWindow.__init__.
        Add widgets to self._layout.
        """

        # --------------------------------------------------------------
        # TODO 2: Create a QPushButton with the label "Hello from UI".
        #         Add it to self._layout using self._layout.addWidget(btn).
        # --------------------------------------------------------------
        btn = QPushButton("Hello from UI")
        self._layout.addWidget(btn)

        # --------------------------------------------------------------
        # TODO 3: Connect the button's clicked signal to a method.
        #         btn.clicked.connect(self._on_hello)
        #         Implement _on_hello below so it prints a greeting message.
        # --------------------------------------------------------------
        btn.clicked.connect(self._on_hello)

    def _on_hello(self) -> None:
        """Called when the Hello button is clicked."""
        # TODO: replace this with a real greeting message
        print("TODO: print your greeting message here")


def main() -> None:
    """Create and show the HelloWindow."""
    if not _UI_AVAILABLE:
        print("Qt (PySide2 or PySide6) is not installed – cannot show UI.")
        return

    # ------------------------------------------------------------------
    # TODO 4: Instantiate HelloWindow and call show_window().
    #         Provide a meaningful title string.
    # ------------------------------------------------------------------
    window = HelloWindow(title="MDS Day 04 – Hello UI")
    window.show_window()
    return window  # return so Maya keeps a reference and the window stays open


if __name__ == "__main__":
    main()
