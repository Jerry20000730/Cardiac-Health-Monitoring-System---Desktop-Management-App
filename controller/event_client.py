from PyQt5.QtCore import QObject, pyqtSignal
import sys
import os
import time
from model.global_var import GlobalVar, EventQuene
import random

"""
Author: GRP group 14
"""
class EventThread(QObject):
    
    finished = pyqtSignal()
    progress = pyqtSignal(str)

    def run(self):
    
        try:
            while True:
                
                print("------------------")
                print("GET...")
                event = EventQuene.get_event()
                info = "[{type}] {time}\n{info}".format(time = event[1][0][0 : len(event[1][0]) - 7], type = event[1][1], info = event[1][4])
                self.progress.emit(info)
                EventQuene.print_quene()
                print("------------------")
                
                time.sleep(2)
            
        except Exception as exce:
            print("[Error] EventThread: {info}".format(info = exce))

        self.finished.emit()
        