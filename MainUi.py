# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow2.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 450)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pass.setGeometry(QtCore.QRect(20, 290, 280, 30))
        self.lineEdit_pass.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "font: 75 10pt \"Segoe UI\";\n"
                                         "border-color: rgb(19, 118, 118);")
        self.lineEdit_pass.setClearButtonEnabled(True)
        self.lineEdit_pass.setObjectName("lineEdit_pass")

        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(190, 255, 110, 20))
        self.checkBox_2.setStyleSheet("font: 10pt \"Segoe UI\";\n"
                                      "color: rgb(30, 100, 100);")
        self.checkBox_2.setObjectName("checkBox_2")

        self.label_share = QtWidgets.QLabel(self.centralwidget)
        self.label_share.setGeometry(QtCore.QRect(230, 410, 81, 20))
        self.label_share.setOpenExternalLinks(True)
        self.label_share.setObjectName("label_share")

        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(90, 370, 140, 30))
        self.pushButton_start.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_start.setAutoFillBackground(False)
        self.pushButton_start.setStyleSheet("")
        self.pushButton_start.setObjectName("pushButton_start")

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
        self.button_viewClient.setAutoFillBackground(False)
        self.button_viewClient.setObjectName("button_viewClient")

        self.checkBox_1 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_1.setGeometry(QtCore.QRect(200, 40, 110, 20))
        self.checkBox_1.setStyleSheet("font: 10pt \"Segoe UI\";\n"
                                      "color: rgb(255, 255, 255);")
        self.checkBox_1.setObjectName("checkBox_1")

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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_pass.setText(_translate("MainWindow", "mYpassword"))
        self.checkBox_2.setText(_translate("MainWindow", "Show Password"))
        self.label_share.setText(_translate("MainWindow",
                                            "<html><head/><body><p><a href=\"google.com\"><span style=\" font-size:8pt; font-style:italic; text-decoration: underline; color:#fc5400;\">Share Internet</span></a></p></body></html>"))
        self.pushButton_start.setText(_translate("MainWindow", "Start Hotspot"))
        self.label_settings.setText(_translate("MainWindow",
                                               "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">Settings</span></p></body></html>"))
        self.lineEdit_ssid.setText(_translate("MainWindow", "My Hotspot"))
        self.label_passEd.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" color:#1e6464;\">Password</span></p></body></html>"))
        self.label_ssid.setText(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" color:#ffffff;\">Hotspot Name: V I P E R</span></p></body></html>"))
        self.label_pass.setText(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" color:#ffffff;\">Password: **********</span></p></body></html>"))
        self.label_num.setText(_translate("MainWindow",
                                          "<html><head/><body><p><span style=\" color:#ffffff;\">10 clients connected</span></p></body></html>"))
        self.button_viewClient.setText(_translate("MainWindow", "View Clients"))
        self.checkBox_1.setText(_translate("MainWindow", "Show Password"))
        self.label_status.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" color:#ffffff;\">Status: Not Started</span></p></body></html>"))
        self.label_ssidEd.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" color:#1e6464;\">Hotspot Name</span></p></body></html>"))
