# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'short_assessment.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from model.global_var import GlobalVar
"""
Author: GRP group 14
"""
class Ui_Dialog(object):
    def setup(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 800)
        Dialog.setMinimumSize(QtCore.QSize(600, 780))
        Dialog.setMaximumSize(QtCore.QSize(600, 780))
        self.close_button = QtWidgets.QPushButton(Dialog)
        self.close_button.setGeometry(QtCore.QRect(122, 730, 141, 32))
        self.close_button.setObjectName("close_button")
        self.suggestion_button = QtWidgets.QPushButton(Dialog)
        self.suggestion_button.setGeometry(QtCore.QRect(260, 730, 181, 32))
        self.suggestion_button.setObjectName("suggestion_button")
        self.figure_frame = QtWidgets.QFrame(Dialog)
        self.figure_frame.setGeometry(QtCore.QRect(30, 10, 541, 521))
        self.figure_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.figure_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.figure_frame.setObjectName("figure_frame")
        self.assessment_fig = QtWidgets.QLabel(self.figure_frame)
        self.assessment_fig.setGeometry(QtCore.QRect(10, 30, 421, 291))
        self.assessment_fig.setText("")
        self.assessment_fig.setPixmap(QtGui.QPixmap(GlobalVar.get_value("path", "short_assessment_sample")))
        self.assessment_fig.setScaledContents(True)
        self.assessment_fig.setObjectName("assessment_fig")
        self.assessment_fig_label = QtWidgets.QLabel(self.figure_frame)
        self.assessment_fig_label.setGeometry(QtCore.QRect(10, 10, 231, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.assessment_fig_label.setFont(font)
        self.assessment_fig_label.setObjectName("assessment_fig_label")
        self.ecg_fig_label = QtWidgets.QLabel(self.figure_frame)
        self.ecg_fig_label.setGeometry(QtCore.QRect(10, 340, 231, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ecg_fig_label.setFont(font)
        self.ecg_fig_label.setObjectName("ecg_fig_label")
        self.ecg_fig = QtWidgets.QLabel(self.figure_frame)
        self.ecg_fig.setGeometry(QtCore.QRect(10, 370, 521, 141))
        self.ecg_fig.setText("")
        self.ecg_fig.setPixmap(QtGui.QPixmap(QtGui.QPixmap(GlobalVar.get_value("path", "arrhythmia_ecg_sample"))))
        self.ecg_fig.setScaledContents(True)
        self.ecg_fig.setObjectName("ecg_fig")
        self.heart_event_label = QtWidgets.QLabel(Dialog)
        self.heart_event_label.setGeometry(QtCore.QRect(30, 650, 541, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.heart_event_label.setFont(font)
        self.heart_event_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.heart_event_label.setObjectName("heart_event_label")
        self.heart_event_text = QtWidgets.QLabel(Dialog)
        self.heart_event_text.setGeometry(QtCore.QRect(30, 670, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.heart_event_text.setFont(font)
        self.heart_event_text.setAutoFillBackground(False)
        self.heart_event_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.heart_event_text.setObjectName("heart_event_text")
        self.report_label = QtWidgets.QLabel(Dialog)
        self.report_label.setGeometry(QtCore.QRect(30, 550, 541, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.report_label.setFont(font)
        self.report_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.report_label.setObjectName("report_label")
        self.report_text = QtWidgets.QLabel(Dialog)
        self.report_text.setGeometry(QtCore.QRect(30, 570, 541, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.report_text.setFont(font)
        self.report_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.report_text.setWordWrap(True)
        self.report_text.setObjectName("report_text")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Short-term Assessment"))
        self.close_button.setText(_translate("Dialog", "Save and Close"))
        self.suggestion_button.setText(_translate("Dialog", "More Suggestions..."))
        self.assessment_fig_label.setText(_translate("Dialog", "Assessment Plot (10 minutes):"))
        self.ecg_fig_label.setText(_translate("Dialog", "ECG Excerpts (10 seconds):"))
        self.heart_event_label.setText(_translate("Dialog", "Heart Events:"))
        self.heart_event_text.setText(_translate("Dialog", "1. Premature ventricular contraction\n"
"2. Bundle branch block beat (unspecified)"))
        self.report_label.setText(_translate("Dialog", "Heart Report:"))
        self.report_text.setText(_translate("Dialog", "Your assessment result is slightly out of the bounds.\n"
"Please pay attention to your cardiovascular health and adopt a healthier lifestyle."))

