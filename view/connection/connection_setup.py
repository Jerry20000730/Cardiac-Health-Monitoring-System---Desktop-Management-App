# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connection_setup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.pyplot import inferno
from model.global_var import GlobalVar
"""
Author: GRP group 14
"""
class Ui_Dialog(object):
    def setup(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(414, 310)
        self.host_edit = QtWidgets.QPlainTextEdit(Dialog)
        self.host_edit.setGeometry(QtCore.QRect(60, 100, 281, 31))
        self.host_edit.setObjectName("host_edit")
        self.host_label = QtWidgets.QLabel(Dialog)
        self.host_label.setGeometry(QtCore.QRect(60, 40, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.host_label.setFont(font)
        self.host_label.setObjectName("host_label")
        self.port_label = QtWidgets.QLabel(Dialog)
        self.port_label.setGeometry(QtCore.QRect(60, 150, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.port_label.setFont(font)
        self.port_label.setObjectName("port_label")
        self.port_edit = QtWidgets.QPlainTextEdit(Dialog)
        self.port_edit.setGeometry(QtCore.QRect(60, 210, 281, 31))
        self.port_edit.setPlainText("")
        self.port_edit.setOverwriteMode(False)
        self.port_edit.setObjectName("port_edit")
        self.host_combobox = QtWidgets.QComboBox(Dialog)
        self.host_combobox.setGeometry(QtCore.QRect(60, 70, 281, 26))
        self.host_combobox.setObjectName("host_combobox")
        self.host_combobox.addItem("")
        self.port_combobox = QtWidgets.QComboBox(Dialog)
        self.port_combobox.setGeometry(QtCore.QRect(60, 180, 281, 26))
        self.port_combobox.setObjectName("port_combobox")
        self.port_combobox.addItem("")
        self.port_combobox.addItem("")
        self.okay_button = QtWidgets.QPushButton(Dialog)
        self.okay_button.setGeometry(QtCore.QRect(90, 270, 113, 32))
        self.okay_button.setObjectName("okay_button")
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(210, 270, 113, 32))
        self.cancel_button.setObjectName("cancel_button")
        
        self.okay_button.clicked.connect(self.update_connection_setup)
        self.okay_button.clicked.connect(lambda: self.close_current_window(Dialog))
        self.cancel_button.clicked.connect(lambda: self.close_current_window(Dialog))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def update_connection_setup(self):
        
        host_combobox_value = self.host_combobox.currentText()
        print(host_combobox_value)
        if host_combobox_value != "Manually Input":
            host_value = host_combobox_value
        else:
            host_value = self.host_edit.toPlainText()
        try:
            print(host_value)
            GlobalVar.set_value("client", "client_host", host_value)
        except Exception as err:
            print("[Error] {info}".format(info = err))
        
        port_combobox_value = self.port_combobox.currentText()
        if port_combobox_value != "Manually Input":
            port_value = port_combobox_value
        else:
            port_value = self.port_edit.toPlainText()
        try:
            GlobalVar.set_value("client", "client_port", int(port_value))
        except Exception as err:
            print("[Error] {info}".format(info = err))
            
    def close_current_window(self, current_window):
        current_window.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Connection Setting"))
        self.host_label.setText(_translate("Dialog", "Client Host Address:"))
        self.port_label.setText(_translate("Dialog", "Client Port Address:"))
        self.host_combobox.setItemText(0, _translate("Dialog", "Manually Input"))
        self.port_combobox.setItemText(0, _translate("Dialog", "7801"))
        self.port_combobox.setItemText(1, _translate("Dialog", "Manually Input"))
        self.okay_button.setText(_translate("Dialog", "Okay"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))

