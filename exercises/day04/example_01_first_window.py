# 3D2G04A_3DScripting: Day 04
# Example 01: Your First Window in Maya
# Description: Learn what PySide6 and Qt are, and get a basic window open inside Maya.

# PySide6 is the Python library that lets us build UIs using the Qt framework inside Maya 2025.
# Qt is a C++ framework for building UIs. PySide6 is the Python version of that.
# Every element in a Qt UI is called a widget - windows, buttons, labels are all widgets.
# QMainWindow is the top level window widget.
# QWidget is the base class for all UI elements.
# QVBoxLayout stacks widgets vertically.
# QPushButton is a clickable button widget.

from PySide6 import QtWidgets
from shiboken6 import wrapInstance
import maya.OpenMayaUI as omui

def get_maya_main_window():
    ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(ptr), QtWidgets.QWidget)


class Example01Window(QtWidgets.QMainWindow):
    def __init__(self, parent=get_maya_main_window()):
        super().__init__(parent)
        self.setWindowTitle("Example 01 - First Window")
        self.resize(400, 200)
        self.setup_ui()

    def setup_ui(self):
        central = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(central)

        button = QtWidgets.QPushButton("Click Me")
        layout.addWidget(button)

        self.setCentralWidget(central)


ui = Example01Window()
ui.show()