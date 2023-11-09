import asyncio
import logging
from bleak import BleakClient
from bleak import BleakScanner
from bleak import BleakError
from bleak import _logger as logger
import qasync
import time
import csv
from bleak import discover

"""
Author: GRP group 14
"""

class Xiaomi_scale:

    """
    Set the basic parameters of the scale
    """
    def __init__(self):
        self.CHARACTERISTIC_UUID = "00002a9c-0000-1000-8000-00805f9b34fb"
        self.ADDRESS = "0C:95:41:CB:C6:BD"
        self.SLEEP_TIME = 1.0
        self.TIME_OUT = 10.0
        self.weight = 0
        self.time = ""
        self.stop=False
        loop = asyncio.get_event_loop()
        loop.set_debug(True)
        task = asyncio.ensure_future(self.connect_to_device(self.ADDRESS, debug=True))
        loop.run_until_complete(task)

    """Simple notification handler which prints the data received."""
    def notification_handler(self, sender, data):
        print("---> Notification handler:\t {0}: {1}".format(sender, data))
        if (data[1] & (1<<5)):
            #if (len(data) == 13):
            self.stop = True
            print(self.cau_time())
            self.weight = self.cau_weight(data)
            f = open('controller/weight_data.csv', 'w', encoding='utf-8')
            csv_writer = csv.writer(f)
            csv_writer.writerow([self.weight])
            csv_writer.writerow([self.cau_time()])
            f.close()

    def disconnect_callback(self, client: BleakClient):
        print("xxxxx Client with address {} got disconnected!".format(client.address))

    # deprecated, we no longer need this code
    async def find_device_service(ble_address: str):
        while True:
            try:
                scanner = BleakScanner(scanning_mode='Passive')
                scanner.set_scanning_filter(filters='SignalStrengthFilter')
                device = await scanner.find_device_by_address(ble_address, timeout=5.0)
                if not device:
                    print(f"A device with address {ble_address} could not be found.")
                else:
                    break
            except BleakError as e2:
                print(e2)
            except Exception as e:
                print(e)
            
            print("re-find services\n")
            print("===============\n")

        async with BleakClient(device) as client:
            svcs = await client.get_services()
            print("Services:")
            for service in svcs:
                print(service)

    # code to connect to Xiaomi Scale
    @qasync.asyncSlot()
    async def connect_to_device(self, address: str, debug=True):
        # if debug
        #     import sys
        #     l = logging.getLogger("asyncio")
        #     l.setLevel(logging.DEBUG)
        #     h = logging.StreamHandler(sys.stdout)
        #     h.setLevel(logging.DEBUG)
        #     l.addHandler(h)
        #     logger.addHandler(h)

        while not self.stop:
            print("Waiting connect to sensor....")
            try:
                # disconnected_callback = self.disconnect_callback
                async with BleakClient(address,timeout=60.0) as self.client:
                    # print(client.is_connected)
                    # await client.connect();
                    self.is_connected = await self.client.is_connected()
                    if self.is_connected:
                        print("Connected to Device")

                        await self.client.start_notify(
                            self.CHARACTERISTIC_UUID, self.notification_handler,
                        )
                        if self.stop:
                            self.client.stop_notify(self.CHARACTERISTIC_UUID)

                        while not self.stop:
                            if not self.is_connected:
                                print("Device disconnected!!!")
                                break
                            await asyncio.sleep(self.SLEEP_TIME)
                            print("=========")
                    else:
                        print(f"Failed to connect to Device")
            except Exception as e:
                print(f"Exception when connect: {e}")

            if not self.stop:
                print(f"\n---Reconnect! Sleep {self.SLEEP_TIME} seconds!")
                await asyncio.sleep(self.SLEEP_TIME)

    """
    Calculate the weight data from the scale
    """
    def cau_weight(self,data):
        weight = (((data[12] & 0xFF) << 8) | (data[11] & 0xFF)) / 200.0
        print("weight is "+ str(weight))
        return weight

"""    def cau_time(self):

        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())"""
