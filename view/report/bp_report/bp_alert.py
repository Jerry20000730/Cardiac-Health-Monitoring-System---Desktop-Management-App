# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bp_alert.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

"""
Author: GRP group 14
"""
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_bp_alert(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(472, 267)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 471, 271))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 60, 421, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(150, 190, 171, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    font-family: Arial;border: 1px solid  #292929;color: #292929; \n"
                                      "    font-size: 14px; font-weight: bold;\n"
                                      "}\n"
                                      "QPushButton:hover{                    \n"
                                      "    border: 0px solid7;\n"
                                      "    color:white;background: #292929;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "    background:#353535;\n"
                                      "}")
        self.pushButton.clicked.connect((Dialog.close))
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(220, 130, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Alert"))
        self.label.setText(_translate("Dialog", "You haven\'t measure your\n"
"blood pressure today!"))
        self.pushButton.setText(_translate("Dialog", "New Measurement"))
        self.label_2.setText(_translate("Dialog", "☺"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_bp_alert()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
