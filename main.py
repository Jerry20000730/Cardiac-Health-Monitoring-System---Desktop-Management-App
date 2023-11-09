import sys
import os
from view.main_window import Ui_MainWindow
from model.global_var import GlobalVar, EventQuene
from controller.data_io import *
from controller.plotter import *
import subprocess
"""
Author: GRP group 14
"""

if __name__ == "__main__":
    GlobalVar._init()
    EventQuene._init()
    # start connections
    # start database server

    path = os.path.join(os.getcwd(), "influxdb")
    command = 'cd ' + path + ' && ' + 'start influxd.exe'
    subprocess.run(command, shell=True)
    # start user interface
    Ui_MainWindow.start_main_window()

