import pandas as pd
"""
Author: GRP group 14
"""
class ECGPackage:
    def __init__(self, index, timestamp):
        self.index = index
        self.timestamp = timestamp
        self.name = []
        self.ecg_signal = []
        # self.ecg_signal = pd.DataFrame()

# TEST
# ecg_package = ECGPackage(index = 1, timestamp = 2)
# ecg_package.ecg_signal = ecg_package.ecg_signal.append({"timestamp": 0, "ecg": 1}, ignore_index = True)
# ecg_package.ecg_signal = ecg_package.ecg_signal.append({"timestamp": 1, "ecg2": 1}, ignore_index = True)
# print(ecg_package.ecg_signal)