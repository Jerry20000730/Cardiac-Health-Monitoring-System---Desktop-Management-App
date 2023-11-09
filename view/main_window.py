# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QThread
import paramiko
from model.data.Counter import Counter
from controller.database_io.data_process_storage import *
from controller.edge_connection.socket_client import ClientThread
from controller.event_client import EventThread
from view.report.bm_report.bm_alert import Ui_bm_alert
from view.report.bm_report.bm_window import Ui_bm_window
from view.report.bp_report.bp_alert import Ui_bp_alert
from view.report.bp_report.bp_window import Ui_bp_window
from view.report.health_report.health_report_alert import Ui_report_alert
from view.report.hr_report.hr_alert import Ui_hr_alert
from view.report.hr_report.hr_window import Ui_hr_window
from view.measurement.bm_measurement.bm_decide import Ui_weight_decide
from view.measurement.bp_meamurement.bp_measure import Ui_bp_measure
from view.report.health_report.health_report_window import Ui_report_window
import view.measurement.bp_meamurement.bp_tip
from controller.data_io import *
from controller.plotter import *
from model.socket.socketUtil import *
from controller.graph_producer import plot_controller as graph
from apscheduler.schedulers.qt import QtScheduler
from view.scheduler import scheduler

"""
Author: GRP group 14
"""
class Ui_MainWindow(QtWidgets.QMainWindow):

    # create a QThread object
    binding_thread = QThread()
    client_thread = QThread()
    status_thread = QThread()
    event_thread = QThread()

    # create a client_worker object
    binding_worker = BindingThread()
    client_worker = ClientThread()
    status_worker = CheckingStatusThread()
    event_worker = EventThread()
    scheduler = QtScheduler()

    # thread_lock = QMutex()

    def __init__(self, parent=None):
        super(QtWidgets.QMainWindow, self).__init__(parent)
        uic.loadUi('view/main_window.ui', self)
        # self.start_client()
        self.start_event()

        self.update_connection_setup()
        self.init_device_table()

        self.bp_button.clicked.connect(self.open_bp_window)
        self.hr_button.clicked.connect(self.open_hr_window)
        self.bm_button.clicked.connect(self.open_bm_window)
        self.weight_button.clicked.connect(self.open_weight_decide)
        # self.sure_button.clicked.connect(self.open_hr_monior)
        self.hr_button.setStyleSheet("QPushButton{\n"
                                     "    font-family: Arial;border: 1px solid  #292929;color: #292929; \n"
                                     "    font-weight: bold; font-size: 16px\n"
                                     "}\n"
                                     "QPushButton:hover{                    \n"
                                     "    border: 0px solid7;\n"
                                     "    color:white;background: #292929;\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "    background:#353535;\n"
                                     "}")
        self.bm_button.setStyleSheet("QPushButton{\n"
                                     "    font-family: Arial;border: 1px solid  #292929;color: #292929;\n"
                                     "    font-weight: bold; font-size: 16px\n"
                                     "}\n"
                                     "QPushButton:hover{                    \n"
                                     "    border: 0px solid7;\n"
                                     "    color:white;background: #292929;\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "    background:#353535;\n"
                                     "}")
        self.bp_button.setStyleSheet("QPushButton{\n"
                                     "    font-family: Arial;border: 1px solid  #292929;color: #292929;\n"
                                     "    font-weight: bold; font-size: 16px\n"
                                     "}\n"
                                     "QPushButton:hover{                    \n"
                                     "    border: 0px solid7;\n"
                                     "    color:white;background: #292929;\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "    background:#353535;\n"
                                     "}")
        self.bp_measure_button.clicked.connect(self.open_bp_tips)
        self.manually_connection_rbutton.toggled.connect(self.auto_connection_mode)
        self.connect_button.clicked.connect(self.start_client)
        self.connect_button_2.clicked.connect(self.bind_hub)
        self.connection_setup_button.clicked.connect(self.open_connection_setup)
        self.connect_button.setStyleSheet("QPushButton{\n"
                                          "    font-family: Arial;border: 1px solid  #292929;color: #292929; \n"
                                          "    font-weight: bold;font-size: 16px;\n"
                                          "}\n"
                                          "QPushButton:hover{                    \n"
                                          "    border: 0px solid7;\n"
                                          "    color:white;background: #292929;\n"
                                          "}\n"
                                          "QPushButton:pressed{\n"
                                          "    background:#353535;\n"
                                          "}")
        self.connect_button_2.setStyleSheet("QPushButton{\n"
                                            "    font-family: Arial;border: 1px solid  #292929;color: #292929; \n"
                                            "    font-weight: bold;font-size: 16px;\n"
                                            "}\n"
                                            "QPushButton:hover{                    \n"
                                            "    border: 0px solid7;\n"
                                            "    color:white;background: #292929;\n"
                                            "}\n"
                                            "QPushButton:pressed{\n"
                                            "    background:#353535;\n"
                                            "}")
        self.connection_setup_button.setStyleSheet("QPushButton{\n"
                                                   "    font-family: Arial;border: 1px solid  #292929;color: #292929; \n"
                                                   "    font-weight: bold;font-size: 16px;\n"
                                                   "}\n"
                                                   "QPushButton:hover{                    \n"
                                                   "    border: 0px solid7;\n"
                                                   "    color:white;background: #292929;\n"
                                                   "}\n"
                                                   "QPushButton:pressed{\n"
                                                   "    background:#353535;\n"
                                                   "}")
        self.apply_button.setStyleSheet("QPushButton{\n"
                                        "    font-family: Arial;border: 1px solid  #292929;color: #292929; \n"
                                        "    font-weight: bold;font-size: 16px;\n"
                                        "}\n"
                                        "QPushButton:hover{                    \n"
                                        "    border: 0px solid7;\n"
                                        "    color:white;background: #292929;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background:#353535;\n"
                                        "}")
        self.apply_button.clicked.connect(self.update_connection_setup)
        self.health_record_button.clicked.connect(self.open_health_report)
        self.update_button.clicked.connect(self.update_info)
        self.update_button.setStyleSheet("QPushButton{\n"
                                         "    font-family: Arial;border: 1px solid #2d4bdf; color:#2d4bdf;\n"
                                         "    font-weight: bold;font-size: 16px\n"
                                         "}\n"
                                         "QPushButton:hover{                    \n"
                                         "    border: 0px solid7;\n"
                                         "    color:white;background: #2d4bdf;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    background:#c4e0f3;\n"
                                         "}")
        self.health_record_button.setStyleSheet("QPushButton{\n"
                                                "    font-family: Arial;border: 1px solid  #292929;color: #292929; \n"
                                                "    font-weight: bold;font-size: 16px\n"
                                                "}\n"
                                                "QPushButton:hover{                    \n"
                                                "    border: 0px solid7;\n"
                                                "    color:white;background: #292929;\n"
                                                "}\n"
                                                "QPushButton:pressed{\n"
                                                "    background:#353535;\n"
                                                "}")
        self.weight_button.setStyleSheet("QPushButton{\n"
                                         "    font-family: Arial;border: 1px solid  #292929;color: #292929; "
                                         "    font-size: 20px;\n"
                                         "    font-weight: bold;\n"
                                         "}\n"
                                         "QPushButton:hover{                    \n"
                                         "    border: 0px solid7;\n"
                                         "    color:white;background: #292929;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    background:#353535;\n"
                                         "}")
        self.bp_measure_button.setStyleSheet("QPushButton{\n"
                                             "    font-family: Arial;border: 1px solid  #292929;color: #292929; \n"
                                             "    font-weight: bold;font-size: 20px;\n"
                                             "}\n"
                                             "QPushButton:hover{                    \n"
                                             "    border: 0px solid7;\n"
                                             "    color:white;background: #292929;\n"
                                             "}\n"
                                             "QPushButton:pressed{\n"
                                             "    background:#353535;\n"
                                             "}")
        self.manage_family_button.setStyleSheet("QPushButton{\n"
                                             "    font-family: Arial;border: 1px solid  #292929;color: #292929; \n"
                                             "    font-weight: bold;font-size: 16px;\n"
                                             "}\n"
                                             "QPushButton:hover{                    \n"
                                             "    border: 0px solid7;\n"
                                             "    color:white;background: #292929;\n"
                                             "}\n"
                                             "QPushButton:pressed{\n"
                                             "    background:#353535;\n"
                                             "}")
        self.manually_connection_rbutton.setStyleSheet(
            "    font-family: Arial;color: #292929; \n"
            "    font-weight: bold;font-size: 16px;\n"
            )
        self.update_data_progress_bar.setVisible(False)
        self.update_data_progress_bar.setStyleSheet(
            "QProgressBar{(border: 1px solid  #FFFFFF;height:30; background: red;color:rgb(255,255,0);")
        self.tabs.setStyleSheet("QPushButton{ background = #c4e0f3;"
                                "}")
        self.msg_label.setStyleSheet("    font-family: Arial;color: #292929; \n")
        # self.scheduler.add_job(self.open_scheduler, 'interval', seconds=5)
        # self.scheduler.start()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 575)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(19, 9, 491, 481))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tabs.setFont(font)
        self.tabs.setWhatsThis("")
        self.tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabs.setUsesScrollButtons(False)
        self.tabs.setDocumentMode(False)
        self.tabs.setTabsClosable(False)
        self.tabs.setMovable(True)
        self.tabs.setTabBarAutoHide(False)
        self.tabs.setObjectName("tabs")
        self.report_tab = QtWidgets.QWidget()
        self.report_tab.setEnabled(True)
        self.report_tab.setToolTip("")
        self.report_tab.setObjectName("report_tab")
        self.health_record_button = QtWidgets.QPushButton(self.report_tab)
        self.health_record_button.setGeometry(QtCore.QRect(350, 50, 121, 81))
        self.health_record_button.setObjectName("health_record_button")
        self.health_report_label = QtWidgets.QLabel(self.report_tab)
        self.health_report_label.setGeometry(QtCore.QRect(20, 50, 320, 80))
        self.health_report_label.setAutoFillBackground(False)
        self.health_report_label.setText("")
        self.health_report_label.setPixmap(QtGui.QPixmap("view/img/health_report_tag.png"))
        self.health_report_label.setScaledContents(True)
        self.health_report_label.setObjectName("health_report_label")

        self.hr_label = QtWidgets.QLabel(self.report_tab)
        self.hr_label.setGeometry(QtCore.QRect(20, 180, 320, 80))
        self.hr_label.setAutoFillBackground(False)
        self.hr_label.setText("")
        self.hr_label.setPixmap(QtGui.QPixmap("view/img/hr_trend_tag.png"))
        self.hr_label.setScaledContents(True)
        self.hr_label.setObjectName("hr_label")
        self.bp_label = QtWidgets.QLabel(self.report_tab)
        self.bp_label.setGeometry(QtCore.QRect(20, 270, 320, 80))
        self.bp_label.setAutoFillBackground(False)
        self.bp_label.setText("")
        self.bp_label.setPixmap(QtGui.QPixmap("view/img/bp_tag.png"))
        self.bp_label.setScaledContents(True)
        self.bp_label.setObjectName("bp_label")
        self.bm_label = QtWidgets.QLabel(self.report_tab)
        self.bm_label.setGeometry(QtCore.QRect(20, 360, 320, 80))
        self.bm_label.setAutoFillBackground(False)
        self.bm_label.setText("")
        self.bm_label.setPixmap(QtGui.QPixmap("view/img/bm_tag.png"))
        self.bm_label.setScaledContents(True)
        self.bm_label.setObjectName("bm_label")
        self.hr_button = QtWidgets.QPushButton(self.report_tab)
        self.hr_button.setGeometry(QtCore.QRect(350, 180, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.hr_button.setFont(font)
        self.hr_button.setObjectName("hr_button")
        self.bp_button = QtWidgets.QPushButton(self.report_tab)
        self.bp_button.setGeometry(QtCore.QRect(350, 270, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.update_button.setGeometry(QtCore.QRect(120, 10, 131, 28))
        self.update_button.setStyleSheet("font-size:16px")
        self.update_button.setObjectName("update_button")

        self.bp_button.setFont(font)
        self.bp_button.setObjectName("bp_button")
        self.bm_button = QtWidgets.QPushButton(self.report_tab)
        self.bm_button.setGeometry(QtCore.QRect(350, 360, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bm_button.setFont(font)
        self.bm_button.setObjectName("bm_button")
        self.catergories_label = QtWidgets.QLabel(self.report_tab)
        self.catergories_label.setGeometry(QtCore.QRect(20, 150, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.catergories_label.setFont(font)
        self.catergories_label.setObjectName("catergories_label")
        self.summary_label = QtWidgets.QLabel(self.report_tab)
        self.summary_label.setGeometry(QtCore.QRect(20, 20, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.summary_label.setFont(font)
        self.summary_label.setObjectName("summary_label")
        self.tabs.addTab(self.report_tab, "")
        self.measurement_tab = QtWidgets.QWidget()
        self.measurement_tab.setObjectName("measurement_tab")
        self.tabs.addTab(self.measurement_tab, "")
        self.weight_button = QtWidgets.QPushButton(self.measurement_tab)
        self.weight_button.setGeometry(QtCore.QRect(0, 0, 511, 141))
        self.weight_button.setObjectName("weight_button")
        self.bp_measure_button = QtWidgets.QPushButton(self.measurement_tab)
        self.bp_measure_button.setGeometry(QtCore.QRect(0, 135, 491, 161))
        self.bp_measure_button.setObjectName("bp_measure_button")
        # self.sure_button = QtWidgets.QPushButton(self.measurement_tab)
        # self.sure_button.setGeometry(QtCore.QRect(0, 290, 491, 161))
        # self.sure_button.setObjectName("sure_button")
        self.device_tab = QtWidgets.QWidget()
        self.device_tab.setObjectName("device_tab")
        self.device_tabel = QtWidgets.QTableWidget(self.device_tab)
        self.device_tabel.setGeometry(QtCore.QRect(30, 30, 421, 321))
        self.device_tabel.setObjectName("device_tabel")
        self.device_tabel.setColumnCount(3)
        self.device_tabel.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.device_tabel.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.device_tabel.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.device_tabel.setHorizontalHeaderItem(2, item)
        self.connect_button = QtWidgets.QPushButton(self.device_tab)
        self.connect_button.setGeometry(QtCore.QRect(310, 400, 151, 32))
        self.connect_button.setObjectName("connect_button")
        self.hub_label = QtWidgets.QLabel(self.device_tab)
        self.hub_label.setGeometry(QtCore.QRect(230, 408, 81, 16))
        self.hub_label.setObjectName("hub_label")
        self.line = QtWidgets.QFrame(self.device_tab)
        self.line.setGeometry(QtCore.QRect(30, 360, 421, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.manually_connection_rbutton = QtWidgets.QRadioButton(self.device_tab)
        self.manually_connection_rbutton.setGeometry(QtCore.QRect(30, 370, 171, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.manually_connection_rbutton.setFont(font)
        self.manually_connection_rbutton.setObjectName("manually_connection_rbutton")
        self.tabs.addTab(self.device_tab, "")
        self.preference_tab = QtWidgets.QWidget()
        self.preference_tab.setObjectName("preference_tab")
        self.user_combo_box = QtWidgets.QComboBox(self.preference_tab)
        self.user_combo_box.setGeometry(QtCore.QRect(140, 30, 201, 26))
        self.user_combo_box.setObjectName("user_combo_box")
        self.user_combo_box.addItem("")
        self.user_combo_box.addItem("")
        self.user_combo_box.addItem("")
        self.user_combo_box.addItem("")
        self.user_combo_box.addItem("")
        self.user_combo_box.addItem("")
        self.user_label = QtWidgets.QLabel(self.preference_tab)
        self.user_label.setGeometry(QtCore.QRect(30, 30, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.user_label.setFont(font)
        self.user_label.setObjectName("user_label")
        self.manage_family_button = QtWidgets.QPushButton(self.preference_tab)
        self.manage_family_button.setGeometry(QtCore.QRect(340, 26, 131, 32))
        self.manage_family_button.setObjectName("manage_family_button")
        self.connection_label = QtWidgets.QLabel(self.preference_tab)
        self.connection_label.setGeometry(QtCore.QRect(30, 70, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.connection_label.setFont(font)
        self.connection_label.setObjectName("connection_label")
        self.connection_frame = QtWidgets.QFrame(self.preference_tab)
        self.connection_frame.setGeometry(QtCore.QRect(140, 70, 321, 41))
        self.connection_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.connection_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.connection_frame.setObjectName("connection_frame")
        self.host_label = QtWidgets.QLabel(self.connection_frame)
        self.host_label.setGeometry(QtCore.QRect(0, 0, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.host_label.setFont(font)
        self.host_label.setObjectName("host_label")
        self.port_label = QtWidgets.QLabel(self.connection_frame)
        self.port_label.setGeometry(QtCore.QRect(0, 20, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.port_label.setFont(font)
        self.port_label.setObjectName("port_label")
        self.connection_setup_button = QtWidgets.QPushButton(self.preference_tab)
        self.connection_setup_button.setGeometry(QtCore.QRect(340, 120, 131, 32))
        self.connection_setup_button.setObjectName("connection_setup_button")
        self.communication_label = QtWidgets.QLabel(self.preference_tab)
        self.communication_label.setGeometry(QtCore.QRect(30, 150, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.communication_label.setFont(font)
        self.communication_label.setObjectName("communication_label")
        self.interval_label = QtWidgets.QLabel(self.preference_tab)
        self.interval_label.setGeometry(QtCore.QRect(60, 180, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.interval_label.setFont(font)
        self.interval_label.setObjectName("interval_label")
        self.interval_combobox = QtWidgets.QComboBox(self.preference_tab)
        self.interval_combobox.setGeometry(QtCore.QRect(190, 180, 201, 26))
        self.interval_combobox.setObjectName("interval_combobox")
        self.interval_combobox.addItem("")
        self.interval_combobox.addItem("")
        self.interval_combobox.addItem("")
        self.interval_combobox.addItem("")
        self.interval_combobox.addItem("")
        self.interval_combobox.addItem("")
        self.interval_combobox.addItem("")
        self.interval_combobox.addItem("")
        self.interval_combobox.addItem("")
        self.interval_combobox.addItem("")
        self.interval_combobox.addItem("")
        self.apply_button = QtWidgets.QPushButton(self.preference_tab)
        self.apply_button.setGeometry(QtCore.QRect(360, 420, 121, 32))
        self.apply_button.setObjectName("apply_button")
        self.tabs.addTab(self.preference_tab, "")
        self.msg_label = QtWidgets.QLabel(self.centralwidget)
        self.msg_label.setGeometry(QtCore.QRect(20, 510, 461, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.msg_label.setFont(font)
        self.msg_label.setText("")
        self.msg_label.setObjectName("msg_label")
        self.msg_label_2 = QtWidgets.QFrame(self.centralwidget)
        self.msg_label_2.setGeometry(QtCore.QRect(20, 500, 491, 16))
        self.msg_label_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.msg_label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.msg_label_2.setObjectName("msg_label_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 525, 24))
        self.menubar.setObjectName("menubar")
        self.menuSHH_Edge = QtWidgets.QMenu(self.menubar)
        self.menuSHH_Edge.setObjectName("menuSHH_Edge")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout_Edge = QtWidgets.QAction(MainWindow)
        self.actionAbout_Edge.setObjectName("actionAbout_Edge")
        self.actionHide_Edge = QtWidgets.QAction(MainWindow)
        self.actionHide_Edge.setCheckable(False)
        self.actionHide_Edge.setEnabled(True)
        self.actionHide_Edge.setObjectName("actionHide_Edge")
        self.actionQuit_Egde = QtWidgets.QAction(MainWindow)
        self.actionQuit_Egde.setObjectName("actionQuit_Egde")
        self.actionUser_Manual = QtWidgets.QAction(MainWindow)
        self.actionUser_Manual.setObjectName("actionUser_Manual")
        self.actionLog = QtWidgets.QAction(MainWindow)
        self.actionLog.setObjectName("actionLog")
        self.menuSHH_Edge.addAction(self.actionAbout_Edge)
        self.menuSHH_Edge.addSeparator()
        self.menuSHH_Edge.addAction(self.actionHide_Edge)
        self.menuSHH_Edge.addAction(self.actionQuit_Egde)
        self.menuHelp.addAction(self.actionUser_Manual)
        self.menuView.addAction(self.actionLog)
        self.menubar.addAction(self.menuSHH_Edge.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())


        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ! [START] link UI components with the methods
        # TODO: transfer these codes into the updated UI file

        # ≈

        self.update_connection_setup()
        self.init_device_table()
        self.bp_button.clicked.connect(self.open_bp_window)
        self.hr_button.clicked.connect(self.open_hr_window)
        self.bm_button.clicked.connect(self.open_bm_window)
        self.weight_button.clicked.connect(self.open_weight_decide)
        # self.sure_button.clicked.connect(self.open_hr_monior)
        self.bp_measure_button.clicked.connect(self.open_bp_tips)
        self.manually_connection_rbutton.toggled.connect(self.auto_connection_mode)
        self.connect_button.clicked.connect(self.start_client)
        self.connection_setup_button.clicked.connect(self.open_connection_setup)
        self.apply_button.clicked.connect(self.update_connection_setup)

        self.msg_label.setText("Haa")
        self.health_record_button.clicked.connect(self.open_log_window)

        # ! [END] link UI components with the methods

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SHH Edge Computer"))
        self.health_record_button.setText(_translate("MainWindow", "Health\n""Report"))
        self.hr_button.setText(_translate("MainWindow", "Heart Rate"))
        self.bp_button.setText(_translate("MainWindow", "Blood\n""Pressure"))
        self.bm_button.setText(_translate("MainWindow", "Weight"))
        self.catergories_label.setText(_translate("MainWindow", "Health Catergories"))
        self.summary_label.setText(_translate("MainWindow", "Summary"))
        self.tabs.setTabText(self.tabs.indexOf(self.report_tab), _translate("MainWindow", "Report"))
        self.weight_button.setText(_translate("MainWindow", "Weight"))
        self.update_button.setText(_translate("MainWindow", "update data"))
        self.bp_measure_button.setText(_translate("MainWindow", "Blood Pressure"))
        # self.sure_button.setText(_translate("MainWindow", "Heart Rate"))
        self.tabs.setTabText(self.tabs.indexOf(self.measurement_tab), _translate("MainWindow", "Measurement"))
        item = self.device_tabel.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.device_tabel.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Device Name"))
        item = self.device_tabel.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        self.connect_button.setText(_translate("MainWindow", "Check Status"))
        self.connect_button.setStyleSheet("font: 9pt \"Arial\";")
        self.connect_button_2.setText(_translate("MainWindow", "Bind"))
        self.connect_button_2 = QtWidgets.QPushButton(self.device_tab)
        self.connect_button_2.setGeometry(QtCore.QRect(320, 470, 151, 41))
        self.connect_button_2.setStyleSheet("font: 9pt \"Arial\";")
        self.connect_button_2.setObjectName("connect_button_2")
        self.hub_label.setText(_translate("MainWindow", "Mobile Hub:"))
        self.manually_connection_rbutton.setText(_translate("MainWindow", "Auto Connections"))
        self.tabs.setTabText(self.tabs.indexOf(self.device_tab), _translate("MainWindow", "Device"))
        self.user_combo_box.setItemText(0, _translate("MainWindow", "Jack (Dad, Admin)"))
        self.user_combo_box.setItemText(1, _translate("MainWindow", "Rose (Mom, Admin)"))
        self.user_combo_box.setItemText(2, _translate("MainWindow", "Bob (Son)"))
        self.user_combo_box.setItemText(3, _translate("MainWindow", "Candy (Daughter)"))
        self.user_combo_box.setItemText(4, _translate("MainWindow", "Tom (Grandpa)"))
        self.user_combo_box.setItemText(5, _translate("MainWindow", "Molly (Grandma)"))
        self.user_label.setText(_translate("MainWindow", "Current User:"))
        self.manage_family_button.setText(_translate("MainWindow", "Manage Family"))
        self.connection_label.setText(_translate("MainWindow", "Connection:"))
        self.host_label.setText(_translate("MainWindow", "Client Host:"))
        self.port_label.setText(_translate("MainWindow", "Client Port:"))
        self.connection_setup_button.setText(_translate("MainWindow", "Manually Setup"))
        self.communication_label.setText(_translate("MainWindow", "Communication:"))
        self.interval_label.setText(_translate("MainWindow", "Request Interval:"))
        self.interval_combobox.setItemText(0, _translate("MainWindow", "10 minutes (default)"))
        self.interval_combobox.setItemText(1, _translate("MainWindow", "30 seconds"))
        self.interval_combobox.setItemText(2, _translate("MainWindow", "1 minute"))
        self.interval_combobox.setItemText(3, _translate("MainWindow", "2 minutes"))
        self.interval_combobox.setItemText(4, _translate("MainWindow", "5 minutes"))
        self.interval_combobox.setItemText(5, _translate("MainWindow", "30 minutes"))
        self.interval_combobox.setItemText(6, _translate("MainWindow", "1 hour"))
        self.interval_combobox.setItemText(7, _translate("MainWindow", "2 hours"))
        self.interval_combobox.setItemText(8, _translate("MainWindow", "6 hours"))
        self.interval_combobox.setItemText(9, _translate("MainWindow", "12 hours"))
        self.interval_combobox.setItemText(10, _translate("MainWindow", "24 hours"))
        self.apply_button.setText(_translate("MainWindow", "Apply"))
        self.tabs.setTabText(self.tabs.indexOf(self.preference_tab), _translate("MainWindow", "Preferences"))
        self.menuSHH_Edge.setTitle(_translate("MainWindow", "SHH-Edge"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionAbout_Edge.setText(_translate("MainWindow", "About Edge"))
        self.actionAbout_Edge.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionHide_Edge.setText(_translate("MainWindow", "Hide Edge"))
        self.actionHide_Edge.setShortcut(_translate("MainWindow", "Alt+H"))
        self.actionQuit_Egde.setText(_translate("MainWindow", "Quit Egde"))
        self.actionQuit_Egde.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionUser_Manual.setText(_translate("MainWindow", "User Manual"))
        self.actionUser_Manual.setShortcut(_translate("MainWindow", "Ctrl+Alt+H"))
        self.actionLog.setText(_translate("MainWindow", "Log"))
        self.actionLog.setShortcut(_translate("MainWindow", "Ctrl+L"))

    # ! [START] define customized methods
    # TODO: transfer these codes into the updated UI file

    def open_scheduler(self):
        import view.scheduler.scheduler1
        self.new_window = QtWidgets.QDialog()
        self.scheduler_alert = view.scheduler.scheduler1.Ui_Dialog()
        self.scheduler_alert.setupUi(self.new_window)
        self.new_window.exec()

    def init_device_table(self):
        sensor_data = GlobalVar.get_list("sensor")
        mobile_data = GlobalVar.get_list("mobile")
        iot_data = GlobalVar.get_list("iot")
        MD_data = GlobalVar.get_list("MD")
        # rowPosition = self.device_tabel.rowCount()
        # self.device_tabel.insertRow(rowPosition)

        column_header = []

        for column, key in enumerate(MD_data.keys()):
            # column_header.append(key)
            self.device_tabel.horizontalHeader().setSectionResizeMode(column, QtWidgets.QHeaderView.Stretch)

            for row, item in enumerate(MD_data[key]):

                if column == 0:
                    self.device_tabel.insertRow(row)

                self.device_tabel.setItem(row, column, QtWidgets.QTableWidgetItem(item))

        for column, key in enumerate(mobile_data.keys()):
            for row, item in enumerate(mobile_data[key]):

                if column == 0:
                    self.device_tabel.insertRow(row)

                self.device_tabel.setItem(row, column, QtWidgets.QTableWidgetItem(item))

        for column, key in enumerate(iot_data.keys()):
            for row, item in enumerate(iot_data[key]):

                if column == 0:
                    self.device_tabel.insertRow(row)

                self.device_tabel.setItem(row, column, QtWidgets.QTableWidgetItem(item))

        for column, key in enumerate(sensor_data.keys()):
            for row, item in enumerate(sensor_data[key]):

                if column == 0:
                    self.device_tabel.insertRow(row)

                self.device_tabel.setItem(row, column, QtWidgets.QTableWidgetItem(item))

                # print each item
                # print("row: {row}, column: {column}, item: {item}".format(row = row, column = column, item = item))

        # self.device_tabel.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)


    def update_device_table(self):
        self.device_tabel.setRowCount(0)
        self.device_tabel.clearContents()
        self.init_device_table()

    def auto_connection_mode(self):

        radio_button = self.sender()

        if radio_button.isChecked():
            self.hub_label.setEnabled(False)
            self.connect_button.setText("Auto Mode")
            self.connect_button.setEnabled(False)
            GlobalVar.set_value("dict", "hub_auto_connect", True)
        else:
            if self.client_thread.isRunning():
                self.hub_label.setEnabled(True)
                self.connect_button.setText("Disconnect")
                self.connect_button.setEnabled(True)
            else:
                self.hub_label.setEnabled(True)
                self.connect_button.setText("Connect")
                self.connect_button.setEnabled(True)
            GlobalVar.set_value("dict", "hub_auto_connect", False)

    def start_event(self):

        Utility.generate_event(priority=4,
                               module="Ui_MainWindow.start_event",
                               log_info="Event processing thread started.")

        # move client_worker to the client_thread
        self.event_worker.moveToThread(self.event_thread)

        # connect signals and slots
        self.event_thread.started.connect(self.event_worker.run)
        self.event_worker.finished.connect(self.event_thread.quit)
        self.event_worker.finished.connect(self.event_worker.deleteLater)
        self.event_thread.finished.connect(self.event_thread.deleteLater)

        self.event_worker.progress.connect(self.print_progress)

        # start the event_thread
        self.event_thread.start()

    def print_progress(self, text):
        print("MainWindow: {info}".format(info=text))
        self.msg_label.setText(text)

    # def open_bp_window(self):
    #     """
    #     * Open a new blood pressure window
    #     @param self: the instance of Ui_MainWindow class
    #     """
    #     self.window = QtWidgets.QMainWindow()
    #     self.bp_sub_window = Ui_bp_window()  # initialize BP window object
    #     self.bp_sub_window.setup(self.window)  # setup new BP window
    #     self.window.show()  # display new BP window

    def open_bp_window(self):
        """
        * Open a new blood pressure window
        @param self: the instance of Ui_MainWindow class
        """
        if graph.bp_report_producer() == 0:
            self.window = QtWidgets.QDialog()
            self.bp_alert = Ui_bp_alert()
            self.bp_alert.setupUi(self.window)
            self.window.show()
        else:
            self.window = QtWidgets.QMainWindow()
            self.bp_sub_window = Ui_bp_window()  # initialize BP window object
            self.bp_sub_window.setup(self.window)  # setup new BP window
            self.window.show()  # display new BP window

    def open_hr_window(self):
        """
        * Open a new heart rate window
        @param self: the instance of Ui_MainWindow class
        """
        if graph.hr_report_hour() == 0 or graph.hr_report_24hour() == 0:
            self.window = QtWidgets.QDialog()
            self.hr_alert = Ui_hr_alert()
            self.hr_alert.setupUi(self.window)
            self.window.show()
        else:
            self.window = QtWidgets.QMainWindow()
            self.hr_sub_window = Ui_hr_window()  # initialize HR window object
            self.hr_sub_window.setup(self.window)  # setup new HR window
            self.window.show()  # display new HR window

    def open_bm_window(self):
        """
        * Open a new body mass (weight) window
        @param self: the instance of Ui_MainWindow class
        """
        if graph.bm_report_producer() == 0 :
            self.window = QtWidgets.QDialog()
            self.bm_alert = Ui_bm_alert()
            self.bm_alert.setupUi(self.window)
            self.window.show()
        else:
            self.window = QtWidgets.QMainWindow()
            self.bm_sub_window = Ui_bm_window()  # initialize BM window object
            self.bm_sub_window.setup(self.window)  # setup new BM window
            self.window.show()  # display new BM window


    def open_weight_decide(self):
        """
        * Open a new body mass (weight) window
        @param self: the instance of Ui_MainWindow class
        """
        self.window = QtWidgets.QMainWindow()
        self.sub_weight_decide = Ui_weight_decide()
        self.sub_weight_decide.setup(self.window)
        self.window.show()

    def open_bp_tips(self):

        self.window = QtWidgets.QDialog()
        self.sub_bp_measure = view.measurement.bp_meamurement.bp_tip.Ui_bp_tips()
        self.sub_bp_measure.setup(self.window)
        self.window.show()

    def open_bp_measure(self):
        graph.bp_report_producer()
        self.window = QtWidgets.QDialog()
        self.sub_bp_measure = Ui_bp_measure()
        self.sub_bp_measure.setup(self.window)
        self.window.show()

    def open_connection_setup(self):

        import view.connection.connection_setup

        self.window = QtWidgets.QDialog()
        self.connection_setup = view.connection.connection_setup.Ui_Dialog()
        self.connection_setup.setup(self.window)
        self.window.show()

    def start_client(self):
        self.connect_status_process_show()

        self.connect_button.setEnabled(False)
        self.status_thread = QThread()
        self.status_worker = CheckingStatusThread()

        self.status_worker.moveToThread(self.status_thread)
        self.status_thread.started.connect(self.status_worker.run)
        self.status_worker.exception.connect(self.status_thread.terminate)
        self.status_worker.exception.connect(self.re_activate_status)
        self.status_worker.exception.connect(self.exception_show)
        self.status_worker.exception.connect(self.connect_status.close_window)
        self.status_worker.finished.connect(self.status_thread.terminate)
        self.status_worker.finished.connect(self.re_activate_status)
        self.status_worker.finished.connect(self.update_device_table)
        self.status_worker.finished.connect(self.connect_status_success_show)
        self.status_worker.finished.connect(self.connect_status.close_window)
        self.status_worker.progress.connect(self.connect_status.progress_ui)
        self.status_worker.progress_int.connect(self.connect_status.progress_bar)

        self.status_worker.run()

        # self.thread_lock.lock()

        # # create a QThread object
        # self.client_thread = QThread()

        # # create a client_worker object
        # self.client_worker = ClientThread()

        # move client_worker to the client_thread
        # self.client_worker.moveToThread(self.client_thread)

        # connect signals and slots
        # self.client_thread.started.connect(self.client_worker.run)
        # self.client_worker.finished.connect(self.client_thread.quit)
        # self.client_worker.finished.connect(self.client_worker.deleteLater)
        # self.client_thread.finished.connect(self.client_thread.deleteLater)

        # start the client_thread
        # self.client_thread.start()

        # final resets
        # self.connect_button.setEnabled(False)
        # self.connect_button.setText("Disconnect")

        # self.client_thread.finished.connect(
        #     lambda: self.connect_button.setEnabled(True)
        # )

        # self.client_thread.finished.connect(
        #     lambda: self.bp_label.setText("Long-Running Step: 0")
        # )

        # self.thread_lock.unlock()

    def bind_hub(self):
        import view.component.pair_dialog
        # 出现新的窗口
        self.pairing_progress_show()

        self.connect_button_2.setEnabled(False)
        self.binding_thread = QThread()
        self.binding_worker = BindingThread()

        self.binding_worker.moveToThread(self.binding_thread)
        self.binding_thread.started.connect(self.binding_worker.run)
        self.binding_worker.exception.connect(self.binding_thread.terminate)
        self.binding_worker.exception.connect(self.re_activate_bind)
        self.binding_worker.exception.connect(self.exception_show)
        self.binding_worker.exception.connect(self.pair_dialog.close_window)
        self.binding_worker.finished.connect(self.binding_thread.terminate)
        self.binding_worker.finished.connect(self.update_device_table)
        self.binding_worker.finished.connect(self.re_activate_bind)
        self.binding_worker.finished.connect(self.pairing_success_show)
        self.binding_worker.finished.connect(self.pair_dialog.close_window)
        self.binding_worker.progress.connect(self.pair_dialog.progress_ui)
        self.binding_worker.progress_int.connect(self.pair_dialog.progress_bar)

        self.binding_thread.start()

    def re_activate_status(self):
        self.connect_button.setEnabled(True)

    def re_activate_bind(self):
        self.connect_button_2.setEnabled(True)

    def pairing_progress_show(self):
        import view.component.pair_dialog
        self.window = QtWidgets.QDialog()
        self.pair_dialog = view.component.pair_dialog.Ui_pairing()
        self.pair_dialog.setupUi(self.window)
        self.window.show()

    def exception_show(self):
        import view.component.connectionTimeout
        self.window = QtWidgets.QDialog()
        self.timeout = view.component.connectionTimeout.Ui_timeout()
        self.timeout.setupUi(self.window)
        self.window.show()

    def pairing_success_show(self):
        import view.component.pair_successful_dialog
        self.window = QtWidgets.QDialog()
        self.pairing_success = view.component.pair_successful_dialog.Ui_PairingSuccess()
        self.pairing_success.setupUi(self.window)
        self.window.show()

    def connect_status_process_show(self):
        import view.component.connect_status
        self.window = QtWidgets.QDialog()
        self.connect_status = view.component.connect_status.Ui_Dialog()
        self.connect_status.setupUi(self.window)
        self.window.show()

    def connect_status_success_show(self):
        import view.component.connect_status_successful_dialog
        self.window = QtWidgets.QDialog()
        self.connect_status_success = view.component.connect_status_successful_dialog.Ui_StatusAcquire()
        self.connect_status_success.setupUi(self.window)
        self.window.show()

    # def update_info(self, data):
        # 更新窗口新的内容


    def open_hr_monitor(self):

        import view.report.hr_report.hr_monitor

        self.window = QtWidgets.QDialog()
        self.connection_setup = view.report.hr.hr_monitor.Ui_Monitor()
        self.connection_setup.setup(self.window)
        self.window.show()

    # def open_log_window(self):
    #
    #     import view.logs
    #
    #     # self.window = QtWidgets.QDialog()
    #     # self.log_window = view.logs.Ui_SystemLogs()
    #     # self.log_window.setup(self.window)
    #     # self.window.show()
    #
    #     self.log_window = QtWidgets.QDialog()
    #     self.log_window = view.logs.Ui_SystemLogs()
    #     self.log_window.show()

    def open_health_report(self):

        if graph.weekly_report_producer() == 0 or graph.monthly_report_producer() == 0:
            self.window = QtWidgets.QDialog()
            self.report_alert = Ui_report_alert()
            self.report_alert.setupUi(self.window)
            self.window.show()
        else:
            self.window = QtWidgets.QMainWindow()
            self.report_window = Ui_report_window()
            self.report_window.setup(self.window)
            self.window.show()


    def update_info(self):
        self.update_data_progress_bar.setVisible(True)
        self.update_data_progress_bar.setValue(0)
        print(Counter.get_process_counter(self))
        self.download()
        # start = '2021-07-01T06:01:06.000Z'
        # stop = '2022-01-24T06:16:06.206Z'
        # db_delete_data.DeleteByDays(start, stop)
        # db_delete_data.DeleteByDays(start, stop)
        # db_delete_data.DeleteByDays(start, stop)
        # db_delete_data.DeleteByDays(start, stop)
        data_process()
        self.update_data_progress_bar.setValue(95)
        sleep(5)
        self.update_data_progress_bar.setValue(100)
        self.update_data_progress_bar.setVisible(False)

        DataIO.refresh_BM_plot_file()
        DataIO.refresh_BP_plot_file("new")
        Plotter.generate_HR_trends(Plotter, True)
        print("hello")

    def update_connection_setup(self):
        # communication_interval = self.interval_combobox.currentText()
        # communication_interval_minute = Utility.text_to_minute(communication_interval)
        # GlobalVar.set_value("client", "request_interval", communication_interval_minute)
        self.host_label.setText("Client Host: {host}".format(host=GlobalVar.get_value("client", "client_host")))
        self.port_label.setText("Client Port: {port}".format(port=GlobalVar.get_value("client", "client_port")))
        height = self.height_edit.text()
        if len(height) != 0:
            GlobalVar.set_value("height", "h", height)


    def closeEvent(self, event):
        close = QtWidgets.QMessageBox.information(self,
                                                  "Quit SHH Edge Software",
                                                  "Are you sure you want to quit the software?\nIt might take few seconds to save the data.",
                                                  QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def download(self):
        hostname = '192.168.50.32'
        port = 22
        username = 'root'
        password = 'handofking'
        remote_path = '/home/grp_remote_repository'
        local_path = "model\\data_dir"
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=hostname, port=port, username=username, password=password)

        sftp_client = client.open_sftp()
        remote_file = sftp_client.listdir(remote_path)

        print(len(remote_file))

        if (len(remote_file) == 0):
            self.update_data_progress_bar.setValue(33)
            return

        Counter.init_bar_counter(Counter, len(remote_file))
       # print(Counter.get_counter(len(remote_file)) * 6)
        for dir_name in remote_file:
            remote_dir_path = remote_path + "/" + dir_name
            detail_files = sftp_client.listdir(remote_dir_path)
            local_file_path = local_path + "\\" + dir_name
            if not os.path.exists(local_file_path):
                os.mkdir(local_file_path)
                for detail_file in detail_files:
                    remote_file_path = remote_dir_path + "/" + detail_file
                    local_file_paths = local_file_path + "\\" + detail_file
                    print(local_file_paths)
                    sftp_client.get(remote_file_path, local_file_paths)
                    Counter.add_process_counter(self)
                    self.update_data_progress_bar.setValue(Counter.get_process_counter(self))

        self.update_data_progress_bar.setValue(33)


    def start_main_window():
        """
        * Method to start this main window (to be called by main method)
        """

        app = QtWidgets.QApplication(sys.argv)
        # MainWindow = QtWidgets.QMainWindow()
        # ui = Ui_MainWindow()
        # ui.setupUi(MainWindow)
        # MainWindow.show()
        # sys.exit(app.exec_())

        ui = Ui_MainWindow()
        ui.show()

        # create a scheduler for alarm
        sys.exit(app.exec_())

    # ! [END] define customized methods



# class Client(QObject):
#     finished = pyqtSignal()
#     progress = pyqtSignal(int)

#     def run(self):

#         client_host = GlobalVar.get_value("client", "client_host")
#         client_port = int(GlobalVar.get_value("client", "client_port"))
#         comm_interval = GlobalVar.get_value("client", "request_interval")

#         try:
#             # self.progress.emit(1)
#             client = SocketClient(client_host, client_port)
#             client.client_startRecording(comm_interval)
#             client.client_requestForData(comm_interval)
#         except Exception as exce:
#             print("[Error] Client: {info}".format(info = exce))

#         # self.finished.emti()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())

    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
