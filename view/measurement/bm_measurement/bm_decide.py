# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bm_decide.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets

from view.measurement.bm_measurement.bm_connection_tips import Ui_test
from view.measurement.bm_measurement.bm_manual import Ui_weight_manual
"""
Author: GRP group 14
"""

class Ui_weight_decide(object):
    def setup(self, weight_decide):
        weight_decide.setObjectName("Weight Data Source")
        weight_decide.resize(558, 495)
        self.pushButton = QtWidgets.QPushButton(weight_decide)
        self.pushButton.setGeometry(QtCore.QRect(150, 80, 261, 121))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton{\n"
                                         "    font-family: Arial;border: 1px solid  #292929;color: #292929; \n"
                                         "    font-weight: bold; font-size: 18px;\n"
                                         "}\n"
                                         "QPushButton:hover{                    \n"
                                         "    border: 0px solid7;\n"
                                         "    color:white;background: #292929;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    background:#353535;\n"
                                         "}")

        self.pushButton_2 = QtWidgets.QPushButton(weight_decide)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 290, 261, 131))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                         "    font-family: Arial;border: 1px solid  #292929;color: #292929; \n"
                                         "    font-weight: bold;font-size: 18px\n"
                                         "}\n"
                                         "QPushButton:hover{                    \n"
                                         "    border: 0px solid7;\n"
                                         "    color:white;background: #292929;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    background:#353535;\n"
                                         "}")

        self.retranslateUi(weight_decide)
        QtCore.QMetaObject.connectSlotsByName(weight_decide)
        self.pushButton.clicked.connect(self.open_weight_manual)
        self.pushButton_2.clicked.connect(self.open_bt_tips)

    def open_weight_manual(self):

        self.window = QtWidgets.QDialog()
        self.weight_manual = Ui_weight_manual()
        self.weight_manual.setup(self.window)
        self.window.show()
    #
    #
    # def open_weight_bt(self):
    #     self.window = QtWidgets.QDialog()
    #     self.weight_measure = Ui_Dialog()
    #     self.weight_measure.setup(self.window)
    #     self.window.show()

    def open_bt_tips(self):
        self.window = QtWidgets.QDialog()
        self.sub_bt_measure = Ui_test()
        self.sub_bt_measure.setup(self.window)
        self.window.show()

        # msg = QtWidgets.QMessageBox()
        # msg.setWindowTitle("New Weight Measurement")
        # msg.setText("You are starting a new weight measurement.\n connecting")
        # msg.setIcon(QtWidgets.QMessageBox.Information)
        #
        # msg.setStandardButtons(QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Yes)
        # msg.setDefaultButton(QtWidgets.QMessageBox.Yes)
        # x = msg.exec_()
        # scale_yunmai = Yunmai_scale()
        # print(scale_yunmai.weight)
        # scale_yunmai.weight
        # scale_yunmai.time
        # msg.setText(scale_yunmai.weight)
        # x = msg.exec_()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Weight Data Source"))
        self.pushButton.setText(_translate("Form", "Manual input"))
        self.pushButton_2.setText(_translate("Form", "Connect Bluetooth"))


if __name__ == "__main__":
     import sys
     app = QtWidgets.QApplication(sys.argv)
     weight_decide = QtWidgets.QDialog()
     ui = Ui_weight_decide()
     ui.setup(weight_decide)
     weight_decide.show()
     sys.exit(app.exec_())