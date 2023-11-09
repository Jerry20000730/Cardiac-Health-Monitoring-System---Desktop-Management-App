# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bp_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

# ! [START] import customized packages
# TODO: transfer these codes into the updated UI file

# ! [END] import customized packages
from controller.database_io import db_query_data
from controller.graph_producer import plot_controller

"""
Author: GRP group 14
"""
class Ui_bp_window(object):
    def setup(self, bp_window):
        bp_window.setObjectName("bp_window")
        bp_window.resize(810, 797)
        self.tabWidget = QtWidgets.QTabWidget(bp_window)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 811, 721))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.bp_tab_1 = QtWidgets.QWidget()
        self.bp_tab_1.setObjectName("bp_tab_1")
        self.bp_figure = QtWidgets.QLabel(self.bp_tab_1)
        self.bp_figure.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.bp_figure.setText("")
        self.bp_figure.setPixmap(QtGui.QPixmap("view/img/graph/bp_day.png"))
        self.bp_figure.setScaledContents(True)
        self.bp_figure.setWordWrap(False)
        self.bp_figure.setObjectName("bp_figure")
        self.frame = QtWidgets.QFrame(self.bp_tab_1)
        self.frame.setGeometry(QtCore.QRect(190, 530, 461, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.diastolic_label = QtWidgets.QLabel(self.frame)
        self.diastolic_label.setGeometry(QtCore.QRect(10, 0, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.diastolic_label.setFont(font)
        self.diastolic_label.setStyleSheet("font-size:22px")
        self.diastolic_label.setObjectName("diastolic_label")
        self.systolic_label = QtWidgets.QLabel(self.frame)
        self.systolic_label.setGeometry(QtCore.QRect(220, 0, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.systolic_label.setFont(font)
        self.systolic_label.setStyleSheet("font-size:22px")
        self.systolic_label.setObjectName("systolic_label")
        self.diastolic_value = QtWidgets.QLabel(self.frame)
        self.diastolic_value.setGeometry(QtCore.QRect(120, 0, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.diastolic_value.setFont(font)
        self.diastolic_value.setStyleSheet("font-size:18px")
        self.diastolic_value.setObjectName("diastolic_value")
        self.systolic_value = QtWidgets.QLabel(self.frame)
        self.systolic_value.setGeometry(QtCore.QRect(330, 0, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.systolic_value.setFont(font)
        self.systolic_value.setStyleSheet("font-size:18px")
        self.systolic_value.setObjectName("systolic_value")
        self.bp_text = QtWidgets.QLabel(self.bp_tab_1)
        self.bp_text.setGeometry(QtCore.QRect(160, 580, 501, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.bp_text.setFont(font)
        self.bp_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bp_text.setStyleSheet("font-size:22px")
        self.bp_text.setAlignment(QtCore.Qt.AlignCenter)
        self.bp_text.setObjectName("bp_text")
        self.frame.raise_()
        self.bp_figure.raise_()
        self.bp_text.raise_()
        self.tabWidget.addTab(self.bp_tab_1, "")
        self.bp_close_botton = QtWidgets.QPushButton(bp_window)
        self.bp_close_botton.setGeometry(QtCore.QRect(350, 740, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.bp_close_botton.setFont(font)
        self.bp_close_botton.setObjectName("bp_close_botton")
        self.bp_close_botton.setStyleSheet("QPushButton{\n"
                                                     "    font-size: 14px;font-family: Arial;border: 1px solid  #292929;color: #292929; \n"
                                                     "    font-weight: bold;\n"
                                                     "}\n"
                                                     "QPushButton:hover{                    \n"
                                                     "    border: 0px solid7;\n"
                                                     "    color:white;background: #292929;\n"
                                                     "}\n"
                                                     "QPushButton:pressed{\n"
                                                     "    background:#353535;\n"
                                                     "}")

        self.retranslateUi(bp_window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(bp_window)
        self.bp_close_botton.clicked.connect((bp_window.close))


        # ! [START] link UI components with the methods
        # TODO: transfer these codes into the updated UI file



    ####################TEST
    # def __init__(self):
    #     super().__init__()
    #     self.setFocus()
    #     app.focusChanged(self.update_bp_values(GlobalVar.get_value("bp_display_mode")))


    def retranslateUi(self, bp_window):
        _translate = QtCore.QCoreApplication.translate
        sys = self.get_sys()
        dia = self.get_dia()
        bp_window.setWindowTitle(_translate("bp_window", "Blood Pressure"))
        self.diastolic_label.setText(_translate("bp_window", "Diastolic:"))
        self.systolic_label.setText(_translate("bp_window", "Systolic:"))
        self.diastolic_value.setText(_translate("bp_window", ('%.0f' % dia) + " mmHg"))
        self.systolic_value.setText(_translate("bp_window", ('%.0f' % sys) + " mmHg"))
        self.bp_text.setText(_translate("bp_window", "Your blood pressure seems to be normal.\n"
                                                     "Please keep the healthy lifestyle."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bp_tab_1), _translate("bp_window", "Today"))
        self.bp_close_botton.setText(_translate("bp_window", "Close"))

    # ! [START] define customized methods
    # TODO: transfer these codes into the updated UI file

    def get_sys(self):
        data = db_query_data.get_specified_value_pro("-1d", "-0d", "1d", "mean", "BloodPressure","systolic")
        print(data)
        data = plot_controller.data_integrate(data, "systolic")
        value = data['value'].tolist()
        return value[0]

    def get_dia(self):
        data = db_query_data.get_specified_value_pro("-1d", "-0d", "1d", "mean", "BloodPressure","diastolic")
        print(data)
        data = plot_controller.data_integrate(data, "diastolic")
        value = data['value'].tolist()
        return value[0]



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bp_window = QtWidgets.QDialog()
    ui = Ui_bp_window()
    ui.setup(bp_window)
    bp_window.show()
    sys.exit(app.exec_())

