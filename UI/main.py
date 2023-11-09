import sys
import menuactions
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, QMdiArea

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.mdi = QMdiArea()
        self.setWindowTitle("Flight Management System")
        self.setCentralWidget(self.mdi)
        self._createMenuItems()
        self._createActionsForMenu()
        self._attachActionsToMenu()
        self._createMenuBar()
        self.showMaximized()
    
    def _createMenuItems(self):
        self.flightsMenu = QMenu("&Flight")
        self.passengerMenu = QMenu("&Passenger")
        self.bookingMenu = QMenu("&Booking")

    def _createActionsForMenu(self):
        self.addFlightAction = QAction("&Add", self)
        self.addFlightAction.triggered.connect(lambda: menuactions.addFlightClicked(self))
        self.searchFlightAction = QAction("&Search", self)
        self.searchFlightAction.triggered.connect(lambda: menuactions.searchFlightClicked(self))

    def _attachActionsToMenu(self):
        self.flightsMenu.addAction(self.addFlightAction)
        self.flightsMenu.addAction(self.searchFlightAction)
    
    def _createMenuBar(self):
        menuBar = self.menuBar()
        menuBar.addMenu(self.flightsMenu)
        menuBar.addMenu(self.passengerMenu)
        menuBar.addMenu(self.bookingMenu)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
