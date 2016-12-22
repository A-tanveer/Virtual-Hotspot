import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog

import MainUi
import clients
import ctypes

# http://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
myappid = 'SUST.Project_150.Tanveer\'s Hotspot'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# LandingPageUI, LandingPageBase = uic.loadUiType("clients.ui")
# http://stackoverflow.com/questions/41150669/open-second-window-from-main-with-pyqt5-and-qt-designer


class MainWindow (QMainWindow, MainUi.Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        MainUi.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.button_viewClient.clicked.connect(self.showClients)

    def showClients(self):
        self.child_win = showClientsList(self)
        self.child_win.show()


class showClientsList(QDialog, clients.Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

if __name__ == '__main__':

    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
