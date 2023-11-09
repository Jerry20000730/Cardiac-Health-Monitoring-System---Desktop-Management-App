import numpy as np
import pandas as pd

from controller.utility import Utility
"""
Author: GRP group 14
"""
class SimData(object):
    """ 
    * Simulated data for edge computer software
    ! All data are formatted into DataFrame (pandas library)
    TODO: The data/class should be replaced by real measurement data in the further development
    """
    
    # simulated data for blodd pressure

    data = [68, 156],[65, 112],[72, 150],[70, 153],[61, 157]
    bp_data = pd.read_csv('model/data/example_bp.txt', sep='\t')
    #bp_data = pd.DataFrame(data, columns = ["Diastolic", "Systolic"])

    # simulated data for heart rate
    data = [68, 72, 69, 70, 71, 70, 68, 70, 72, 71, 71, 72, 69, 67, 70, 72, 70, 70, 69, 71, 69, 73, 68, 68, 69, 71, 75, 77, 73, 74, 75]
    hr_data_1 = pd.read_csv('model/data/example_hr.txt', sep='\t')
    #hr_data = hr_data_1["HR/sec (round, de-nan)"]
    hr_data = pd.DataFrame(data, columns = ["HR/sec (round, de-nan)"])

    
    # simulated data for body weight
    data = (["2021-10-01", 52.2, 52.5, 165],
            ["2021-10-02", 51.9, 52.3, 165],
            ["2021-10-03", 51.8, 52.2, 165], 
            ["2021-10-04", 50.8, 52.4, 165],
            ["2021-10-05", 51.6, 52.1, 165],
            ["2021-10-06", 51.5, 52.0, 165],
            ["2021-10-07", 51.4, 52.1, 165],
            ["2021-10-08", 51.2, 51.8, 165],
            ["2021-10-09", 51.0, 51.6, 165],
            ["2021-10-10", 51.0, 51.5, 165],
            ["2021-10-11", 50.9, 91.4, 165],
            ["2021-10-12", 91.0, 51.4, 165],
            ["2021-10-13", 50.9, 51.2, 165],
            ["2021-10-14", 50.7, 51.0, 165],
            ["2021-10-15", 50.5, 51.0, 165],
            ["2021-10-16", 50.6, 51.2, 165],
            ["2021-10-17", 50.3, 50.9, 165],
            ["2021-10-18", 50.4, 51.0, 165],
            ["2021-10-19", 50.5, 50.9, 165],
            ["2021-10-20", 50.2, 50.7, 165],
            ["2021-10-21", 50.1, 50.5, 165])
    bm_data = pd.read_csv('model/data/example_bm.txt', sep='\t')
    #bm_data = pd.DataFrame(data, columns = ["Timestamp", "MIN BM", "MAX BM", "Height"])
    
    # simulated data for heart rate assessment results
    data = (["1911", 0.001784334, 0.015826034, "Hypertensive"],
            ["2289", 0.004447999, 0.026908787, "Hypertensive"],
            ["2033", 0.004035834, 0.027420591, "Hypertensive"],
            ["2307", 0.003009571, 0.015513985, "Hypertensive"],
            ["2100", 0.00679407, 0.022423063, "Hypertensive"],
            ["16265", 0.001576879, 0.014859521, "Normal"],
            ["16273", 0.001496974, 0.014821917, "Normal"],
            ["16795", 0.001752199, 0.0190163, "Normal"],
            ["18177", 0.001698669, 0.021229394, "Normal"],
            ["19830", 0.001542472, 0.018932666, "Normal"],
            ["chf1", 0.012400382, 0.056795177, "Congestive Heart Failure"],
            ["chf2", 0.01383364, 0.060944723, "Congestive Heart Failure"],
            ["chf3", 0.011599982, 0.050799304, "Congestive Heart Failure"],
            ["chf4", 0.005431003, 0.03055907, "Congestive Heart Failure"],
            ["chf5", 0.003466813, 0.018630433, "Congestive Heart Failure"],
            ["2021-10-20", 0.001602472, 0.0185, "Your Assessment"])
    hr_assessment_data = pd.DataFrame(data, columns = ["ID", "STD", "Distance", "Status"])


""" 
* Unused
"""
class BP_Temp(object):
        
    data = [[Utility.get_current_time, 0.0, 0.0]]
    bp_manual_input = pd.DataFrame(data, columns = ["Timestamp", "Diastolic", "Systolic"])
    
    def add_bp(self, data):
        self.bp_manual_data.append(data, ignore_index = True)