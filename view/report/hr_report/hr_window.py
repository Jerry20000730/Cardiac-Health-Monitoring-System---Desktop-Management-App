# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hr_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from controller.database_io import db_query_data
from controller.graph_producer import plot_controller
"""
Author: GRP group 14
"""

class Ui_hr_window(object):
    def setup(self, hr_window):
        hr_window.setObjectName("hr_window")
        hr_window.resize(803, 651)
        self.hr_trends = QtWidgets.QTabWidget(hr_window)
        self.hr_trends.setGeometry(QtCore.QRect(0, 0, 801, 591))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.hr_trends.setFont(font)
        self.hr_trends.setObjectName("hr_trends")
        self.hr_tab_1 = QtWidgets.QWidget()
        self.hr_tab_1.setObjectName("hr_tab_1")
        self.hr_trend_figure = QtWidgets.QLabel(self.hr_tab_1)
        self.hr_trend_figure.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.hr_trend_figure.setText("")
        self.hr_trend_figure.setPixmap(QtGui.QPixmap("view/img/graph/hr_Hour.png"))
        self.hr_trend_figure.setScaledContents(True)
        self.hr_trend_figure.setWordWrap(False)
        self.hr_trend_figure.setObjectName("hr_trend_figure")
        self.frame = QtWidgets.QFrame(self.hr_tab_1)
        self.frame.setGeometry(QtCore.QRect(190, 500, 421, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.hr_label = QtWidgets.QLabel(self.frame)
        self.hr_label.setGeometry(QtCore.QRect(40, 0, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.hr_label.setFont(font)
        self.hr_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.hr_label.setObjectName("hr_label")
        self.hr_value = QtWidgets.QLabel(self.frame)
        self.hr_value.setGeometry(QtCore.QRect(300, 0, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.hr_value.setFont(font)
        self.hr_value.setStyleSheet("font-size:22px")
        self.hr_value.setObjectName("hr_value")
        self.frame.raise_()
        self.hr_trend_figure.raise_()
        self.hr_trends.addTab(self.hr_tab_1, "")
        self.hr_tab_2 = QtWidgets.QWidget()
        self.hr_tab_2.setObjectName("hr_tab_2")
        self.frame_2 = QtWidgets.QFrame(self.hr_tab_2)
        self.frame_2.setGeometry(QtCore.QRect(190, 500, 421, 41))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.hr_label_2 = QtWidgets.QLabel(self.frame_2)
        self.hr_label_2.setGeometry(QtCore.QRect(40, 0, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.hr_label_2.setFont(font)
        self.hr_label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.hr_label_2.setObjectName("hr_label_2")
        self.hr_value_2 = QtWidgets.QLabel(self.frame_2)
        self.hr_value_2.setGeometry(QtCore.QRect(300, 0, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.hr_value_2.setFont(font)
        self.hr_value_2.setStyleSheet("font-size:22px")
        self.hr_value_2.setObjectName("hr_value_2")
        self.hr_trend_figure_2 = QtWidgets.QLabel(self.hr_tab_2)
        self.hr_trend_figure_2.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.hr_trend_figure_2.setText("")
        self.hr_trend_figure_2.setPixmap(QtGui.QPixmap("view/img/graph/hr_Day.png"))
        self.hr_trend_figure_2.setScaledContents(True)
        self.hr_trend_figure_2.setWordWrap(False)
        self.hr_trend_figure_2.setObjectName("hr_trend_figure_2")
        self.hr_trends.addTab(self.hr_tab_2, "")
        self.hr_close_botton = QtWidgets.QPushButton(hr_window)
        self.hr_close_botton.setGeometry(QtCore.QRect(340, 600, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.hr_close_botton.setFont(font)
        self.hr_close_botton.setObjectName("hr_close_botton")
        self.hr_close_botton.setStyleSheet("QPushButton{\n"
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

        self.hr_close_botton.clicked.connect((hr_window.close))

        self.retranslateUi(hr_window)
        self.hr_trends.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(hr_window)

        # ! [START] link UI components with the methods
        # # TODO: transfer these codes into the updated UI file
        # self.hr_new_measurement_button.clicked.connect(self.add_hr_assessment)
        # self.hr_history_button.clicked.connect(self.add_reference_button)
        # ! [END] link UI components with the methods

    def retranslateUi(self, hr_window):
        _translate = QtCore.QCoreApplication.translate
        self.hour = self.get_average_hour()
        self.day = self.get_average_day()
        hr_window.setWindowTitle(_translate("hr_window", "Heart Rate"))
        self.hr_label.setText(_translate("hr_window", "Average Heart Rate:"))
        self.hr_value.setText(_translate("hr_window", str(int(self.hour)) + " BPM"))
        self.hr_trends.setTabText(self.hr_trends.indexOf(self.hr_tab_1), _translate("hr_window", "last hour"))
        self.hr_label_2.setText(_translate("hr_window", "Average Heart Rate:"))
        self.hr_value_2.setText(_translate("hr_window", str(int(self.day)) + " BPM"))
        self.hr_trends.setTabText(self.hr_trends.indexOf(self.hr_tab_2), _translate("hr_window", "last 24 hour"))
        self.hr_close_botton.setText(_translate("hr_window", "Close"))

    # ! [START] define customized methods
    # TODO: transfer these codes into the updated UI file

    def get_average_hour(self):
        hour = db_query_data.get_specified_value("0h", "8h", "1h", "mean", "HeartRate")
        hour = plot_controller.data_integrate(hour, "value")
        return hour['value'].tolist()[0]

    def get_average_day(self):
        day = db_query_data.get_specified_value("-16h", "8h", "1h", "mean", "HeartRate")
        day = plot_controller.data_integrate(day, "value")
        return day['value'].tolist()[0]


    def add_hr_assessment(self):
        """
        * Set heart rate assessment display (without reference of disease samples)
        It reloads the HR assessment picture file and map onto the components
        @param self: the instance of Ui_MainWindow class
        """

        # map the component with HR assessment pictures
        self.hr_figure_2.setPixmap(QtGui.QPixmap("model/result/heart_rate_assessment_new.png"))

    def add_reference_button(self):
        """
        * Set heart rate assessment display (with reference of disease samples)
        It reloads the HR assessment picture file and map onto the components
        @param self: the instance of Ui_MainWindow class
        """

        # map the component with HR assessment pictures
        self.hr_figure_2.setPixmap(QtGui.QPixmap("model/result/heart_rate_assessment_new_reference.png"))

    # ! [END] define customized methods


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hr_window = QtWidgets.QDialog()
    ui = Ui_hr_window()
    ui.setup(hr_window)
    hr_window.show()
    sys.exit(app.exec_())

