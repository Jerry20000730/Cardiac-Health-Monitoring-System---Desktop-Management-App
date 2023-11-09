

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bp_measure.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys

from controller.data_io import DataIO
from controller.utility import Utility
from model.global_var import GlobalVar
import view.measurement.bp_meamurement.bp_tip
from PyQt5 import QtCore, QtGui, QtWidgets
"""
Author: GRP group 14
"""
class Ui_bp_measure(object):

    def setup(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(495, 420)

        self.okay_button = QtWidgets.QPushButton(Dialog)
        self.okay_button.setGeometry(QtCore.QRect(130, 340, 100, 32))
        self.okay_button.setObjectName("okay_button")
        self.okay_button.setText("Okay")
        self.okay_button.setStyleSheet("QPushButton{\n"
                                     "    font-family: Arial;border: 1px solid  #292929;color: #292929; \n"
                                     "    font-weight: bold;\n"
                                     "}\n"
                                     "QPushButton:hover{                    \n"
                                     "    border: 0px solid7;\n"
                                     "    color:white;background: #292929;\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "    background:#353535;\n"
                                     "}")
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(270, 340, 100, 32))
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.setText("Cancel")
        self.cancel_button.setStyleSheet("QPushButton{\n"
                                     "    font-family: Arial;border: 1px solid  #292929;color: #292929; \n"
                                     "    font-weight: bold;\n"
                                     "}\n"
                                     "QPushButton:hover{                    \n"
                                     "    border: 0px solid7;\n"
                                     "    color:white;background: #292929;\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "    background:#353535;\n"
                                     "}")

        self.notice_label = QtWidgets.QLabel(Dialog)
        self.notice_label.setGeometry(QtCore.QRect(80, 30, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.notice_label.setFont(font)
        self.notice_label.setObjectName("notice_label")
        self.notice_label.setStyleSheet("font-family: Arial;color: #292929; \n")
        self.tips_label = QtWidgets.QLabel(Dialog)
        self.tips_label.setGeometry(QtCore.QRect(120, 70, 231, 51))
        self.tips_label.setStyleSheet("color:#2d4bdf;")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setWeight(75)
        self.tips_label.setFont(font)
        self.tips_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tips_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tips_label.setObjectName("tips_label")
        self.dias_label = QtWidgets.QLabel(Dialog)
        self.dias_label.setGeometry(QtCore.QRect(120, 150, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.dias_label.setFont(font)
        self.dias_label.setObjectName("dias_label")
        self.dias_label.setStyleSheet("font-family: Arial;color: #292929; \n")
        self.sys_label = QtWidgets.QLabel(Dialog)
        self.sys_label.setGeometry(QtCore.QRect(120, 230, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.sys_label.setFont(font)
        self.sys_label.setObjectName("sys_label")
        self.sys_label.setStyleSheet("font-family: Arial;color: #292929; \n")

        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(250, 140, 101, 41))
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(250, 230, 101, 41))
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit_2.setObjectName("textEdit_2")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(20)
        self.diastolic_label = QtWidgets.QLabel(Dialog)
        self.diastolic_label.setGeometry(QtCore.QRect(150, 190, 181, 16))
        self.diastolic_label.setWordWrap(True)
        self.diastolic_label.setAlignment(QtCore.Qt.AlignCenter)
        self.diastolic_label.setObjectName("diastolic_label")
        self.diastolic_label.setFont(font)
        self.diastolic_label.setStyleSheet("color:#2d4bdf;")

        self.systolic_label = QtWidgets.QLabel(Dialog)
        self.systolic_label.setGeometry(QtCore.QRect(150, 280, 181, 16))
        self.systolic_label.setWordWrap(True)
        self.systolic_label.setAlignment(QtCore.Qt.AlignCenter)
        self.systolic_label.setObjectName("systolic_label")
        self.systolic_label.setFont(font)
        self.systolic_label.setStyleSheet("color:#2d4bdf;")

        self.textEdit.textChanged.connect(lambda: self.update_text("diastolic"))
        self.textEdit_2.textChanged.connect(lambda: self.update_text("systolic"))

        self.retranslateUi(Dialog)

        self.okay_button.clicked.connect(lambda: self.accept_check(Dialog))
        self.cancel_button.clicked.connect(lambda: self.close_current_window(Dialog))

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def update_text(self, type):

        if type == "diastolic":
            diastolic_value = self.textEdit.toPlainText()
            self.diastolic_label.setText(Utility.check_input_value(diastolic_value, "diastolic"))

        elif type == "systolic":
            systolic_value = self.textEdit_2.toPlainText()
            self.systolic_label.setText(Utility.check_input_value(systolic_value, "systolic"))

    def accept_bp(self, current_window, diastolic_value, systolic_value):

        a_bp1_final = float(diastolic_value)
        a_bp2_final = float(systolic_value)

        DataIO.save_bp_temp(a_bp1_final, a_bp2_final)
        DataIO.send_bp_to_db(a_bp1_final, a_bp2_final)
        # GlobalVar.set_value("dict", "new_BP_meas", True)

        # GlobalVar.set_value("dict", "new_BP_meas", False)

        if GlobalVar.get_repeat_time() >= 3:
            GlobalVar.reset_repeat_time()
            DataIO.refresh_BP_plot_file("new")
            DataIO.refresh_BP_plot_file("history")
            self.close_current_window(current_window)
        else:
            GlobalVar.increase_repeat_time()
            self.close_current_window(current_window)
            self.open_bp_tips()

    def accept_check(self, current_window):

        diastolic_value = self.textEdit.toPlainText()
        systolic_value = self.textEdit_2.toPlainText()

        if Utility.check_input_value(diastolic_value, "diastolic") == "Okay." and Utility.check_input_value(
                systolic_value, "systolic") == "Okay.":
            self.accept_bp(current_window, diastolic_value, systolic_value)
        else:
            self.messageDialog()

        self.diastolic_label.setText(Utility.check_input_value(diastolic_value, "diastolic"))
        self.systolic_label.setText(Utility.check_input_value(systolic_value, "systolic"))

    def messageDialog(self):
        self.msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning,
                                             "Warning",
                                             "The input blood pressure values are invalid! Please try again!")
        self.msg_box.exec_()

    def close_current_window(self, current_window):
        current_window.close()

    def open_bp_tips(self):

        self.window = QtWidgets.QDialog()
        self.sub_bp_measure = view.measurement.bp_meamurement.bp_tip.Ui_bp_tips()
        self.sub_bp_measure.setup(self.window)
        self.window.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Blood Pressure (Manually Input)"))
        self.notice_label.setText(_translate("Dialog", "Please enter your blood pressure"))
        self.tips_label.setText(_translate("Dialog", "Tips: Have a 5-minute break\n"
                                                     " before you measure"))
        self.dias_label.setText(_translate("Dialog", "Diastolic:"))
        self.sys_label.setText(_translate("Dialog", "Systolic:"))
        self.diastolic_label.setText(_translate("Dialog", "Please enter the value"))
        self.systolic_label.setText(_translate("Dialog", "Please enter the value"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    bp_measure = QtWidgets.QDialog()
    ui = Ui_bp_measure()
    ui.setup(bp_measure)
    bp_measure.show()
    sys.exit(app.exec_())