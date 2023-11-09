import os
import datetime
import traceback
import warnings
import pandas as pd
import numpy as np
import struct
from model.global_var import EventQuene, GlobalVar
"""
Author: GRP group 14
"""
class Utility(object):
    """
    * This is the class of useful utility methods 
    """

    @staticmethod
    def get_current_path():
        """
        * The method to return current absolute location in OS
        """
     
        # get the current absolute location
        filepath = os.path.dirname(os.path.realpath('__file__'))
        return filepath
    
    @staticmethod
    def get_current_time(format):
        """
        * The method to return current time
        """
        if format == False:
            current_time = datetime.datetime.now()
            return current_time
        if format == "UTC":
            current_time = datetime.datetime.utcnow()
            return current_time
        
    @staticmethod
    def read_file(filepath):
        """
        * The method to read the file by given path
        """
        if Utility.check_file(filepath):
            try:
                data = pd.read_csv(filepath)
            except Exception as exce:
                print("[ERROR] Utility.read_file: {}".format(exce))
            else:
                return data
        else:
            print("[WARNING] Utility.read_file: The file is empty!")

    @staticmethod
    def check_file(filepath):
        """
        * The method to check path
        """
        return os.path.isfile(filepath)
    
    ### OLD
    @staticmethod
    def check_empty(data, warning_info):
        """
        * The method to check if the data is empty
        """
        if len(data) == 0:
            if warning_info:
                print("[WARNING] The data is empty.")
            return True
        else:
            return False
        
    @staticmethod
    def update_temp_file(data, filepath, overwrite = False):
        
        # if the file exists, add row
        if Utility.check_file(filepath) == True and overwrite == False:
            data.to_csv(filepath, mode = "a", header = None)
        # otherwise, create new file and store
        else:
            data.to_csv(filepath)
            
    @staticmethod
    def tuple_to_list(a_tuple):
        
        a_list = []
        for i in range(len(a_tuple)):
            a_list.append(list(a_tuple[i]))
        return a_list
    
    @staticmethod
    def list_to_df(a_list, data_type):
        
        if data_type == "BP":
            columns = ["Timestamp", "Diastolic", "Systolic", "Device"]
        elif data_type == "BM":
            columns = ["Timestamp", "Weight", "Device"]
        a_df = pd.DataFrame(a_list, columns = columns)
        return a_df
        
    @staticmethod
    def check_input_value(value, type):
        
        from model.global_var import GlobalVar
        
        try:
            value = float(value)
        except Exception as exec:
            print("[Error] {info}.".format(info = exec))
            return "Invalid input!"
        else:
            if value < float(GlobalVar.get_input_limit(type, "min", "value")):
                return GlobalVar.get_input_limit(type, "min", "msg")
            elif value > float(GlobalVar.get_input_limit(type, "max", "value")):
                return GlobalVar.get_input_limit(type, "max", "msg")
            else:
                return "Okay."
        
    @staticmethod
    def calculate_bmi(weight, height):
        
        try:
            bmi = weight / (height * height)
        except:
            err_info = traceback.format_exc()
            print("[ERROR] Invalid input when calculating BMI:")
            print(err_info)
            bmi = 0
        finally:
            print("[INFO]: BIM = " + str(bmi) + ".")
            return bmi
        
    @staticmethod
    def get_timestamp_hex_to_float(time_str):
    
        try:
            timestamp = np.float64(struct.unpack("<d", bytes.fromhex(time_str))[0])
        except:
            err_info = traceback.format_exc()
            print("[ERROR] Cannot unpack the hex data:")
            print(err_info)
        else:
            return timestamp

    @staticmethod
    def float_to_datetime(timestamp_float):
        
        SECOND_IN_A_DAY = 86400   # seconds in a day
        DAYS = 25569              # days between 1970/01/01 and 1900/01/01
        
        timestamp_datetime = datetime.datetime.utcfromtimestamp((timestamp_float - DAYS) * SECOND_IN_A_DAY)
        return timestamp_datetime
    
    @staticmethod
    def text_to_minute(key):
        
        convert_dict = {"10 minutes (default)": 10,
                        "30 seconds": 0.5,
                        "1 minute": 1,
                        "2 minutes": 2,
                        "5 minutes": 5,
                        "10 minutes": 10,
                        "30 minutes": 30,
                        "1 hour": 60,
                        "2 hours": 120,
                        "6 hours": 360,
                        "12 hours": 720,
                        "24 hours": 1440}
        
        try:
            minute_time = convert_dict[key]
        except Exception as err:
            print("[ERROR] {info}".format(info = err))
            print("[INFO] Communication interval has been set to default: 10.")
            return 10
        else:
            print("[INFO] Communication interval has been set to {time}.".format(time = minute_time))
            return minute_time
        
    @staticmethod
    def to_singanl_dec(hex):
  
        width = 16  # 16进制数所占位数
        #******************请输入负数data fxxx**************#
        data = hex
        # data='FFFF'+data
        dec_data = int(data, 16)
        if dec_data > 2 ** (width - 1) - 1:
            dec_data = 2 ** width - dec_data
            dec_data = 0 - dec_data
        return dec_data
    
    @staticmethod
    def generate_event(priority, module = "", log_info = "", print_info = True):
        time = str(datetime.datetime.now())
        type = GlobalVar.get_value("priority", priority)
        event = (time, type, priority, module, log_info)
        GlobalVar.add_log(time, type, priority, module, log_info)
        EventQuene.add_event(priority, event)
        
        if print_info:
            print("[{type}] {module}: {log_info} (Time: {time})".format(type = type, module = module, log_info = log_info, time = time))

        