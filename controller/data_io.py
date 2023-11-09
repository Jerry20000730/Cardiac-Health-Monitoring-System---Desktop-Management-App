# import package
import traceback
import pandas as pd
import datetime
from model.global_var import GlobalVar
from model.packages import ECGPackage
from model.temp_data import SimData
from controller.plotter import Plotter
from controller.utility import Utility

"""
Author: GRP group 14
"""
class DataIO:
    """
    * This is the class for data input and output methods
    """

    @staticmethod
    def get_new_BP_value(sim_data, device_name, start_time, stop_time):
        """ 
        * The method to get newest blood pressure measurement value in DataFrame
        ! This is static method, don't need to be initialized
        """
        
        if sim_data:

            # initialize the simulated data object
            sim_data = SimData()

            # return the last data point
            return sim_data.bp_data.tail(1)
        
        else:
            
            bp_data = DataIO.get_bp_from_db(device_name, start_time, stop_time)
            return bp_data.tail(1)
        
    @staticmethod
    def get_new_BM_value(sim_data, device_name, start_time, stop_time):
        """
        * The method to get newest weight measurement value in DataFrame
        ! This is static method, don't need to be initialized
                """
        if sim_data:
            # initialize the simulated data object
            sim_data = SimData()

            # return the last data point
            return sim_data.bm_data.tail(1)
        
        else:
            bm_data = DataIO.get_bm_from_db(device_name, start_time, stop_time)
            return bm_data.tail(1)

    @staticmethod
    def refresh_BP_plot_file(result_range):
        """ 
        * The method to refresh the file (picture) of blood pressure plot
        It calls the methods to plot and save new BP figure into the default filepath
        ! This is static method, don't need to be initialized
        """
        # initialize the plotter object
        plt = Plotter()

        # generate new blood pressure figure and save
        plt.generate_BP_plot(result_range, saveto = True)
        
    @staticmethod
    def refresh_BM_plot_file():
        """
        * The method to refresh the file (picture) of weight plot
        It calls the methods to plot and save new BM figure into the default filepath
        ! This is static method, don't need to be initialized
        """
        # initialize the plotter object
        plt = Plotter()

        # generate new blood pressure figure and save
        plt.generate_BM_trends(sim_data = True, goal = 50.5, saveto = True)

    @staticmethod
    def save_bp_temp(diastolic_value, systolic_value):
        """ 
        * Save BP data to temporary cache file
        """

        filepath = GlobalVar.get_path("bp_temp")

        data = [[Utility.get_current_time(False), diastolic_value, systolic_value]]
        data = pd.DataFrame(data, columns = ["Timestamp", "Diastolic", "Systolic"])

        # update 
        Utility.update_temp_file(data, filepath)

    @staticmethod
    def send_bp_to_db(diastolic_value, systolic_value):
        """
        send blood pressure data to database
        """
        # current_time = Utility.get_current_time("UTC")
        current_time = datetime.datetime.utcnow()
        device_name = "Manually Input"

        try:
            
            from controller.database_io.db_store_data import store_bp
            
            store_bp(current_time, device_name, systolic_value, diastolic_value)
            print("[INFO] Successfully sent blood pressure data to the database.")
        except:
            err_info = traceback.format_exc()
            print("[ERROR] Cannot send blood pressure data to the database.")
            print(err_info)

    @staticmethod
    def get_bp_from_db(device_name, start_time, stop_time):
        """
        get blood pressure data from database
        """
        bp_data = []
        
        try:
            
            from controller.database_io.db_query_data import getByDays_bp
            
            bp_data = getByDays_bp(device_name, start_time, stop_time)
            bp_data = Utility.list_to_df(bp_data, "BP")
        except:
            err_info = traceback.format_exc()
            print("[ERROR] Cannot get blood pressure data from the database.")
            print(err_info)
            bp_data = DataIO.get_bp_from_temp()
        else:
            print("[INFO] Successfully got blood pressure data from the database.")
        finally:
            # if Utility.check_empty(bp_data, warning_info = True) == False:
            return bp_data

    @staticmethod
    def get_bp_from_temp():
        """
        get blood pressure data from temp file
        """
        filepath = GlobalVar.get_path("bp_temp")

        try:
            data = pd.read_csv(filepath)
        except:
            err_info = traceback.format_exc()
            print("[ERROR] Cannot read blood pressure data from the temp file.")
            print(err_info)
        else:
            print("[INFO] Successfully read blood pressure data from the temp file.")
            return data

    @staticmethod
    def save_bm_temp(bm_value):
        """ 
        * Save BM data to temporary cache file
        """

        filepath = GlobalVar.get_path("bm_temp")

        data = [[Utility.get_current_time(False), bm_value]]
        data = pd.DataFrame(data, columns=["Timestamp", "Weight"])

        # update 
        Utility.update_temp_file(data, filepath)

    @staticmethod
    def send_bm_to_db(bm_value):
        """
        send weight data to database
        """
        # current_time = Utility.get_current_time("UTC")
        current_time = datetime.datetime.utcnow()
        device_name = "Manually Input"

        try:
            from controller.database_io.db_store_data import store_bm
            
            store_bm(current_time, device_name, bm_value)
            print("[INFO] Successfully sent weight data to the database.")
        except:
            err_info = traceback.format_exc()
            print("[ERROR] Cannot send weight data to the database.")
            print(err_info)

    @staticmethod
    def get_bm_from_db(device_name, start_time, stop_time):
        """
        get weight data from database
        """
        bm_data = []

        try:
            from controller.database_io.db_query_data import getByDays_bm
            
            bm_data = getByDays_bm(device_name, start_time, stop_time)
            bm_data = Utility.list_to_df(bm_data, "BM")

        except:
            err_info = traceback.format_exc()
            print("[ERROR] Cannot get weight data from the database.")
            print(err_info)
            bm_data = DataIO.get_bm_from_temp()
        else:
            print("[INFO] Successfully got weight data from the database.")
        finally:
            # if Utility.check_empty(bm_data, warning_info=True):
            return bm_data

    @staticmethod
    def get_bm_from_temp():

        filepath = GlobalVar.get_path("bm_temp")

        try:
            data = pd.read_csv(filepath)
        except:
            err_info = traceback.format_exc()
            print("[ERROR] Cannot read weight data from the temp file.")
            print(err_info)
        else:
            print("[INFO] Successfully read weight data from the temp file.")
            return data
    
    @staticmethod
    def unpack_ECG_file(filepath, sampling_frequency):
        """
        Unpack the ECG file
        """
        filepath = "model/data/ecg_signal_manually_output_test.ecgd0"

        # Open in binary mode (so you don't read two byte line endings on Windows as one byte)
        # and use with statement (always do this to avoid leaked file descriptors, unflushed files)
        with open(filepath, "rb") as f:
            # Slurp the whole file and efficiently convert it to hex all at once
            hexdata = f.read().hex()
            
        hexlist = map(''.join, zip(*[iter(hexdata)] * 2))

        index = 0
        package_num = 0
        time_str = ""
        package_list = []
        timestamp_list = []
        ecg_sianal_list = []

        HEADER_LENGTH = 12
        TIMESTAMP_LENGTH = 8
        PACKAGE_LENGTH = 512
        HEX = 16

        for ch in hexlist:
            
            if index < TIMESTAMP_LENGTH:
                
                time_str += ch
                
                if index == (TIMESTAMP_LENGTH - 1):
                    timestamp_float = Utility.get_timestamp_hex_to_float(time_str)
                    timestamp_datetime = Utility.float_to_datetime(timestamp_float)
                    package_list.append(ECGPackage(package_num, timestamp_datetime))
                    time_str = ""
                
            if index >= HEADER_LENGTH:
                new_data = int(ch, HEX)
                new_time = timestamp_datetime + datetime.timedelta(seconds = (index - HEADER_LENGTH) / sampling_frequency)
                timestamp_list.append(new_time)
                ecg_sianal_list.append(new_data)
                package_list[package_num].ecg_signal.append(new_data)
                
            index += 1
            
            if index >= PACKAGE_LENGTH:
                index = 0
                package_num += 1
                
        ecg_dataframe = pd.DataFrame({"timestamp": timestamp_list, "ecg_lead_II": ecg_sianal_list})
                
        return [package_list, ecg_dataframe]
    
    @staticmethod
    def hub_data_process(number_of_files):
        """
        process the data comes from the Hub
        """
        processed_data = {"HR": [],
                          "PPG": []}
        
        for i in range(number_of_files):
            f = open("temp" + str(i + 1) + ".txt", "r")
            lines = f.readlines()
            
            for lines in lines:
            
                if "HR" in lines:
                    data_2 = pd.read_csv("temp" + str(i + 1) + ".txt", sep = " ", names = ["Y-M-D", "Time", "0", "1", "2"])
                    AB_HR = pd.DataFrame(data_2, columns = ["Y-M-D", "Time"])
                    AB_HR["Arm_band_HR"] = data_2["2"]
                    AB_HR["Device_type"] = lines.replace("\n","")
                    AB_HR = AB_HR.drop(index = [0])
                    AB_HR["Arm_band_HR"] = AB_HR["Arm_band_HR"].apply(lambda x: int(x,16))
                    
                    # processed_data["HR"].append(AB_HR)
                    # print(AB_HR)
            
                if "PPG" in lines:
                    data = pd.read_csv("temp" + str(i + 1) +".txt", sep = " ", names = ["Y-M-D", "Time", "0", "1", "2",  "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"])
                    #df = pd.DataFrame({"PPG_signal": [data["4"],data["3"] ], "X_Accelerator": [data["10"],data["9"]]})
                    AB_PPG = pd.DataFrame(data, columns = ["Y-M-D", "Time"])
                    AB_PPG["PPG_signal"] = data["4"] + data["3"]
                    AB_PPG["X_Accelerator"] = data["14"] + data["13"]
                    AB_PPG["Y_Accelerator"] = data["10"] + data["9"]
                    AB_PPG["Z_Accelerator"] = data["12"] + data["11"]
                    AB_PPG["Package_ID"] = data["20"]
                    AB_PPG["Device_type"] = lines.replace("\n","")
                    AB_PPG = AB_PPG.drop(index=[0])
                    
                    AB_PPG["PPG_signal"] = AB_PPG["PPG_signal"].apply(lambda x: Utility.to_singanl_dec(x))
                    AB_PPG["X_Accelerator"] = AB_PPG["X_Accelerator"].apply(lambda x: Utility.to_singanl_dec(x))
                    AB_PPG["Y_Accelerator"] = AB_PPG["Y_Accelerator"].apply(lambda x: Utility.to_singanl_dec(x))
                    AB_PPG["Z_Accelerator"] = AB_PPG["Z_Accelerator"].apply(lambda x: Utility.to_singanl_dec(x))
                    
                    # processed_data["PPG"].append(AB_PPG)
                    # print(AB_PPG)
                    
        return processed_data

    @staticmethod
    def clear_logs():
        
        GlobalVar.clear_logs()
        empty_data = pd.DataFrame([], columns = ["Time", "Type", "Priority", "Module", "Log Information"])
        Utility.update_temp_file(empty_data, GlobalVar.get_path("logs"), overwrite = True)
        