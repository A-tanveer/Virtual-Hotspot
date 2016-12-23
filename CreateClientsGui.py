import HostedNetwork


def create_gui():

    string = """from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")"""

    host_list = HostedNetwork.get_ip_mac()
    num_client = len(host_list)
    # num_client = 2
    x = 60 + num_client * 45
    string += "\n        Dialog.resize(350, " + repr(x) + ")\n"
    string += """
        self.frame_x = QtWidgets.QFrame(Dialog)
        self.frame_x.setGeometry(QtCore.QRect(0, 0, 350, 60))
        self.frame_x.setStyleSheet("font:10pt \\\"Segoe UI\\\";\\nbackground-color: rgb(30, 100, 100);")
        self.frame_x.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_x.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_x.setObjectName("frame_x")
        self.label_name_2 = QtWidgets.QLabel(self.frame_x)
        self.label_name_2.setGeometry(QtCore.QRect(10, 0, 331, 41))
        self.label_name_2.setObjectName("label_name_2")
        self.label_num_2 = QtWidgets.QLabel(self.frame_x)
        self.label_num_2.setGeometry(QtCore.QRect(10, 30, 321, 21))
        self.label_num_2.setObjectName("label_num_2")\n"""

    for x in range(num_client):
        y = 65 + 45 * x
        string += "\n        self.frame_" + repr(x) + " = QtWidgets.QFrame(Dialog)" + \
                  "\n        self.frame_" + repr(x) + ".setGeometry(QtCore.QRect(0, " + repr(y) + ", 350, 40))" + \
                  "\n        self.frame_" + repr(x) + ".setAutoFillBackground(False)" + \
                  "\n        self.frame_" + repr(x) + ".setStyleSheet(\"font:10pt \\\"Segoe UI\\\";\\nbackground-color:" \
                                                  " rgb(209, 209, 209);\")" + \
                  "\n        self.frame_" + repr(x) + ".setFrameShape(QtWidgets.QFrame.StyledPanel)" + \
                  "\n        self.frame_" + repr(x) + ".setFrameShadow(QtWidgets.QFrame.Raised)" + \
                  "\n        self.frame_" + repr(x) + ".setObjectName(\"frame_" + repr(x) + "\")\n" + \
                  "\n        self.label_h" + repr(x) + " = QtWidgets.QLabel(self.frame_" + repr(x) + ")" + \
                  "\n        self.label_h" + repr(x) + ".setGeometry(QtCore.QRect(10, 0, 350, 21))" + \
                  "\n        self.label_h" + repr(x) + ".setObjectName(\"label_h" + repr(x) + "\")" + \
                  "\n        self.label_i" + repr(x) + " = QtWidgets.QLabel(self.frame_" + repr(x) + ")" + \
                  "\n        self.label_i" + repr(x) + ".setGeometry(QtCore.QRect(10, 20, 111, 16))" + \
                  "\n        self.label_i" + repr(x) + ".setObjectName(\"label_i" + repr(x) + "\")" + \
                  "\n        self.label_m" + repr(x) + " = QtWidgets.QLabel(self.frame_" + repr(x) + ")" + \
                  "\n        self.label_m" + repr(x) + ".setGeometry(QtCore.QRect(180, 20, 151, 16))" + \
                  "\n        self.label_m" + repr(x) + ".setObjectName(\"label_m" + repr(x) + "\")\n"

    name = HostedNetwork.get_name()

    string += """
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate\n
        Dialog.setWindowTitle(_translate("Dialog", "Connected Clients"))

        self.label_name_2.setText(_translate("Dialog", "<html><head/><body><p align=\\\"center\\\"><span style=\\\" font-size:14pt; color:#ffffff;\\\">Hotspot Name: """
    string += name

    string += """"
                                                       "</span></p></body></html>"))
        self.label_num_2.setText(_translate("Dialog", "<html><head/><body><p align=\\\"center\\\"><span style=\\\" color:"
                                                      "#ffffff;\\\">Clients Connected: """
    string += repr(num_client)
    string += """</span></p></body></html>"))

"""
    for x in range(num_client):
        host = host_list[x]
        mac = host[1]
        hostname = host[2]
        ip = host[0]

        string += "        self.label_h" + repr(x) + ".setText(_translate(\"Dialog\", \"<html><head/><body><p><span style=\\\" color:#1e6464;\\\">"
        string += hostname
        string += """</span></p></body></html>"))
        self.label_i""" + repr(x) + """.setText(_translate("Dialog", "<html><head/><body><p><span style=\\\" color:#000000;\\\">IP: """
        string += ip
        string += """</span></p></body></html>"))
        self.label_m""" + repr(x) + """.setText(_translate("Dialog", "<html><head/><body><p><span style=\\\" font-size:10pt; "
                                                  "color:#000000;\\\">MAC: """
        string += mac + "</span></p></body></html>\"))\n\n"

    f = open('clients.py', 'w')
    f.write(string)
    f.close()

