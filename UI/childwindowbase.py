import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMdiSubWindow

class ChildWindowBase():
    
    def __init__(self, mainWindow, title= "Child Window", parent=None):
        self.sub = QMdiSubWindow()
        self.sub.setWindowTitle(title)
        self.parentWindow = mainWindow
        self.parentWindow.mdi.addSubWindow(self.sub)
        self.sub.showMaximized()
    
    def showWindow(self):
        self.sub.show()

    def closeWindow(self):
        self.sub.close()