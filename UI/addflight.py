import sys
from childwindowbase import ChildWindowBase
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox

class AddFlightWindow(ChildWindowBase):
    def __init__(self, mainWindow, title= "Child Window", parent=None):
        super().__init__(mainWindow, title, parent)
        self.initializeForm()


    def initializeForm(self):
        print('ToInitialize Add Flight Form')