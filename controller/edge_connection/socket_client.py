import datetime
import socket
import sys
import time
import os
from PyQt5.QtCore import QMutex, QObject, pyqtSignal
import portalocker
import random
from controller.utility import Utility

from model.global_var import GlobalVar, EventQuene

# a customized header is a 14 bytes array
# first byte - instruction cmd
# second byte: The ID of the file
# third byte - sixth byte: current package number
# seventh byte - tenth byte: the total number of the file packages
# eleventh byte - fourteenth byte: the length of the package
class Header():

    def __init__(self, inputStream=[]):
        assert len(inputStream) == 14
        self.instrCMD = int(inputStream[0])
        self.id = int(inputStream[1])
        self.packageNum = int.from_bytes(inputStream[2:6], byteorder='big')
        self.totalPackageNum = int.from_bytes(inputStream[6:10], byteorder='big')
        self.packageLength = int.from_bytes(inputStream[10:14], byteorder='big')

    def __init__(self, instrCMD, id, packageNum=[], totalPackageNum=[], packageLength=[]):
        assert len(packageNum) == 4 and len(totalPackageNum) == 4 and len(packageLength) == 4
        self.instrCMD = int(instrCMD)
        self.id = int(id)
        self.packageNum = int.from_bytes(packageNum, byteorder='big')
        self.totalPackageNum = int.from_bytes(totalPackageNum, byteorder='big')
        self.packageLength = int.from_bytes(packageLength, byteorder='big')

    def __init__(self, instrCMD):
        self.instrCMD = instrCMD
        self.id = 255
        self.packageNum = 0
        self.totalPackageNum = 0  
        self.packageLength = 0
    
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
        self.path = GlobalVar.get_value("path", "client_temp")

    # connectionList is the name list of ble device for client to send to the server
    # e.g. ["CL880", "CL831", "CL800"]
    def client_requestForConnection(self, connectionList = []):
        assert len(connectionList) != 0
        # create socket
        print("[INFO] Client: Creating a socket...")
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error:
            print("[ERROR] Client: failed to create socket!")
            sys.exit()
        print("[INFO] Client: Socket successfully created.")

        # connect to socket server
        s.connect((self.host, self.port))
        print("[INFO] Client: Connecting to server: " + str(self.host) + " on port: " + str(self.port))
        
        # sending request to server
        # instructionCMD = 1 <- requestForDeviceConnection
        header = Header(1)
        request = header.transToByteArray() + bytes(",".join(connectionList), encoding='utf8')
        print("[INFO] Client: Sending device connection request to server...")

        # sending and receiving
        try:
            s.sendall(request)
            header = Header(list(s.recv(14)))
            if (header.instrCMD == 1):
                # info is the feedback from the server
                # e.g. "CL880,1,CL800,1,CL831,1"
                receivedInfo = s.recv(1024).decode('utf-8')
                receivedInfoDict = self.trans_feedback_to_dict(receivedInfo)
                print(receivedInfoDict)
        except socket.error:
            print(socket.error)
            print("[Error] Client: Send failed.")
            sys.exit()

    
    def client_startRecording(self, time_interval):
        # create socket
        print("[INFO] Client: Creating a socket...")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print("[Error] Client: Failed to create socket!")
            sys.exit()
        print("[INFO] Client: Socket successfully created.")

        # connect to socket server
        s.connect((self.host, self.port))
        print("[INFO] Client: Connecting to server: " + str(self.host) + " on port: " + str(self.port))

        # sending request to server
        # instructionCMD = 2 <- requestForDeviceRecording
        print("[INFO] Client: Sending recording request to server...")
        header = Header(2)
        request = header.transToByteArray + bytes("start recording: ", encoding='utf8')

        try:
            s.sendall(request)
            header = Header(list(s.recv(14)))
            header.printInfo()
            if (header.instrCMD == 2):
                # confirmation from the server
                confirmation = s.recv(1024).decode('utf-8')
                if confirmation != "Confirmed":
                    print("[ERROR] Client: did not receive confirmation from server.")

            s.close()
            print("[INFO] Client: Socket is closed")
            # s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # s2.connect((host, port))

            # receive = s2.recv(1024).decode()

            # if receive[:21] == "recording_in_progress":
            #     print("Hub began to record heart rate data")
            # elif receive == "recording_failed":
            #     print("Recording failed")
        except socket.error:
            print(socket.error)
            print("[Error] Client: Send failed.")
            sys.exit()
        
        if (confirmation == "Confirmed"):
            self.countdown(time_interval)
            self.client_requestForData(time_interval)


    def client_requestForData(self, time_interval):
        # create socket
        print("[INFO] Client: Creating a socket...")
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error:
            print("[ERROR] Client: failed to create socket!")
            sys.exit()
        print("[INFO] Client: Socket successfully created.")

        # connect to socket server
        s.connect((self.host, self.port))
        print("[INFO] Client: Connecting to server: " + str(self.host) + " on port: " + str(self.port))

        # send request to server
        print("[INFO Client: Sending request to server...")
        request = "short: " + str(time_interval)
    
        try:
            s.sendall(bytes(request, encoding='utf8'))
            header = Header(list(s.recv(14)))
            header.printInfo()

            # check the first byte: instruction byte.
            if (self.header_check(header.instrCMD)):
                WholeFileNumber = header.id

                for i in range(WholeFileNumber):
                    fileID = header.id
                    file_package_total = header.totalPackageNum
                    print("[INFO] Client: Prepare for transmission, fileID: " + str(fileID) + ", number of package: " + str(file_package_total) + "\n")
                    for i in range(file_package_total):
                        package_number = header.packageNum
                        package_length = header.packageLength
                        package_content = s.recv(package_length).decode('utf-8')
                        
                        # path = 'C:/Users/Sensor-group/Desktop/temp' + str(WholeFileNumber - fileID + 1) + '.txt'
                        f = open(self.path, 'a+')
                        # lock the file, prevent other process entering the file
                        portalocker.lock(f, portalocker.LOCK_EX)
                        
                        f.write(package_content)
                        f.flush()
                        os.fsync(f.fileno())
                        print("[INFO] Client: Receive package " + str(package_number) + " from server.")
                        header = Header(list(s.recv(14)))
                        f.close()
                        # portalocker.unlock(f)   
                
        except socket.error:
            print("[Error] Client: Send failed: {info}".format(info = socket.error))
            sys.exit()
        s.close()

    def trans_feedback_to_dict(self, receivedInfo):
        receivedInfoList = receivedInfo.split(',')
        assert len(receivedInfoList) % 2 == 0
        keyList = receivedInfoList[::2]
        valueList = receivedInfoList[1::2]
        receivedInfoDict = dict(zip(keyList, valueList))
        return receivedInfoDict

    # check the header send is file, not a request
    def header_check(self, s):
        usf = True
        if (s == b'0xFF'):
            usf = False
        return usf

    def countdown(self, time_left_minute):
        time_left_second = time_left_minute * 60
        while (time_left_second >= 0):
            if (time_left_second % 60 == 0):
                print("[INFO] Client: Count down, " + str(time_left_second//60) + " minutes left.")   
            time.sleep(1)
            time_left_second = time_left_second - 1
            
# if __name__ == '__main__':
#     client = SocketClient('192.168.50.8', 7801)
#     client.client_startRecording(10)
#     client.client_requestForData(10)

class ClientThread(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(str)
    # thread_lock = QMutex()

    def run(self):
        
        # self.thread_lock.lock()
        
        # client_host = GlobalVar.get_value("client", "client_host")
        # client_port = int(GlobalVar.get_value("client", "client_port"))
        # comm_interval = GlobalVar.get_value("client", "request_interval")
    
        try:
            # client = SocketClient(client_host, client_port)
            # client.client_startRecording(comm_interval)
            # client.client_requestForData(comm_interval)
            while True:
                # self.progress.emit(1)
                # self.progress.emit(str(random.randint(0, 100)))
                print("------------------")
                print("ADD...")
                
                # GlobalVar.test_add()
                # EventQuene.add_event(random.randint(0, 5), list)
                
                Utility.generate_event(random.randint(0, 5),
                                       module = str(random.random()),
                                       log_info = str(random.random()))
                
                EventQuene.print_quene()
                print("------------------")
                
                time.sleep(1)
            
        except Exception as exce:
            print("[Error] Client: {info}".format(info = exce))
            
        # self.thread_lock.unlock()
        # self.finished.emit()

            