# 3D2G04A_3DScripting: Day 04
# Task 01: Simple UI
# Description: Build a minimal window with a single button that prints a message when clicked.

from mds.ui.base_window import BaseWindow, QPushButton


class HelloWindow(BaseWindow):

    def build_ui(self):
        btn = QPushButton("Hello from UI")
        btn.clicked.connect(self._on_hello)
        self._layout.addWidget(btn)

    def _on_hello(self):
        print("Hello from Maya UI!")


window = HelloWindow(title="MDS Day 04 - Hello UI")
window.show_window()

