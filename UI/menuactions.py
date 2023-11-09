import common
from addflight import AddFlightWindow
from searchflight import SearchFlightWindow
from childwindowbase import ChildWindowBase

def addFlightClicked(mainWindow):
    common.showMessage('Add Flight Menu Item Clicked....')
    addFlightWindow = AddFlightWindow(mainWindow, "Add Flight")
    addFlightWindow.showWindow()

def searchFlightClicked(mainWindow):
    common.showMessage('Search Flight Clicked!')
    childWindow = SearchFlightWindow(mainWindow, "Search Flights...")
    childWindow.showWindow()
