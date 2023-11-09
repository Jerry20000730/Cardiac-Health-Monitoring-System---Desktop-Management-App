import sys
import socket
from PyQt5.QtCore import QObject,pyqtSignal
from controller.utility import Utility
import random
import time

from model.global_var import EventQuene, GlobalVar


class Header:

    def __init__(self, instrCMD=0):
        self.instrCMD = instrCMD
        self.id = 255
        self.packageNum = 0
        self.totalPackageNum = 0
        self.packageLength = 0

    def createHeaderByList(self, inputList=[]):
        assert len(inputList) == 14
        self.instrCMD = int(inputList[0])
        self.id = int(inputList[1])
        self.packageNum = int.from_bytes(inputList[2:6], byteorder='big')
        self.totalPackageNum = int.from_bytes(inputList[6:10], byteorder='big')
        self.packageLength = int.from_bytes(inputList[10:14], byteorder='big')

    def createHeaderByComponent(self, instrCMD=0, id=0, packageNum=[], totalPackageNum=[], packageLength=[]):
        assert len(packageNum) == 4 and len(totalPackageNum) == 4 and len(packageLength) == 4
        self.instrCMD = int(instrCMD)
        self.id = int(id)
        self.packageNum = int.from_bytes(packageNum, byteorder='big')
        self.totalPackageNum = int.from_bytes(totalPackageNum, byteorder='big')
        self.packageLength = int.from_bytes(packageLength, byteorder='big')

    def printInfo(self):
        print("[INFO] Receive header, cmd: " + str(self.instrCMD) + ", packageID: " + str(self.id) \
              + ", package number: " + str(self.packageNum) + ", package total number: " + str(self.totalPackageNum) \
              + ", package length" + str(self.packageLength))

    def transToByteArray(self):
        instrCMDByteArr = self.instrCMD.to_bytes(1, byteorder='big')
        idByteArr = self.id.to_bytes(1, byteorder='big')
        packageNumArr = self.packageNum.to_bytes(4, byteorder='big')
        totalPackageNumArr = self.totalPackageNum.to_bytes(4, byteorder='big')
        packageLengthArr = self.packageLength.to_bytes(4, byteorder='big')

        header_in_bytes = instrCMDByteArr + idByteArr + packageNumArr + totalPackageNumArr + packageLengthArr
        return header_in_bytes


class SocketClient():

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.port = port

    def client_initialBind(self, sensorConnectionList=[]):
        assert len(sensorConnectionList) != 0
        # create socket
        print("[INFO] Client: Creating a socket...")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(20)
        except socket.error:
            print("[ERROR] Client: failed to create socket!")
        print("[INFO] Client: Socket successfully created.")

        # connect to socket server
        s.connect((self.host, self.port))
        print("[INFO] Client: Connecting to server: " + str(self.host) + " on port: " + str(self.port))

        # sending request to server
        # instructionCMD = 1 <- initialBinding
        header = Header(1)
        request = header.transToByteArray() + bytes(",".join(sensorConnectionList), encoding='utf8')
        print("[INFO] Client: Sending sensor information to Hub")

        # sending and receiving
        try:
            s.sendall(request)
            header = Header()
            header.createHeaderByList(list(s.recv(14)))
            receivedInfo = ""
            if (header.instrCMD == 1):
                # info is the feedback from the hub, with its Hubid
                # e.g. HUB001
                receivedInfo = s.recv(1024).decode('utf-8')
                print(receivedInfo)
            return receivedInfo
        except socket.error:
            print(socket.error)
            print("[Error] Client: Send failed.")


    # connectionList is the name list of ble device for client to send to the server
    # e.g. ["CL880", "CL831", "CL800"]
    def client_requestForConnectionStatus(self, connectionList=[]):
        assert len(connectionList) != 0
        # create socket
        print("[INFO] Client: Creating a socket...")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(20)
        except socket.error:
            print("[ERROR] Client: failed to create socket!")
        print("[INFO] Client: Socket successfully created.")

        # connect to socket server
        s.connect((self.host, self.port))
        print("[INFO] Client: Connecting to server: " + str(self.host) + " on port: " + str(self.port))

        # sending request to server
        # instructionCMD = 2 <- requestForDeviceStatus
        header = Header(2)
        request = header.transToByteArray() + bytes(",".join(connectionList), encoding='utf8')
        print("[INFO] Client: Sending device connection request to server...")

        # sending and receiving
        try:
            s.sendall(request)
            header = Header()
            header.createHeaderByList(list(s.recv(14)))
            if (header.instrCMD == 2):
                # info is the feedback from the server
                # e.g. "CL880,1,CL800,1,CL831,1"
                receivedInfo = s.recv(1024).decode('utf-8')
                receivedInfoDict = self.trans_feedback_to_dict(receivedInfo)
                print(receivedInfoDict)
            return receivedInfoDict
        except socket.error:
            print(socket.error)
            print("[Error] Client: Send failed.")

    def trans_feedback_to_dict(self, receivedInfo):
        receivedInfoList = receivedInfo.split(',')
        assert len(receivedInfoList) % 2 == 0
        keyList = receivedInfoList[::2]
        valueList = receivedInfoList[1::2]
        receivedInfoDict = dict(zip(keyList, valueList))
        return receivedInfoDict


class BindingThread(QObject):
    finished = pyqtSignal()
    exception = pyqtSignal()
    no_reply = pyqtSignal()
    progress = pyqtSignal(str)
    progress_int = pyqtSignal(int)

    def run(self):

        client_host = GlobalVar.get_value("client", "client_host")
        client_port = int(GlobalVar.get_value("client", "client_port"))

        try:
            client = SocketClient(client_host, client_port)
            self.progress.emit("Sending Sensor Information")
            self.progress_int.emit(0)
            returnInfo = client.client_initialBind(GlobalVar.get_value("sensor", "ID"))
            self.progress.emit("Receiving Hub information")
            self.progress_int.emit(25)
            if (returnInfo != ""):
                update_id = GlobalVar.get_value("mobile", "ID")
                update_id.append(returnInfo.strip("\n"))
                update_name = GlobalVar.get_value("mobile", "Name")
                update_name.append("Mobile Hub")
                update_status = GlobalVar.get_value("mobile", "Status")
                update_status.append("Connected")

                self.progress.emit("Updating device table")
                self.progress_int.emit(50)

                GlobalVar.set_value("mobile", "ID", update_id)
                GlobalVar.set_value("mobile", "Name", update_name)
                GlobalVar.set_value("mobile", "Status", update_status)

                self.progress.emit("Pairing success")
                self.progress_int.emit(100)
                self.finished.emit()
            else:
                self.no_reply.emit()

        except Exception as exce:
            print("[Error] Client: {info}".format(info=exce))
            self.exception.emit()
            
        # self.thread_lock.unlock()
        # self.finished.emit()

class CheckingStatusThread(QObject):
    finished = pyqtSignal()
    exception = pyqtSignal()
    no_reply = pyqtSignal()
    progress = pyqtSignal(str)
    progress_int = pyqtSignal(int)

    def run(self):
        self.progress.emit("Connecting...")
        client_host = GlobalVar.get_value("client", "client_host")
        client_port = int(GlobalVar.get_value("client", "client_port"))

        try:
            client = SocketClient(client_host, client_port)
            self.progress.emit("Sending Sensor Information")
            self.progress_int.emit(0)
            returnInfo = client.client_requestForConnectionStatus(GlobalVar.get_value("sensor", "ID"))
            self.progress.emit("Receiving Hub information")
            self.progress_int.emit(25)
            if (returnInfo != ""):
                self.transformDictToStatus(returnInfo)
            else:
                self.no_reply.emit()

        except Exception as exce:
            print("[Error] Client: {info}".format(info=exce))
            self.exception.emit()

    def transformDictToStatus(self, sensor_status_dict):
        sensor_list = GlobalVar.get_value("sensor", "ID")
        sensor_status = []
        self.progress.emit("Updating device table")
        self.progress_int.emit(50)
        for sensor_id in sensor_list:
            if sensor_status_dict[sensor_id] == '1':
                sensor_status.append("Connected")
            elif sensor_status_dict[sensor_id] == '0':
                sensor_status.append("Disconnected")

        GlobalVar.set_value("sensor", "Status", sensor_status)
        self.progress.emit("Acquire sensor status success")
        self.progress_int.emit(100)
        self.finished.emit()