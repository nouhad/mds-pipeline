# 3D2G04A_3DScripting: Day 04
# Task 01: Simple UI
# Description: Build a minimal window with a single button that prints a message when clicked.

from mds.ui.baseWindow import BaseWindow, QPushButton


class HelloWindow(BaseWindow):

    def buildUi(self):
        btn = QPushButton("Hello from UI")
        btn.clicked.connect(self._onHello)
        self._layout.addWidget(btn)

    def _onHello(self):
        print("Hello from Maya UI!")


window = HelloWindow(title="MDS Day 04 - Hello UI")
window.showWindow()

