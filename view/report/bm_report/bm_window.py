# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bm_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
"""
Author: GRP group 14
"""
import controller.graph_producer.plot_controller
from controller.database_io import db_query_data
from controller.graph_producer import plot_controller
from model.global_var import GlobalVar

class Ui_bm_window(object):
    def setup(self, bm_window):
        bm_window.setObjectName("bm_window")
        bm_window.resize(802, 765)
        self.tabWidget = QtWidgets.QTabWidget(bm_window)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 691))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.bm_tab_1 = QtWidgets.QWidget()
        self.bm_tab_1.setObjectName("bm_tab_1")
        self.bm_trend_figure = QtWidgets.QLabel(self.bm_tab_1)
        self.bm_trend_figure.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.bm_trend_figure.setText("")
        self.bm_trend_figure.setPixmap(QtGui.QPixmap("view/img/graph/bm_trend_Week.png"))
        self.bm_trend_figure.setScaledContents(True)
        self.bm_trend_figure.setWordWrap(False)
        self.bm_trend_figure.setObjectName("bm_trend_figure")
        self.frame = QtWidgets.QFrame(self.bm_tab_1)
        self.frame.setGeometry(QtCore.QRect(210, 600, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(6)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bmi_label = QtWidgets.QLabel(self.frame)
        self.bmi_label.setGeometry(QtCore.QRect(210, 0, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.bmi_label.setFont(font)
        self.bmi_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.bmi_label.setObjectName("bmi_label")
        self.weight_value = QtWidgets.QLabel(self.frame)
        self.weight_value.setGeometry(QtCore.QRect(110, 0, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.weight_value.setFont(font)
        self.weight_value.setObjectName("weight_value")
        self.bmi_value = QtWidgets.QLabel(self.frame)
        self.bmi_value.setGeometry(QtCore.QRect(300, 0, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.bmi_value.setFont(font)
        self.bmi_value.setObjectName("bmi_value")
        self.weight_label = QtWidgets.QLabel(self.frame)
        self.weight_label.setGeometry(QtCore.QRect(-10, 0, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.weight_label.setFont(font)
        self.weight_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.weight_label.setObjectName("weight_label")
        self.bmi_figure = QtWidgets.QLabel(self.bm_tab_1)
        self.bmi_figure.setGeometry(QtCore.QRect(0, 490, 800, 100))
        self.bmi_figure.setText("")
        self.bmi_figure.setPixmap(QtGui.QPixmap("view/img/graph/BMI_day.png"))
        self.bmi_figure.setObjectName("bmi_figure")
        self.bmi_figure.setScaledContents(True)
        self.frame.raise_()
        self.bm_trend_figure.raise_()
        self.bmi_figure.raise_()
        self.tabWidget.addTab(self.bm_tab_1, "")
        self.bm_close_botton = QtWidgets.QPushButton(bm_window)
        self.bm_close_botton.setGeometry(QtCore.QRect(340, 710, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bm_close_botton.setFont(font)
        self.bm_close_botton.setObjectName("bm_close_botton")
        self.bm_close_botton.setStyleSheet("QPushButton{\n"
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

        self.retranslateUi(bm_window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(bm_window)
        self.bm_close_botton.clicked.connect((bm_window.close))

        # self.bm_new_measurement_button.clicked.connect(self.)
        # self.update_text()

    def retranslateUi(self, bm_window):
        weight = self.get_weight()
        bmi = self.get_BMI()
        _translate = QtCore.QCoreApplication.translate
        bm_window.setWindowTitle(_translate("bm_window", "Weight"))
        self.bmi_label.setText(_translate("bm_window", "BMI:"))
        self.weight_value.setText(_translate("bm_window", '%.2f' % weight))
        self.bmi_value.setText(_translate("bm_window", '%.2f' % bmi))
        self.weight_label.setText(_translate("bm_window", "Weight:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bm_tab_1), _translate("bm_window", "Today"))
        self.bm_close_botton.setText(_translate("bm_window", "Close"))

    def get_weight(self):
        data = db_query_data.get_specified_value("-1d", "-0d", "1d", "mean", "Weight")
        print(data)
        data = plot_controller.data_integrate(data, "value")
        weight = data['value'].tolist()
        print(weight)
        return weight[0]

    def get_BMI(self):
        data = db_query_data.get_specified_value("-1d", "-0d", "1d", "mean", "Weight")
        data = plot_controller.data_integrate(data, "value")
        bmi = plot_controller.bmi_calculator(data)
        print(bmi)
        bmi_value = bmi['value'].tolist()
        return bmi_value[0]

    def update_bm_figure(self):
        """
        * Update the display of BP measurement
        @param self: the instance of Ui_MainWindow class
        """
        
        # re-generate and save the BP measurement picture file
        # DataIO.refresh_BM_plot_file()
        
        # map the component with BP measurement figure
        # self.bm_trend_figure.setPixmap(QtGui.QPixmap(GlobalVar.get_path("bm_trend_new")))

        
    # def update_text(self):
    #
    #     # get the newest (last) BM value
    #     new_bm_value = DataIO.get_new_BM_value(False, "Manually Input", "-1d", "-0d")
    #
    #     # get the BMI result
    #     # TODO: height value should auto in the further development
    #     bmi = round(Utility.calculate_bmi(weight = float(new_bm_value["Weight"].values),
    #                                       height = 1.65),
    #                 1)
    #
    #     self.weight_value.setText(str(float(new_bm_value["Weight"].values)) + " KG")
    #     self.bmi_value.setText(str(bmi))
    #
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bm_window = QtWidgets.QDialog()
    ui = Ui_bm_window()
    ui.setup(bm_window)
    bm_window.show()
    sys.exit(app.exec_())

