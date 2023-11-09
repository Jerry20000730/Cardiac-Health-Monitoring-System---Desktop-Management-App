# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logs.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from controller.data_io import DataIO

from model.global_var import GlobalVar

"""
Author: GRP group 14
"""
class Ui_SystemLogs(QtWidgets.QDialog):
    
    def __init__(self, parent = None):
        super(QtWidgets.QDialog, self).__init__(parent)
        
        uic.loadUi('view/logs.ui', self)
        
        self.init_table()
        self.close_button.clicked.connect(self.close)
        self.log_table.clicked.connect(self.get_clicked_value)
        self.refresh_button.clicked.connect(self.refresh_table)
        self.clear_button.clicked.connect(self.clear_logs)
        

    def retranslateUi(self, SystemLogs):
        _translate = QtCore.QCoreApplication.translate
        SystemLogs.setWindowTitle(_translate("SystemLogs", "System Logs"))
        self.clear_button.setText(_translate("SystemLogs", "Clear Logs"))
        self.close_button.setText(_translate("SystemLogs", "Close"))
        self.export_button.setText(_translate("SystemLogs", "Export Logs"))
        item = self.log_table.horizontalHeaderItem(0)
        item.setText(_translate("SystemLogs", "Date"))
        item = self.log_table.horizontalHeaderItem(1)
        item.setText(_translate("SystemLogs", "Time"))
        item = self.log_table.horizontalHeaderItem(2)
        item.setText(_translate("SystemLogs", "Type"))
        item = self.log_table.horizontalHeaderItem(3)
        item.setText(_translate("SystemLogs", "Priority"))
        item = self.log_table.horizontalHeaderItem(4)
        item.setText(_translate("SystemLogs", "Log Information"))
        self.pushButton.setText(_translate("SystemLogs", "Refresh"))
        
    def refresh_table(self):
        self.log_table.setRowCount(0)
        self.init_table()
        print("[INFO] Ui_SystemLogs.refresh_table: refreshed!")
        
        
    def clear_logs(self):
        
        close = QtWidgets.QMessageBox.warning(self,
                                    "Clear all system logs",
                                    "Are you sure you want to clear all system logs?\nThis operation is irrevocable.",
                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            print("clearing")
            DataIO.clear_logs()
            self.log_table.setRowCount(0)
            self.init_table()
        
    def clicked_mapping_signal(self):
        self.log_table.clicked.connect(self.get_clicked_value)
        
    def get_clicked_value(self, item):
        text = self.log_table.item(item.row(), item.column()).text()
        header = self.log_table.horizontalHeaderItem(item.column()).text()
        self.detail_info.setText("[{header}]: {info}".format(header = header, info = text))
 
        
    def init_table(self):
        
        data = GlobalVar.get_list("logs")
        print(data)
        
        # rowPosition = self.log_table.rowCount()
        # self.log_table.insertRow(rowPosition)
        
        column_header = []
        for column, key in enumerate(data.keys()):
            # column_header.append(key)
            
            self.log_table.horizontalHeader().setSectionResizeMode(column, QtWidgets.QHeaderView.Stretch)

            for row, item in enumerate(data[key]):
                
                if column == 0:
                    self.log_table.insertRow(row)
                
                self.log_table.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))
                
                # print("row: {row}, column: {column}, item: {item}".format(row = row, column = column, item = item))
        
        # self.log_table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

