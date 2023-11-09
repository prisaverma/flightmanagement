import sys
from childwindowbase import ChildWindowBase
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox

class SearchFlightWindow(ChildWindowBase):
    def __init__(self, mainWindow, title, parent=None):
        super().__init__(mainWindow, title, parent)
        self.initializeForm()


    def initializeForm(self):
        print('To Initialize Search Flight Form')