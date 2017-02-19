import ctypes
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog

import CreateClientsGui
import MainUi

CreateClientsGui.create_gui()

import clients

myappid = 'SUST.Project_150.Tanveer\'s Hotspot'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)



class MainWindow(QMainWindow, MainUi.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        MainUi.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.button_viewClient.clicked.connect(self.showClients)

    def showClients(self):
        CreateClientsGui.create_gui()
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
