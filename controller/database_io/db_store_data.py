from influxdb_client import Point, WritePrecision, WriteOptions, InfluxDBClient
from controller.database_io import db_path as db
"""
Author: GRP group 14
"""

"""
Store the weight data
"""
def store_bm(time, device, value):
    print("[INFO] DB: Starting the storage process...")
    point = Point("Weight") \
        .tag("device", device) \
        .field("value", float(value)) \
        .time(time, WritePrecision.NS)
    db.write_api.write(db.bucket, db.org, point)
    print("[INFO] DB: Weight has been stored.")

"""
Store the blood pressure data
"""
def store_bp(time, device, sys, dias):
    print("[INFO] DB: Starting the storage process...")
    point = Point("BloodPressure") \
        .tag("device", device) \
        .field("diastolic", float(dias)) \
        .field("systolic", float(sys)) \
        .time(time, WritePrecision.NS)
    db.write_api.write(db.bucket, db.org, point)
    print("[INFO] DB: Blood Pressure has been stored.")

"""
Store the heart rate data
"""
def store_hr(time, device, value):
    print("Start the storage.")
    point = Point("HeartRate") \
        .tag("device", device) \
        .field("value", value) \
        .time(time, WritePrecision.NS)
    db.write_api.write(db.bucket, db.org, point)
    print("Heart Rate has been stored.")

"""
Store the heart rate device
"""
def store_hr_df(df):
    with InfluxDBClient(url="http://localhost:8086", token=db.token, org=db.org) as db.client:
        with db.client.write_api(write_options=WriteOptions(batch_size=500,
                                                            flush_interval=10_000,
                                                            jitter_interval=2_000,
                                                            retry_interval=5_000,
                                                            max_retries=5,
                                                            max_retry_delay=30_000,
                                                            exponential_base=2)) as _write_client:
            _write_client.write("Edge Computer Database", db.org, record=df,
                                data_frame_measurement_name='HeartRate', data_frame_tag_columns=['device'])

"""
Store the acc data
"""
def store_acc(time, device, category, x, y, z):
    print("[INFO] DB: Starting the storage process...")
    point1 = Point("ACC") \
        .tag("device", device) \
        .tag("axis", "x") \
        .tag("category", category) \
        .field("value", x) \
        .time(time, WritePrecision.NS)
    point2 = Point("ACC") \
        .tag("device", device) \
        .tag("axis", "y") \
        .tag("category", category) \
        .field("value", y) \
        .time(time, WritePrecision.NS)
    point3 = Point("ACC") \
        .tag("device", device) \
        .tag("axis", "z") \
        .tag("category", category) \
        .field("value", z) \
        .time(time, WritePrecision.NS)
    db.write_api.write(db.bucket, db.org, point1)
    db.write_api.write(db.bucket, db.org, point2)
    db.write_api.write(db.bucket, db.org, point3)
    print("[INFO] DB: Accelerometer has been stored.")

"""
Store the acc device data
"""
def store_acc_df(df):
    with InfluxDBClient(url="http://localhost:8086", token=db.token, org=db.org) as _client:
        with _client.write_api(write_options=WriteOptions(batch_size=500,
                                                          flush_interval=10_000,
                                                          jitter_interval=2_000,
                                                          retry_interval=5_000,
                                                          max_retries=5,
                                                          max_retry_delay=30_000,
                                                          exponential_base=2)) as _write_client:
            """
            Write Pandas DataFrame
            """
            _write_client.write("Edge Computer Database", db.org, record=df, data_frame_measurement_name='ACC',
                                data_frame_tag_columns=['axis', 'category', 'device'])

"""
Store the ppg data
"""
def store_ppg(time, device, category, value):
    print("[INFO] DB: Starting the storage process...")
    point = Point("PPG") \
        .tag("device", device) \
        .tag("category", category) \
        .field("value", value) \
        .time(time, WritePrecision.NS)
    db.write_api.write(db.bucket, db.org, point)
    print("[INFO] DB: PPG has been stored.")

"""
Store the ppg device data
"""
def store_ppg_df(df):
    with InfluxDBClient(url="http://localhost:8086", token=db.token, org=db.org) as _client:
        with _client.write_api(write_options=WriteOptions(batch_size=500,
                                                          flush_interval=10_000,
                                                          jitter_interval=2_000,
                                                          retry_interval=5_000,
                                                          max_retries=5,
                                                          max_retry_delay=30_000,
                                                          exponential_base=2)) as _write_client:
            """
            Write Pandas DataFrame
            """
            _write_client.write("Edge Computer Database", db.org, record=df, data_frame_measurement_name='PPG',
                                data_frame_tag_columns=['device', 'category'])

"""
Store the ecg data
"""
def store_ecg(time, device, first, second, third):
    print("[INFO] DB: Starting the storage process...")
    point1 = Point("ECG") \
        .tag("device", device) \
        .tag("lead", "lead_I") \
        .field("value", float(first)) \
        .time(time, WritePrecision.NS)
    point2 = Point("ECG") \
        .tag("device", device) \
        .tag("lead", "lead_II") \
        .field("value", float(second)) \
        .time(time, WritePrecision.NS)
    point3 = Point("ECG") \
        .tag("device", device) \
        .tag("lead", "lead_III") \
        .field("value", float(third)) \
        .time(time, WritePrecision.NS)
    db.write_api.write(db.bucket, db.org, point1)
    db.write_api.write(db.bucket, db.org, point2)
    db.write_api.write(db.bucket, db.org, point3)
    print("[INFO] DB: ECG has been stored.")

"""
Store the long term data
"""
def store_lt(time, device, type, value):
    print("Start the storage.")
    point = Point("LongTerm") \
        .tag("device", device) \
        .tag("type", type) \
        .field("value", value) \
        .time(time, WritePrecision.NS)
    db.write_api.write(db.bucket, db.org, point)
    print("Long term data has been stored.")

"""
Store the short term data
"""
def store_st(time, device, type, value):
    print("Start the storage.")
    point = Point("ShortTerm") \
        .tag("device", device) \
        .tag("type", type) \
        .field("value", value) \
        .time(time, WritePrecision.NS)
    db.write_api.write(db.bucket, db.org, point)
    print("Short term data has been stored.")

