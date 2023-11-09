from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

"""
Author: GRP group 14
"""

token = "LYz53HePhtZqcHf0jm1t3oqFAAtHhFTxUVZoXQX9B_YJ_RVU1DIn_5OBVFes8BgimjQmqLmqe450u5D7PjdtbQ=="
org = "UNNC"
bucket = "Edge Computer Database"
client = InfluxDBClient(url="http://127.0.0.1:8086", token=token,org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)
