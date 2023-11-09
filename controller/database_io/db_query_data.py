import pandas as pd
from influxdb_client import InfluxDBClient, Dialect
from controller.database_io import db_path as db

"""
Author: GRP group 14
"""

"""
Get weight data from database
"""
def getByDays_bm(device, start, stop):
    query = f'from(bucket: "Edge Computer Database") |> range(start: {start}, stop: {stop})|> filter(fn:(r) => r._measurement == "Weight") |> ' \
            f'filter(fn:(r) => r.device == "{device}")'
    tables = db.client.query_api().query(query, org=db.org)
    data_frame = pd.DataFrame(columns=["time", "value", "device"])
    for table in tables:
        for record in table.records:
            data_frame.loc[len(data_frame.index)] = [record.get_time(), record.get_value(), device]
            # results.append((record.get_time(), record.get_value(), device))
    # print(results)
    return data_frame

"""
Get blood pressure data from database
"""
def getByDays_bp(device, start, stop):
    query1 = f'from(bucket: "Edge Computer Database") |> range(start: {start}, stop: {stop}) |> filter(fn:(r) => r._measurement == ' \
             f'"BloodPressure") |> filter(fn: (r) => r._field == "diastolic") |> filter(fn:(r) => r.device == ' \
             f'"{device}") '
    tables1 = db.client.query_api().query(query1, db.org)
    query2 = f'from(bucket: "Edge Computer Database") |> range(start: {start}, stop: {stop}) |> filter(fn:(r) => r._measurement == ' \
             f'"BloodPressure") |> filter(fn: (r) => r._field == "systolic") |> filter(fn:(r) => r.device == ' \
             f'"{device}") '
    tables2 = db.client.query_api().query(query2, org=db.org)
    data_frame = pd.DataFrame(columns=["time", "diastolic", "systolic", "device"])
    # results = []
    value = 0
    for table in tables1:
        for record in table.records:
            for t in tables2:
                for record2 in t.records:
                    if record2.get_time() == record.get_time():
                        data_frame.loc[len(data_frame.index)] = [record.get_time(), record.get_value(),
                                                                 record2.get_value(), device]
                        # results.append((record.get_time(), record.get_value(), record2.get_value(), device))
                        continue
    return data_frame

"""
Get ecg data from database
"""
def getByDays_ecg(device, lead, start, stop):
    query = f'from(bucket: "Edge Computer Database") |> range(start: {start}, stop: {stop}) |> filter(fn:(r) => r._measurement == ' \
            f'"ECG") |> filter(fn: (r) => r.lead == "{lead}") |> filter(fn:(r) => r.device == ' \
            f'"{device}") '
    tables = db.client.query_api().query(query, org=db.org)

    results = []
    value = 0
    for t1 in tables:
        for record in t1.records:
            if record.get_time() == record.get_time():
                results.append((record.get_time(), record.get_value(), lead, device))
            continue
    return results

"""
Get ppg data from database
"""
def getByDays_ppg(device, category, start, stop):
    query = f'from(bucket:"Edge Computer Database") |> range(start: {start}, stop: {stop}) |> filter(fn:(r) => r._measurement == ' \
            f'"PPG") |> filter(fn:(r) => r.category == "{category}") |> filter(fn: (r) => r._field == "value") |> filter(fn:(r) => r.device == ' \
            f'"{device}") '
    tables = db.client.query_api().query(query, org=db.org)
    results = []
    for table in tables:
        for record in table.records:
            results.append((record.get_time(), record.get_value(), category, device))
            continue
    return results

"""
Get acc data from database
"""
def getByDays_acc(device, category, passage, start, stop):
    query = f'from(bucket: "Edge Computer Database") |> range(start: {start}, stop: {stop}) |> filter(fn:(r) => r._measurement == ' \
            f'"Accelerometer") |> filter(fn: (r) => r.passage == "{passage}") |> filter(fn:(r) => r.device == ' \
            f'"{device}") |> filter(fn:(r) => r.category == "{category}") |> filter(fn: (r) => r._field == "value")'
    tables = db.client.query_api().query(query, org=db.org)

    results = []
    for table in tables:
        for record in table.records:
            results.append((record.get_time(), record.get_value(), passage, category, device))
            continue
    return results

"""
Get the type of device of heart rate from database
"""
def getByDays_hr_device(device, start, stop):
    query = f'from(bucket:"Edge Computer Database") |> range(start: {start}, stop:{stop}) |> filter(fn:(r) => ' \
            f'r._measurement == "HeartRate") |> filter(fn:(r) => r.device == "{device}")|> pivot(rowKey:["_time"], ' \
            f'columnKey: ["_field"], valueColumn: "_value") |> keep(columns: ["_time","device", "value"])'

    data_frame = db.client.query_api().query_data_frame(query)
    print(data_frame.to_string())
    return data_frame

"""
Get heart rate data from database
"""
def getByDays_hr(start, stop):
    query = f'from(bucket:"Edge Computer Database") |> range(start: {start}, stop:{stop}) |> filter(fn:(r) => ' \
            f'r._measurement == "HeartRate") |> pivot(rowKey:["_time"], ' \
            f'columnKey: ["_field"], valueColumn: "_value") |> keep(columns: ["_time","device", "value"])'

    data_frame = db.client.query_api().query_data_frame(query)
    # print(data_frame.to_string())
    return data_frame

"""
Get average heart rate data of every minute from database
"""
def get_mean_hr(start, stop, period):
    query = f'from(bucket:"Edge Computer Database") |> range(start: {start}, stop: {stop}) |> filter(fn:(r) => ' \
            f'r._measurement == "HeartRate")|> aggregateWindow(every: {period}, fn: mean, createEmpty: false)|> pivot(rowKey:["_time"], ' \
            f'columnKey: ["_field"], valueColumn: "_value") |> keep(columns: ["_time","device", "value"])'

    data_frame = db.client.query_api().query_data_frame(query)
    # print(data_frame)
    return data_frame

"""
Get specified type data from database
"""
def get_specified_value(start, stop, period, type, table):
    query = f'from(bucket:"Edge Computer Database") |> range(start: {start}, stop: {stop}) |> filter(fn:(r) => ' \
            f'r._measurement == "{table}")|> aggregateWindow(every: {period}, fn: {type}, createEmpty: false)|> pivot(rowKey:["_time"], ' \
            f'columnKey: ["_field"], valueColumn: "_value") |> keep(columns: ["_time","device", "value"])'

    data_frame = db.client.query_api().query_data_frame(query)
    # print(data_frame)
    return data_frame

"""
Get specified type data from database
"""
def get_specified_value_pro(start, stop, period, type, table, additional_field):
    query = f'from(bucket:"Edge Computer Database") |> range(start: {start}, stop: {stop}) |> filter(fn:(r) => ' \
            f'r._measurement == "{table}") |> filter(fn: (r) => r["_field"] == "{additional_field}")|> ' \
            f'aggregateWindow(every: {period}, fn: {type}, createEmpty: false)|> pivot(rowKey:["_time"], ' \
            f'columnKey: ["_field"], valueColumn: "_value") |> keep(columns: ["_time","device", "{additional_field}"])'

    data_frame = db.client.query_api().query_data_frame(query)
    # print(data_frame)
    return data_frame


if __name__ == '__main__':
    a = get_mean_hr("2022-03-08T21:05:00.000Z", "2022-03-08T22:05:00.000Z", "10m", "max")
    print("----")
    print(a)
