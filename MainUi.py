# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow2.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

import threading
import sched
import time

from PyQt5 import QtCore, QtGui, QtWidgets

import HostedNetwork as hn
import CreateClientsGui

s = sched.scheduler(time.time, time.sleep)


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(320, 450)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        x = hn.check_drivers()
        if x != 'Yes':
            self.show_dialog_2()
            self.closeEvent()

        self.lineEdit_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pass.setGeometry(QtCore.QRect(20, 290, 280, 30))
        self.lineEdit_pass.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "font: 75 10pt \"Segoe UI\";\n"
                                         "border-color: rgb(255, 255, 255);")
        self.lineEdit_pass.setClearButtonEnabled(True)
        self.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.lineEdit_pass.textEdited.connect(self.set_button_name)

        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(190, 255, 110, 20))
        self.checkBox_2.setStyleSheet("font: 10pt \"Segoe UI\";\n"
                                      "color: rgb(30, 100, 100);")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.stateChanged.connect(self.changeTextEdit)

        self.label_share = QtWidgets.QLabel(self.centralwidget)
        self.label_share.setGeometry(QtCore.QRect(230, 410, 81, 20))
        self.label_share.setOpenExternalLinks(True)
        self.label_share.setObjectName("label_share")

        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(90, 370, 140, 30))
        self.pushButton_start.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_start.setAutoFillBackground(False)
        self.pushButton_start.setStyleSheet("background-color: rgb(30, 100, 100); color: white")
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_start.clicked.connect(self.startStop)

        self.label_settings = QtWidgets.QLabel(self.centralwidget)
        self.label_settings.setGeometry(QtCore.QRect(0, 100, 320, 30))
        self.label_settings.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_settings.setObjectName("label_settings")

        self.lineEdit_ssid = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ssid.setGeometry(QtCore.QRect(20, 200, 280, 30))
        self.lineEdit_ssid.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "font: 75 10pt \"Segoe UI\";\n"
                                         "border-color: rgb(19, 118, 118);")
        self.lineEdit_ssid.setClearButtonEnabled(True)
        self.lineEdit_ssid.setObjectName("lineEdit_ssid")
        self.lineEdit_ssid.textEdited.connect(self.set_button_name)

        self.label_passEd = QtWidgets.QLabel(self.centralwidget)
        self.label_passEd.setGeometry(QtCore.QRect(20, 250, 161, 30))
        self.label_passEd.setStyleSheet("font: 75 12pt \"Segoe UI\" white;")
        self.label_passEd.setObjectName("label_passEd")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 320, 100))
        self.frame.setStyleSheet("font:10pt \"Segoe UI\";\n"
                                 "background-color: rgb(30, 100, 100);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label_ssid = QtWidgets.QLabel(self.frame)
        self.label_ssid.setGeometry(QtCore.QRect(10, 10, 180, 20))
        self.label_ssid.setObjectName("label_ssid")

        self.label_pass = QtWidgets.QLabel(self.frame)
        self.label_pass.setGeometry(QtCore.QRect(10, 40, 160, 20))
        self.label_pass.setObjectName("label_pass")

        self.label_num = QtWidgets.QLabel(self.frame)
        self.label_num.setGeometry(QtCore.QRect(10, 70, 160, 20))
        self.label_num.setObjectName("label_num")

        self.button_viewClient = QtWidgets.QPushButton(self.frame)
        self.button_viewClient.setGeometry(QtCore.QRect(200, 70, 110, 20))
        self.button_viewClient.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_viewClient.setStyleSheet("background-color: white; color: rgb(30, 100, 100)")
        self.button_viewClient.setAutoFillBackground(False)
        self.button_viewClient.setObjectName("button_viewClient")

        self.checkBox_1 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_1.setGeometry(QtCore.QRect(200, 40, 110, 20))
        self.checkBox_1.setStyleSheet("font: 10pt \"Segoe UI\";\n"
                                      "color: rgb(255, 255, 255);")
        self.checkBox_1.setObjectName("checkBox_1")
        self.checkBox_1.stateChanged.connect(self.changeLabel)

        self.label_status = QtWidgets.QLabel(self.frame)
        self.label_status.setGeometry(QtCore.QRect(200, 10, 110, 20))
        self.label_status.setObjectName("label_status")

        self.label_ssidEd = QtWidgets.QLabel(self.centralwidget)
        self.label_ssidEd.setGeometry(QtCore.QRect(20, 160, 181, 30))
        self.label_ssidEd.setStyleSheet("font: 75 12pt \"Segoe UI\" white;")
        self.label_ssidEd.setObjectName("label_ssidEd")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tanveer's wifi Hotspot"))
        MainWindow.setWindowIcon(QtGui.QIcon('logo.png'))

        self.lineEdit_pass.setText(_translate("MainWindow", hn.get_password()))
        self.lineEdit_ssid.setText(_translate("MainWindow", hn.get_name()))

        self.checkBox_2.setText(_translate("MainWindow", "Show Password"))

        self.label_share.setText(_translate("MainWindow", "<html><head/><body><p>"
                                                          "<a href=\"shareIntarnet.html\"><span style=\""
                                                          " font-size:8pt; font-style:italic; text-decoration: "
                                                          "underline; color:#fc5400;\">Share Internet</span>"
                                                          "</a></p></body></html>"))

        self.set_button_name()

        self.label_settings.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\""
                                                             " font-size:14pt; color:#ffffff;\">Settings</span>"
                                                             "</p></body></html>"))

        self.label_passEd.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#1e6464;\">"
                                                           "Password</span></p></body></html>"))

        self.label_ssid.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">"
                                                         "SSID: " + hn.get_name() + "</span></p></body></html>"))

        self.label_pass.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">"
                                                         "Password: ********</span></p></body></html>"))

        # if hn.get_no_connected_client() != 'None':
        #     self.label_num.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">" +
        #                                       hn.get_no_connected_client() + " connected</span></p></body></html>"))
        # else:
        #     self.label_num.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">"
        #                                                     "</span></p></body></html>"))
        self.update_client_no()

        self.button_viewClient.setText(_translate("MainWindow", "View Clients"))

        self.checkBox_1.setText(_translate("MainWindow", "Show Password"))

        status = hn.check_status()
        if status != 'Started':
            self.label_status.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">"
                                                               "Status: Not Started</span></p></body></html>"))
        else:
            self.label_status.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">"
                                                               "Status: Started</span></p></body></html>"))

        self.label_ssidEd.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#1e6464;\">"
                                                           "Hotspot Name</span></p></body></html>"))

    def update_client_no(self):

        threading.Timer(10.0, self.update_client_no).start()  # will check every 10 second for client no change

        _translate = QtCore.QCoreApplication.translate
        # this thing needed to be updated dynamically
        if hn.get_no_connected_client() != 'None':
            self.label_num.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">" +
                                              hn.get_no_connected_client() + " connected</span></p></body></html>"))
        else:
            self.label_num.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">"
                                                            "</span></p></body></html>"))

    def changeLabel(self, state):
        _translate = QtCore.QCoreApplication.translate
        passwd = hn.get_password()
        if state == QtCore.Qt.Checked:
            self.label_pass.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">"
                                                       "Password: " + passwd + "</span></p></body></html>"))
        else:
            self.label_pass.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">"
                                                       "Password: ********</span></p></body></html>"))

    def changeTextEdit(self, state):
        if state == QtCore.Qt.Checked:
            self.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)

    def startStop(self):

        ssid = self.lineEdit_ssid.text()
        passwd = self.lineEdit_pass.text()

        task = self.pushButton_start.text()

        if task == 'Stop Hotspot':
            hn.hosted_network_stop()
            self.update_ui()
        else:
            if len(passwd) < 8 or ' ' in passwd or ssid.startswith(' ') or ssid.startswith('"'):
                self.show_dialog()
            else:
                hn.hosted_network_create(ssid, passwd)
                hn.hosted_network_start()
                self.update_ui()

    def update_ui(self):
        _translate = QtCore.QCoreApplication.translate
        CreateClientsGui.create_gui()
        self.set_button_name()
        self.lineEdit_pass.setText(_translate("MainWindow", hn.get_password()))
        self.lineEdit_ssid.setText(_translate("MainWindow", hn.get_name()))
        self.label_ssid.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">"
                                                         "SSID: " + hn.get_name() + "</span></p></body></html>"))
        status = hn.check_status()
        if status != 'Started':
            self.label_status.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">"
                                                               "Status: Not Started</span></p></body></html>"))
        else:
            self.label_status.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">"
                                                               "Status: Started</span></p></body></html>"))

    def set_button_name(self):

        _translate = QtCore.QCoreApplication.translate

        status = hn.check_status()
        if status != 'Started':
            self.pushButton_start.setText(_translate("MainWindow", "Start Hotspot"))
        else:
            ssid = self.lineEdit_ssid.text()
            passwd = self.lineEdit_pass.text()

            name = hn.get_name()
            password = hn.get_password()

            if ssid == name and passwd == password:
                self.pushButton_start.setText(_translate("MainWindow", "Stop Hotspot"))

            elif ssid != name or password != passwd:
                self.pushButton_start.setText(_translate("MainWindow", "Apply Settings"))

    def show_dialog(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("""password must be 8-15 characters long and can't contain spaces
            Hotspot name can't start with a 'space' or a '"'""")
        msg.setWindowIconText('Error')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def show_dialog_2(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("""
        Your device or driver doesn't support virtual wifi hotspot\t
        """)
        msg.setWindowIconText('Error')
        msg.setStandardButtons(QtWidgets.QMessageBox.Abort)
        msg.exec_()

    def closeEvent(self, event):
        # override closeEvent method to close running threads when X button is pressed
        self.stylusProximityControlOff()
        self.deleteLater()
