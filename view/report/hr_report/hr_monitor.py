# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hr_monitor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import datetime
import random
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from model.global_var import GlobalVar
from PyQt5 import QtCore, QtGui, QtWidgets
import view.report.health_report.short_assessment
"""
Author: GRP group 14
"""
matplotlib.use("Qt5Agg")  # claim we use QT5
from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas


class Ui_Monitor(object):
    
    counter_hr          = 0
    counter_ecg         = 0
    counter_ppg         = 0
    counter_second      = 0
    perc_progress       = 0
    sample_hr_data      = None
    sample_ecg_data     = None
    sample_ppg_data     = None
    sample_spo2_data    = None
    ecg_frequency       = 360
    hr_frequency        = 1
    ppg_frequency       = 100
    data_length         = 600
    window_size         = 10
    ecg_window_size     = int(ecg_frequency * window_size)
    hr_window_size      = int(hr_frequency * window_size)
    ppg_window_size     = int(ppg_frequency * window_size)
    fig_dpi             = 100
    fig_size            = (15, 3)
    refresh_time        = 1000
    refresh_time_fast   = 1
    
    def __init__(self):
        super().__init__()
        self.timer = QtCore.QTimer()
        
        if GlobalVar.get_value("dict", "monitor_display_mode") == "Simulation (Demo)":
            self.read_sim_data()
    
    def setup(self, Monitor):
        Monitor.setObjectName("Monitor")
        Monitor.resize(1000, 600)
        Monitor.setMinimumSize(QtCore.QSize(1000, 600))
        Monitor.setMaximumSize(QtCore.QSize(1000, 600))
        self.verticalLayoutWidget = QtWidgets.QWidget(Monitor)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 80, 701, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.ecg_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.ecg_layout.setContentsMargins(0, 0, 0, 0)
        self.ecg_layout.setObjectName("ecg_layout")
        # self.close_button = QtWidgets.QPushButton(Monitor)
        # self.close_button.setGeometry(QtCore.QRect(420, 560, 113, 32))
        # self.close_button.setObjectName("close_button")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Monitor)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 240, 701, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.hr_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.hr_layout.setContentsMargins(0, 0, 0, 0)
        self.hr_layout.setObjectName("hr_layout")
        self.userid_label = QtWidgets.QLabel(Monitor)
        self.userid_label.setGeometry(QtCore.QRect(30, 10, 61, 16))
        self.userid_label.setObjectName("userid_label")
        self.ecg_fig_label = QtWidgets.QLabel(Monitor)
        self.ecg_fig_label.setGeometry(QtCore.QRect(30, 60, 241, 16))
        self.ecg_fig_label.setObjectName("ecg_fig_label")
        self.hr_fig_label = QtWidgets.QLabel(Monitor)
        self.hr_fig_label.setGeometry(QtCore.QRect(30, 220, 241, 16))
        self.hr_fig_label.setObjectName("hr_fig_label")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Monitor)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 400, 701, 131))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.ppg_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.ppg_layout.setContentsMargins(0, 0, 0, 0)
        self.ppg_layout.setObjectName("ppg_layout")
        self.ppg_fig_label = QtWidgets.QLabel(Monitor)
        self.ppg_fig_label.setGeometry(QtCore.QRect(30, 380, 241, 16))
        self.ppg_fig_label.setObjectName("ppg_fig_label")
        self.hr_frame = QtWidgets.QFrame(Monitor)
        self.hr_frame.setGeometry(QtCore.QRect(760, 20, 221, 91))
        self.hr_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hr_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hr_frame.setObjectName("hr_frame")
        self.hr_unit = QtWidgets.QLabel(self.hr_frame)
        self.hr_unit.setGeometry(QtCore.QRect(110, 20, 181, 71))
        self.hr_unit.setObjectName("hr_unit")
        self.hr_value = QtWidgets.QLabel(self.hr_frame)
        self.hr_value.setGeometry(QtCore.QRect(10, 10, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.hr_value.setFont(font)
        self.hr_value.setObjectName("hr_value")
        self.hr_label = QtWidgets.QLabel(self.hr_frame)
        self.hr_label.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.hr_label.setObjectName("hr_label")
        self.spo2_frame = QtWidgets.QFrame(Monitor)
        self.spo2_frame.setGeometry(QtCore.QRect(760, 120, 221, 91))
        self.spo2_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spo2_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spo2_frame.setObjectName("spo2_frame")
        self.spo2_unit = QtWidgets.QLabel(self.spo2_frame)
        self.spo2_unit.setGeometry(QtCore.QRect(100, 30, 181, 71))
        self.spo2_unit.setObjectName("spo2_unit")
        self.spo2_value = QtWidgets.QLabel(self.spo2_frame)
        self.spo2_value.setGeometry(QtCore.QRect(10, 10, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.spo2_value.setFont(font)
        self.spo2_value.setObjectName("spo2_value")
        self.spo2_label = QtWidgets.QLabel(self.spo2_frame)
        self.spo2_label.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.spo2_label.setObjectName("spo2_label")
        self.bp_frame = QtWidgets.QFrame(Monitor)
        self.bp_frame.setGeometry(QtCore.QRect(760, 220, 221, 111))
        self.bp_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bp_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bp_frame.setObjectName("bp_frame")
        self.bp_desc = QtWidgets.QLabel(self.bp_frame)
        self.bp_desc.setGeometry(QtCore.QRect(10, 90, 181, 16))
        self.bp_desc.setObjectName("bp_desc")
        self.bp_label = QtWidgets.QLabel(self.bp_frame)
        self.bp_label.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.bp_label.setObjectName("bp_label")
        self.bp_value = QtWidgets.QLabel(self.bp_frame)
        self.bp_value.setGeometry(QtCore.QRect(10, 10, 201, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.bp_value.setFont(font)
        self.bp_value.setObjectName("bp_value")
        self.bp_unit = QtWidgets.QLabel(self.bp_frame)
        self.bp_unit.setGeometry(QtCore.QRect(170, 30, 181, 71))
        self.bp_unit.setObjectName("bp_unit")
        self.bp_button = QtWidgets.QRadioButton(self.bp_frame)
        self.bp_button.setGeometry(QtCore.QRect(200, 0, 100, 20))
        self.bp_button.setText("")
        self.bp_button.setObjectName("bp_button")
        self.temp_frame = QtWidgets.QFrame(Monitor)
        self.temp_frame.setGeometry(QtCore.QRect(760, 350, 221, 91))
        self.temp_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.temp_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.temp_frame.setObjectName("temp_frame")
        self.temp_value = QtWidgets.QLabel(self.temp_frame)
        self.temp_value.setGeometry(QtCore.QRect(10, 10, 201, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.temp_value.setFont(font)
        self.temp_value.setObjectName("temp_value")
        self.temp_label = QtWidgets.QLabel(self.temp_frame)
        self.temp_label.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.temp_label.setObjectName("temp_label")
        self.temp_unit = QtWidgets.QLabel(self.temp_frame)
        self.temp_unit.setGeometry(QtCore.QRect(130, 50, 31, 31))
        self.temp_unit.setObjectName("temp_unit")
        self.rr_frame = QtWidgets.QFrame(Monitor)
        self.rr_frame.setGeometry(QtCore.QRect(760, 450, 221, 91))
        self.rr_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rr_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rr_frame.setObjectName("rr_frame")
        self.label_17 = QtWidgets.QLabel(self.rr_frame)
        self.label_17.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.label_17.setObjectName("label_17")
        self.label_15 = QtWidgets.QLabel(self.rr_frame)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 201, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.userid_value = QtWidgets.QLabel(Monitor)
        self.userid_value.setGeometry(QtCore.QRect(90, 10, 61, 16))
        self.userid_value.setObjectName("userid_value")
        self.mode_combobox = QtWidgets.QComboBox(Monitor)
        self.mode_combobox.setGeometry(QtCore.QRect(820, 570, 171, 26))
        self.mode_combobox.setObjectName("mode_combobox")
        self.mode_combobox.addItem("")
        self.mode_combobox.addItem("")
        self.mode_combobox.addItem("")
        self.mode_label = QtWidgets.QLabel(Monitor)
        self.mode_label.setGeometry(QtCore.QRect(720, 570, 91, 20))
        self.mode_label.setObjectName("mode_label")
        self.progressBar = QtWidgets.QProgressBar(Monitor)
        self.progressBar.setGeometry(QtCore.QRect(140, 570, 118, 23))
        self.progressBar.setProperty("value", self.perc_progress)
        self.progressBar.setObjectName("progressBar")
        self.start_receive_button = QtWidgets.QRadioButton(Monitor)
        self.start_receive_button.setGeometry(QtCore.QRect(10, 570, 121, 20))
        self.start_receive_button.setObjectName("start_receive_button")
        
        self.time_label = QtWidgets.QLabel(Monitor)
        self.time_label.setGeometry(QtCore.QRect(265, 570, 200, 23))
        self.time_label.setObjectName("time_label")
        self.time_label.setText(str(datetime.timedelta(seconds = self.data_length)) + " (remaining)")
        
        self.canvas_ecg = FigureCanvas(plt.Figure(figsize = self.fig_size, dpi = self.fig_dpi))
        self.canvas_hr = FigureCanvas(plt.Figure(figsize = self.fig_size, dpi = self.fig_dpi))
        self.canvas_ppg = FigureCanvas(plt.Figure(figsize = self.fig_size, dpi = self.fig_dpi))
        
        self.ecg_layout.addWidget(self.canvas_ecg)
        self.hr_layout.addWidget(self.canvas_hr)
        self.ppg_layout.addWidget(self.canvas_ppg)
        
        self.mode_combobox.currentIndexChanged.connect(self.update_display_mode)
        # self.start_receive_button.clicked.connect(self.start_client)
        
        self.insert_ax()
    
        self.start_timer()
        self.timer.timeout.connect(lambda: self.update_chart(Monitor))

        self.retranslateUi(Monitor)
        QtCore.QMetaObject.connectSlotsByName(Monitor)
        
    def read_sim_data(self):
        
        self.sample_hr_data = pd.read_csv("/Users/georgewinston/Documents/Codes/SHH Edge/shh-edge-computer/model/data/sample_arrhythmia_106_HR.csv").iloc[0 : self.data_length + 10, :]
        
        self.sample_ecg_data = pd.read_csv("/Users/georgewinston/Documents/Codes/SHH Edge/shh-edge-computer/model/data/sample_arrhythmia_106_ECG.csv").iloc[0 : (self.data_length + 10) * self.ecg_frequency, :]
        
        self.sample_ppg_data = pd.read_csv("/Users/georgewinston/Documents/Codes/SHH Edge/shh-edge-computer/model/data/sample_arrhythmia_106_HR.csv").iloc[0 : self.data_length + 10, :]["HR/sec (round, de-nan)"]
        for i in range(0, len(self.sample_ppg_data)):
            self.sample_ppg_data[i] += random.randint(0, 10)
        
        self.sample_spo2_data = pd.read_csv("/Users/georgewinston/Documents/Codes/SHH Edge/shh-edge-computer/model/data/sample_healthy_SpO2.csv").iloc[0 : self.data_length + 10, :]
        
    def insert_ax(self):
        
        if GlobalVar.get_value("dict", "monitor_display_mode") == "Simulation (Demo)":
        
            self.ax_hr = self.canvas_hr.figure.subplots()
            self.ax_hr.set_xticks([])
            self.ax_hr.set_ylim([min(self.sample_hr_data["HR/sec (round, de-nan)"]),
                                max(self.sample_hr_data["HR/sec (round, de-nan)"])])
            # self.ax_hr.set_xlabel("Time (seconds")
            self.ax_hr.set_ylabel("Heart Rate\n(bpm)", fontsize = 10)
            
            self.ax_ecg = self.canvas_ecg.figure.subplots()
            self.ax_ecg.set_xticks([])
            self.ax_ecg.set_ylim([min(self.sample_ecg_data.iloc[:, 0]),
                                max(self.sample_ecg_data.iloc[:, 0])])
            # self.ax_ecg.set_xlabel("Timestamp")
            self.ax_ecg.set_ylabel("ECG Signals",fontsize = 10)
            
            self.ax_ppg = self.canvas_ppg.figure.subplots()
            self.ax_ppg.set_xticks([])
            self.ax_ppg.set_ylim([min(self.sample_hr_data["HR/sec (round, de-nan)"]),
                                max(self.sample_hr_data["HR/sec (round, de-nan)"])])
            # self.ax_ppg.set_ylim()
            # self.ax_ppg.set_xlabel("Timestamp")
            # self.ax_ppg.set_ylabel("PPG Signals")
            self.ax_ppg.set_ylabel("Heart Rate\n(bpm)", fontsize = 10)
            
            self.fig_hr = None
            self.fig_ecg = None
            self.fig_ppg = None
        
    def update_chart(self, Object):
        
        if GlobalVar.get_value("dict", "monitor_display_mode") == "Simulation (Demo)":
        
            self.hr_value.setText(str(round(self.sample_hr_data["HR/sec (round, de-nan)"][self.counter_hr])))
            self.spo2_value.setText(str(self.sample_spo2_data["SpO2"][self.counter_hr]))
            
            if GlobalVar.get_value("dict", "monitor_display_mode") == "Simulation (Demo)":
            
                # heart rate data (10 seconds)
                x_hr = self.sample_hr_data["recording time"][self.counter_hr : self.counter_hr + self.hr_window_size]
                y_hr = self.sample_hr_data["HR/sec (round, de-nan)"][self.counter_hr : self.counter_hr + self.hr_window_size]
                
                # ECG data (10 seconds)
                y_ecg = self.sample_ecg_data.iloc[self.counter_ecg : self.counter_ecg + self.ecg_window_size, 0]
                
                # PPG data (10 seconds)
                y_ppg = self.sample_ppg_data[self.counter_ppg : self.counter_ppg + self.hr_window_size]
            
            self.counter_hr += self.hr_frequency
            self.counter_ecg += self.ecg_frequency
            self.counter_ppg += self.hr_frequency       # TODO: to be changed
                
            self.counter_second += 1
            self.counter_progress = self.counter_second / self.data_length
            self.progressBar.setValue(self.counter_progress * 100)
            
            self.time_label.setText(str(datetime.timedelta(seconds = self.data_length - self.counter_second)) + " (remaining)")
            
            if self.fig_hr != None or self.fig_ecg != None:
                try:
                    self.ax_hr.remove()
                    self.ax_ecg.remove()
                    self.ax_ppg.remove()
                    self.insert_ax()
                except Exception as exec:
                    print("[ERROR] Matplotlib: {}".format(exec))
                    
            self.fig_hr = self.ax_hr.plot(x_hr, y_hr, color = "firebrick")
            self.fig_ecg = self.ax_ecg.plot(y_ecg, color = "firebrick")
            self.fig_ppg = self.ax_ppg.plot(y_ppg, color = "royalblue")
            
            self.canvas_hr.draw()
            self.canvas_ecg.draw()
            self.canvas_ppg.draw()
            
            if self.counter_second == 10:
                self.timer.stop()
                self.timer.start(self.refresh_time_fast)
                
            # if self.counter_second >= self.data_length:
            if self.counter_second >= 10:
                self.timer.stop()
                self.open_short_assessment()
                self.close_current_window(Object)
        
    def start_timer(self):
        self.timer.start(self.refresh_time)
        print("[INFO] Monitor: Timing starts...")
        
    def update_display_mode(self):
        
        current_mode = self.mode_combobox.currentText()
        try:
            GlobalVar.set_value("dict", "monitor_display_mode", current_mode)
            print("[Info] The display mode has been changed to {info}.".format(info = current_mode))
        except Exception as exce:
            print("[Error] Cannot set the display mode: {info}".format(info = exce))
            
    def init_bp_display():
        pass
    
    def close_current_window(self, current_window):
            current_window.close()
    
    def open_short_assessment(self):

        self.window = QtWidgets.QDialog()
        self.short_assessment = view.report.health_report.short_assessment.Ui_Dialog()
        self.short_assessment.setup(self.window)
        self.window.show()
        
    # def start_client(self):
        
    #     # create a QThread object
    #     self.thread = QThread()
        
    #     # create a worker object
    #     self.worker = Client()
        
    #     # move worker to the thread
    #     self.worker.moveToThread(self.thread)
        
    #     # connect signals and slots
    #     self.thread.started.connect(self.worker.run)
    #     self.worker.finished.connect(self.thread.quit)
    #     self.worker.finished.connect(self.worker.deleteLater)
    #     self.thread.finished.connect(self.thread.deleteLater)
        
    #     self.worker.progress.connect(self.print_progress)
        
    #     # start the thread
    #     self.thread.start()

    #     # final resets
    #     self.start_receive_button.setEnabled(False)
    #     self.thread.finished.connect(
    #         lambda: self.start_receive_button.setEnabled(True)
    #     )
        
    #     # self.thread.finished.connect(
    #     #     lambda: self.bp_label.setText("Long-Running Step: 0")
    #     # )
        
    def print_progress(self, n):
        print("Progress: {num}".format(num = n))
        print(self.thread.finished)
        print(self.worker.finished)
        print(self.worker.progress)

    def retranslateUi(self, Monitor):
        _translate = QtCore.QCoreApplication.translate
        Monitor.setWindowTitle(_translate("Monitor", "Monitor Window"))
        # self.close_button.setText(_translate("Monitor", "Close"))
        self.userid_label.setText(_translate("Monitor", "User ID:"))
        self.ecg_fig_label.setText(_translate("Monitor", "ECG ({} seconds)".format(str(self.window_size))))
        self.hr_fig_label.setText(_translate("Monitor", "Heart Rate ({} seconds)".format(str(self.window_size))))
        self.ppg_fig_label.setText(_translate("Monitor", "PPG ({} seconds)".format(str(self.window_size))))
        self.hr_unit.setText(_translate("Monitor", "beats\n""per\n""minute"))
        self.hr_value.setText(_translate("Monitor", "--"))
        self.hr_label.setText(_translate("Monitor", "Heart Rate"))
        self.spo2_unit.setText(_translate("Monitor", "%"))
        self.spo2_value.setText(_translate("Monitor", "--"))
        self.spo2_label.setText(_translate("Monitor", "Oxygen Saturation"))
        self.bp_desc.setText(_translate("Monitor", "(Diastolic/Systolic)"))
        self.bp_label.setText(_translate("Monitor", "Blood Pressure"))
        self.bp_value.setText(_translate("Monitor", "--/---"))
        self.bp_unit.setText(_translate("Monitor", "mmHg"))
        self.temp_value.setText(_translate("Monitor", "--.-"))
        self.temp_label.setText(_translate("Monitor", "Body Temperature"))
        self.temp_unit.setText(_translate("Monitor", "°C"))
        self.label_17.setText(_translate("Monitor", "Respiratory Rate"))
        self.label_15.setText(_translate("Monitor", "--"))
        self.userid_value.setText(_translate("Monitor", "001"))
        self.mode_combobox.setItemText(0, _translate("Monitor", "Simulation (Demo)"))
        self.mode_combobox.setItemText(1, _translate("Monitor", "Short-term Assessment"))
        self.mode_combobox.setItemText(2, _translate("Monitor", "Long-term Monitoring"))
        self.mode_label.setText(_translate("Monitor", "Display Mode:"))
        self.start_receive_button.setText(_translate("Monitor", "Start Receivng"))
        
# class Client(QObject):
#     finished = pyqtSignal()
#     progress = pyqtSignal(int)

#     def run(self):
#         # """Long-running task."""
#         # for i in range(5):
#         #     time.sleep(1)
#         #     print("Sleeping...")
#         #     self.progress.emit(i + 1)
#         # print("Waked up!")
#         # self.finished.emit()
        
#         client_host = GlobalVar.get_value("client", "client_host")
#         client_port = int(GlobalVar.get_value("client", "client_port"))
#         comm_interval = GlobalVar.get_value("client", "request_interval")
    
#         try:
#             self.progress.emit(1)
#             client = SocketClient(client_host, client_port)
#             client.client_startRecording(comm_interval)
#             client.client_requestForData(comm_interval)
#         except Exception as exce:
#             print("[Error] Client: {info}".format(info = exce))
            
#         self.finished.emti()
