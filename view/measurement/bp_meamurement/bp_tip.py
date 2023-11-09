import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from model.global_var import GlobalVar
import view.measurement.bp_meamurement.bp_measure
"""
Author: GRP group 14
"""
class Ui_bp_tips(object):
    
    page_index = 0
    time_5min = 300
    time_1min = 60
    counter_second = 0
    
    def __init__(self):
        super().__init__()
        self.timer = QtCore.QTimer()


    def setup(self, Tips):
        Tips.setObjectName("Tips")
        Tips.resize(550, 600)
        self.buttonBox = QtWidgets.QDialogButtonBox(Tips)
        self.buttonBox.setGeometry(QtCore.QRect(200, 500, 300, 80))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tip_text = QtWidgets.QLabel(Tips)
        self.tip_text.setGeometry(QtCore.QRect(50, 400, 450, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setFamily("Arial")
        font.setWeight(50)
        self.tip_text.setFont(font)
        self.tip_text.setObjectName("tip_text")
        self.tip_text.setWordWrap(True)
        self.tip_time = QtWidgets.QLabel(Tips)
        self.tip_time.setGeometry(QtCore.QRect(50, 450, 450, 71))
        self.tip_time.setObjectName("tip_time")
        self.tip_time.setWordWrap(True)
        self.tip_time.setText("Remaining Time: " + str(datetime.timedelta(seconds = self.time_5min)))
        self.tip_time.setStyleSheet("QLabel{ color: #2d4bdf; font-family: Arial;font-weight:bold; font-size: 18px;"
                                    "}")
        self.tip_figure = QtWidgets.QLabel(Tips)
        self.tip_figure.setGeometry(QtCore.QRect(120, 50, 411, 361))
        # self.tip_text.setText(self.tips_list[0])
        # self.tip_figure.setPixmap(QtGui.QPixmap(self.picture_list[0]))
        self.init_figure()
        self.tip_figure.setObjectName("tip_figure")
        self.tip_figure.resize(300,300)
        self.tip_figure.setScaledContents(True)
        
        self.start_timer()
        self.timer.timeout.connect(self.update_time)
        
        self.retranslateUi(Tips)
        self.buttonBox.accepted.connect(lambda: self.close_current_window(Tips))
        self.buttonBox.accepted.connect(self.plus_1)
        self.buttonBox.rejected.connect(Tips.reject)
        self.buttonBox.setStyleSheet("QPushButton{\n"
                                                "    font-family: Arial;border: 1px solid  #292929;color: #292929; \n"
                                                "    font-weight: bold; padding: 5px 5px;\n"
                                                "}\n"
                                                "QPushButton:hover{                    \n"
                                                "    border: 0px solid7;\n"
                                                "    color:white;background: #292929;\n"
                                                "}\n"
                                                "QPushButton:pressed{\n"
                                                "    background:#353535;\n"
                                                "}")
        QtCore.QMetaObject.connectSlotsByName(Tips)
        
    def start_timer(self):
        self.timer.start(1000)
        print("[INFO] BP Tips: Timing starts...")
        
    def update_time(self):
            
        self.counter_second += 1
        self.tip_time.setText("Remaining Time: " + str(datetime.timedelta(seconds = self.time_5min - self.counter_second)))
        
        if self.counter_second == self.time_5min:
            self.timer.stop()
            self.tip_time.setText("The timing has ended. Now you can start the measurement.")
        

    def open_bp_measure_window(self):
        self.window = QtWidgets.QDialog()
        self.sub_bp_measure = view.measurement.bp_meamurement.bp_measure.Ui_bp_measure()
        self.sub_bp_measure.setup(self.window)
        self.window.show()

    def close_current_window(self, current_window):
        if self.page_index == 8:
            current_window.close()

    def plus_1(self):
        if self.page_index != 8:
            
            try:
                self.tip_text.setText(GlobalVar.get_value("text", "bp_tips_5min")[self.page_index])
                self.tip_figure.setPixmap(QtGui.QPixmap(GlobalVar.get_pic_path("bp_tips_1min")[self.page_index]))
            except Exception as err:
                print("[Error] {info}".format(info = err))
            self.page_index += 1
        else:
            self.open_bp_measure_window()
            
    def init_figure(self):
        if GlobalVar.get_repeat_time() == 1:
            try:
                self.tip_text.setText(GlobalVar.get_value("text", "bp_tips_5min")[self.page_index])
                self.tip_figure.setPixmap(QtGui.QPixmap(GlobalVar.get_pic_path("bp_tips_5min")[self.page_index]))
            except Exception as err:
                print("[Error] {info}".format(info = err))
        else:
            try:
                self.tip_text.setText(GlobalVar.get_value("text", "bp_tips_1min")[self.page_index])
                self.tip_figure.setPixmap(QtGui.QPixmap(GlobalVar.get_pic_path("bp_tips_1min")[self.page_index]))
            except Exception as err:
                print("[Error] {info}".format(info = err))
        self.page_index += 1

    def retranslateUi(self, Tips):
        _translate = QtCore.QCoreApplication.translate
        Tips.setWindowTitle(_translate("Tips", "Tips for Blood Pressure Measurement"))
        # self.tip_text.setText(_translate("Tips", "TextLabel"))
        