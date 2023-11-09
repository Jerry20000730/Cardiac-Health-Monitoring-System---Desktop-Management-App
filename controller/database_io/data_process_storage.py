import random
import pandas as pd
from controller.database_io import db_store_data as store, db_store_data
from controller.database_io import db_delete_data
from datetime import datetime
import os

"""
Author: GRP group 14
"""

local_path = "..\\..\\model\\data_dir"

"""
Change the Hex number to dec number
"""
def toSinganl_Dec(Hex):
    width = 16
    data = Hex
    dec_data = int(data, 16)
    if dec_data > 2 ** (width - 1) - 1:
        dec_data = 2 ** width - dec_data
        dec_data = 0 - dec_data
    return dec_data

"""
Process the raw data and store it into the database
"""
def data_process():
    time_stamp_process_start = datetime.now().strftime("%H:%M:%S")
    print(time_stamp_process_start + "    [INFO] process and storage begin")
    dir_name = os.listdir(local_path)
    if len(dir_name) == 0:
        return
    for dir_names in dir_name:
        file_path = local_path + "\\" + dir_names
        print(dir_names)
        file_names = os.listdir(file_path)

        for file_name in file_names:
            final_path = file_path + "\\" + file_name
            # for i in range(number):
            # open raw data txt file
            with open(final_path, 'r') as f:

                time_stamp_file = datetime.now().strftime("%H:%M:%S")
                print(time_stamp_file + "    [INFO] read in " + final_path)

                # read the first line to acquire the model name
                model_id = file_name.rstrip(".txt")
                model_id = model_id.replace("_","-")

                if "CL831" in model_id or "CL880" in model_id:
                    if "HR" in model_id:
                        # acquire data in temp txt
                        data = pd.read_csv(f, sep=' ', dtype=str, names=['Y-M-D', 'Time', '0', '1', '2'])

                        data = data.dropna(axis=0, how='any',subset=['2'])
                        # create time stamp for start processing
                        time_stamp_start_process_hr = datetime.now().strftime("%H:%M:%S")
                        print(
                            time_stamp_start_process_hr + "    [INFO] start processing heart rate data for " + model_id[
                                                                                                               :5])

                        # write HR data in dataframe
                        AB_HR = hr_processing(data, model_id)

                        # create time stamp for finishing
                        time_stamp_stop_process_hr = datetime.now().strftime("%H:%M:%S")
                        print(
                            time_stamp_stop_process_hr + "    [INFO] finish processing heart rate data for " + model_id[
                                                                                                               :5] + ", start storing heart rate data.")

                        # start storing hr_report data in database
                        print(AB_HR)
                        store.store_hr_df(AB_HR)
                        time_stamp_stop_storing_hr = datetime.now().strftime("%H:%M:%S")
                        print(time_stamp_stop_storing_hr + "    [INFO] finish storing heart rate data for " + model_id[
                                                                                                              :5])

                    elif "PPG" in model_id:
                        data = pd.read_csv(f, sep=' ', dtype=str,
                                           names=['Y-M-D', 'Time', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                                  '10',
                                                  '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'])
                        print(data)
                        data = data.dropna(axis=0, how='any',subset=['3', '4'])
                        print(data)
                        # write PPG data in dataframe

                        ABP = CL831_880_ppg_processing(data, model_id)
                        time_stamp_process_ppg = datetime.now().strftime("%H:%M:%S")
                        print(time_stamp_process_ppg + "    [INFO] finish processing ppg data for " + model_id[:5])

                        # write ACC data in dataframe
                        ABA = CL831_880_acc_processing(data, model_id)
                        time_stamp_process_x = datetime.now().strftime("%H:%M:%S")
                        print(
                            time_stamp_process_x + "    [INFO] finish processing xyz accelerameter data for " + model_id[
                                                                                                                :5] + ", start storing ppg data.")

                        # call database API
                        print(ABP)
                        store.store_ppg_df(ABP)
                        time_stamp_ppg = datetime.now().strftime("%H:%M:%S")
                        print(time_stamp_ppg + "    [INFO] stored ppg for" + model_id[
                                                                             :5] + ", start storing accelerameter.")

                        # store xyz accelerameter
                        store.store_acc_df(ABA)
                        time_stamp_xyz = datetime.now().strftime("%H:%M:%S")
                        print(time_stamp_xyz + "    [INFO] finish storing xyz accelerameter for " + model_id[:5])

                elif "CL800" in model_id:
                    if "HR" in model_id:
                        # acquire data in temp txt
                        data = pd.read_csv(f, sep=' ', dtype=str,
                                           names=['Y-M-D', 'Time', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
                        data = data.dropna(axis=0, how='any',subset=['2'])
                        # write HR data in dataframe
                        AB_HR = hr_processing(data, model_id)

                        time_stamp_hr = datetime.now().strftime("%H:%M:%S")
                        print(time_stamp_hr + "    [INFO] stored heart rate data for " + model_id[:5])

                        # call database API
                        store.store_hr_df(AB_HR)
                        print(AB_HR)
                        time_stamp_hr = datetime.now().strftime("%H:%M:%S")
                        print(time_stamp_hr + "    [INFO] stored heart rate data for " + model_id[:5])

                    elif "ACC" in model_id:
                        # acquire data in temp txt
                        data = pd.read_csv(f, sep=' ', dtype=str,
                                           names=['Y-M-D', 'Time', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                                  '10',
                                                  '11', '12', '13', '14', '15', '16', '17', '18', '19',
                                                  '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
                                                  '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
                                                  '41', '42', '43', '44', '45',
                                                  '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56',
                                                  '57', '58', '59', '60', '61',
                                                  '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72',
                                                  '73', '74', '75', '76', '77',
                                                  '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88',
                                                  '89', '90', '91', '92', '93',
                                                  '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104',
                                                  '105', '106', '107', '108',
                                                  '109', '110', '111', '112', '113', '114', '115', '116', '117', '118',
                                                  '119', '120', '121', '122',
                                                  '123', '124', '125', '126', '127', '128', '129', '130', '131', '132',
                                                  '133', '134', '135', '136'])

                        # process the xyz data
                        ABA = CL800_acc_processing(data, model_id)
                        time_stamp_process_acc = datetime.now().strftime("%H:%M:%S")
                        print(time_stamp_process_acc + "    [INFO] finish processing xyz accelerameter for " + model_id[
                                                                                                               :5] + ", start storing xyz acclerameter.")

                        # storing xyz data
                        store.store_acc_df(ABA)
                        time_stamp_process_acc = datetime.now().strftime("%H:%M:%S")
                        print(
                            time_stamp_process_acc + "    [INFO] finish storing xyz accelerameter for " + model_id[:5])

                        time_stamp_process_all = datetime.now().strftime("%H:%M:%S")
                        print(time_stamp_process_all + "    [INFO] process and storage complete!")



def hr_processing(data, lines):
    '''
        time: use to store time stamp temporarily
        value: Heart Rate
        device: device name
    '''

    # create a new dataframe, index: time stamp, column: hr_report-value, device-name
    AB_HR = pd.DataFrame(index=pd.to_datetime(data['Y-M-D'] + " " + data['Time'], format='%Y-%m-%d %H:%M:%S:%f'),
                         columns=['value', 'device'])

    # copy the data for hr_report-value
    AB_HR['value'] = (data['2'].apply(lambda x: int(x, 16)).astype(object)).values
    AB_HR['value'] = AB_HR['value'].astype(float)

    # copy the data for device value
    AB_HR['device'] = lines.replace("\n", "").rstrip("-HR")

    return AB_HR


def CL831_880_ppg_processing(data, lines):
    '''
        time: use to store time stamp temporarily
        value: ppg signal
        device: device name
        category: show where does the data come from (usually measurement)
    '''

    # create a new dataframe, index: time stamp, column: hr_report-value, device-name
    AB_PPG = pd.DataFrame(index=pd.to_datetime(data['Y-M-D'] + " " + data['Time'], format='%Y-%m-%d %H:%M:%S:%f'),
                          columns=['value', 'device', 'category'])

    # Calculate PPG signal
    value_temp = (data['4'] + data['3']).apply(lambda x: toSinganl_Dec(x)).astype(object)

    # copy data for ppg value
    AB_PPG['value'] = value_temp.values
    AB_PPG['value'] = AB_PPG['value'].astype(float)
    # write in data for category
    AB_PPG['category'] = "measurement"
    # write in data for device
    AB_PPG["device"] = lines.replace("\n", "").rstrip("-PPG")

    return AB_PPG


def CL831_880_acc_processing(data, lines):
    '''
        time: use to store time stamp temporarily
        value: axis value
        axis: Axis name
        device: device name
        category: show where does the data come from (usually measurement)
    '''
    # create three new dataframes, index: time stamp, column: axis, acc-value, device-name, category
    ABA_x = pd.DataFrame(index=pd.to_datetime(data['Y-M-D'] + " " + data['Time'], format='%Y-%m-%d %H:%M:%S:%f'),
                         columns=['axis', 'value', 'device', 'category'])
    ABA_y = pd.DataFrame(index=pd.to_datetime(data['Y-M-D'] + " " + data['Time'], format='%Y-%m-%d %H:%M:%S:%f'),
                         columns=['axis', 'value', 'device', 'category'])
    ABA_z = pd.DataFrame(index=pd.to_datetime(data['Y-M-D'] + " " + data['Time'], format='%Y-%m-%d %H:%M:%S:%f'),
                         columns=['axis', 'value', 'device', 'category'])

    # copy the category data
    ABA_x['category'] = ABA_y['category'] = ABA_z['category'] = "measurement"

    # copy axis data
    ABA_x['axis'] = "x"
    ABA_y['axis'] = "y"
    ABA_z['axis'] = "z"

    # copy device data
    ABA_x['device'] = ABA_y['device'] = ABA_z['device'] = lines.replace("\n", "").rstrip("-PPG")

    # calculate acc signal and copy data to designated dataframe
    ABA_x['value'] = ((data['10'] + data['9']).apply(lambda x: toSinganl_Dec(x)).astype(object)).values
    ABA_y['value'] = ((data['12'] + data['11']).apply(lambda x: toSinganl_Dec(x)).astype(object)).values
    ABA_z['value'] = ((data['14'] + data['13']).apply(lambda x: toSinganl_Dec(x)).astype(object)).values

    ABA_x['value'] = ABA_x['value'].astype(float)
    ABA_y['value'] = ABA_y['value'].astype(float)
    ABA_z['value'] = ABA_z['value'].astype(float)

    result = [ABA_x, ABA_y, ABA_z]

    return pd.concat(result)


def CL800_acc_processing(data, lines):
    '''
        time: use to store time stamp temporarily
        value: axis value
        axis: Axis name
        device: device name
        category: show where does the data come from (usually measurement)
    '''
    # only select the line with the "2" index contains "28"
    data = data.loc[data["2"] == "28"]

    # final result concat
    result = []
    column_index = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                    '11', '12', '13', '14', '15', '16', '17', '18', '19',
                    '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
                    '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40']

    # six accelerameter
    for i in range(1, 7):
        # create three new dataframe
        ABA_x = pd.DataFrame(index=pd.to_datetime(data['Y-M-D'] + " " + data['Time'], format='%Y-%m-%d %H:%M:%S:%f'),
                             columns=['axis', 'value', 'device', 'category'])
        ABA_y = pd.DataFrame(index=pd.to_datetime(data['Y-M-D'] + " " + data['Time'], format='%Y-%m-%d %H:%M:%S:%f'),
                             columns=['axis', 'value', 'device', 'category'])
        ABA_z = pd.DataFrame(index=pd.to_datetime(data['Y-M-D'] + " " + data['Time'], format='%Y-%m-%d %H:%M:%S:%f'),
                             columns=['axis', 'value', 'device', 'category'])

        # copy category
        ABA_x['category'] = ABA_y['category'] = ABA_z['category'] = "measurement"

        # copy axis data
        ABA_x['axis'] = "x" + str(i)
        ABA_y['axis'] = "y" + str(i)
        ABA_z['axis'] = "z" + str(i)

        # copy device data
        ABA_x['device'] = ABA_y['device'] = ABA_z['device'] = lines.replace("\n", "").rstrip("-ACC")

        # calculate accelerator value
        ABA_x['value'] = ((data[column_index[3 + (i - 1) * 6]] + data[column_index[2 + (i - 1) * 6]]).apply(
            lambda x: toSinganl_Dec(x)).astype(object)).values
        ABA_y['value'] = ((data[column_index[5 + (i - 1) * 6]] + data[column_index[4 + (i - 1) * 6]]).apply(
            lambda x: toSinganl_Dec(x)).astype(object)).values
        ABA_z['value'] = (
            (data[column_index[7 + (i - 1) * 6]] + data[column_index[i * 6]]).apply(lambda x: toSinganl_Dec(x)).astype(
                object)).values

        ABA_x['value'] = ABA_x['value'].astype(float)
        ABA_y['value'] = ABA_y['value'].astype(float)
        ABA_z['value'] = ABA_z['value'].astype(float)

        result.extend([ABA_x, ABA_y, ABA_z])

    return pd.concat(result)


# temporarily ignore
if __name__ == '__main__':
    # start = '2021-07-01T06:01:06.000Z'
    # stop = '2022-03-23T07:00:00.000Z'
    # db_delete_data.DeleteByDays("BloodPressure", start, stop)
    # db_delete_data.DeleteByDays("Weight", start, stop)
    for i in range(5,9):
        db_store_data.store_bm("2022-03-2"+str(i)+"T06:02:06.000Z","Manually Input", random.randint(55, 60))
        db_store_data.store_bp("2022-03-2"+str(i)+"T06:02:06.000Z","Manually Input", random.randint(110, 130),random.randint(90, 100))
    # db_delete_data.DeleteByDays("BloodPressure", start, stop)
    # db_delete_data.DeleteByDays("Weight", start, stop)
    # db_delete_data.DeleteByDays("ACC", start, stop)
    # db_delete_data.DeleteByDays(start, stop)
    # db_delete_data.DeleteByDays(start, stop)
    # db_delete_data.DeleteByDays(start, stop)
    # str = "CL800-0306605-HR"
    # print(str.strip("-HR"))

    # data_process()
    # print("FINAL: "+"time:{:.5f}s".format(perf_counter()))
