import queue

import pandas as pd
"""
Author: GRP group 14
"""
class GlobalVar():
    
    def _init(self):
        
        from controller.utility import Utility
        
        global _global_dict
        global _global_filepath
        global _global_limit
        global _global_repeat_time
        global _global_pic_path
        global _global_text
        global _global_client
        global _global_device
        global _global_sensor
        global _global_mobile
        global _global_iot
        global _global_MD
        global _global_priority
        global _global_event
        global _dict_of_dict
        global _global_logs
        global _global_height
        
        _global_dict = {"BP_display_mode": "new",
                        "monitor_display_mode": "Simulation (Demo)",
                        "hub_auto_connect": False}
        
        _global_repeat_time = 1
        
        _global_filepath = {"logs": "model/data/logs.csv",
                            "bp_temp": "model/data/temp_bp.csv",
                            "bm_temp": "model/data/temp_bm.csv",
                            "bm_trend_new": "model/result/body_mass_trends_new.png",
                            "client_temp": "model/data/client_temp/",
                            "arrhythmia_ecg_sample": "model/result/sample_arrhythmia_ecg_106.png",
                            "short_assessment_sample": "model/result/sample_short_term_assessment_106.png"}
        
        _global_limit = {"diastolic": 
                            {"min": 
                                {"value": 0,
                                "msg": "Diastolic value is too small!"},
                            "max": 
                                {"value": 100,
                                "msg": "Diastolic value is too big!"}},
                        "systolic":
                            {"min":
                                {"value": 40, 
                                "msg": "Systolic value is too small!"},
                            "max":
                                {"value": 250,
                                "msg": "Systolic value is too high!"}}}
        
        _global_pic_path = {"bp_tips_1min": ["view/img/bp_tips/bp_guide_1_1min.png",
                                             "view/img/bp_tips/bp_guide_2.png",
                                             "view/img/bp_tips/bp_guide_3.png",
                                             "view/img/bp_tips/bp_guide_4.png",
                                             "view/img/bp_tips/bp_guide_5.png",
                                             "view/img/bp_tips/bp_guide_6.png",
                                             "view/img/bp_tips/bp_guide_7.png",
                                             "view/img/bp_tips/bp_guide_finish.png"],
                            "bp_tips_5min": ["view/img/bp_tips/bp_guide_1_5min.png",
                                             "view/img/bp_tips/bp_guide_2.png",
                                             "view/img/bp_tips/bp_guide_3.png",
                                             "view/img/bp_tips/bp_guide_4.png",
                                             "view/img/bp_tips/bp_guide_5.png",
                                             "view/img/bp_tips/bp_guide_6.png",
                                             "view/img/bp_tips/bp_guide_7.png",
                                             "view/img/bp_tips/bp_guide_finish.png"]}
        
        _global_text = {"bp_tips_1min": ["Step 1/8: Make sure the air plug is securely inserted in the main unit.",
                                         "Step 2/8: Remove the tight-fitting clothing from your upper left arm.",
                                         "Step 3/8: Sit on a chair with your feet flat on the floor.",
                                         "Step 4/8: Place your left arm on a table so the cuff is level with your heart.",
                                         "Step 5/8: Hold the thumb grip on the cuff securely with your right hand.",
                                         "Step 6/8: Turn the palm of your left hand upward.",
                                         "Step 7/8: Apply the cuff to your upper arm. The air tube runs down the inside of your arm. The bottom of the cuff should be approximately 1/2 inch above your elbow.",
                                         "Step 8/8: Wrap the cuff firmly in place around your arm using the cloth fastener."],
                        "bp_tips_5min": ["Step 1/8: Make sure the air plug is securely inserted in the main unit.",
                                         "Step 2/8: Remove the tight-fitting clothing from your upper left arm.",
                                         "Step 3/8: Sit on a chair with your feet flat on the floor.",
                                         "Step 4/8: Place your left arm on a table so the cuff is level with your heart.",
                                         "Step 5/8: Hold the thumb grip on the cuff securely with your right hand.",
                                         "Step 6/8: Turn the palm of your left hand upward.",
                                         "Step 7/8: Apply the cuff to your upper arm. The air tube runs down the inside of your arm. The bottom of the cuff should be approximately 1/2 inch above your elbow.",
                                         "Step 8/8: Wrap the cuff firmly in place around your arm using the cloth fastener."]}
        
        _global_client = {"client_host": "192.168.50.8",
                          "client_port": 7801,
                          "request_interval": 10}
        
        _global_device = {"ID":     ["CL800-0306604", "CL831-0207764", "CL880-0208027", "HUB001", "MB001", "IoT001", "IoT002", "MD001"],
                          "Name":   ["Chest Strap", "Armband", "Wristband", "Mobile Hub", "Mobile Phone", "Weight Scale", "BP Monitor", "Multi-signals Monitor"],
                          "Status": ["Disconnected", "Disconnected", "Disconnected", "Disconnected", "Disconnected", "Disconnected", "Disconnected", "Disconnected"]}
        
        _global_sensor = {"ID":     ["CL800-0306604", "CL831-0207764", "CL880-0208027"],
                          "Name":   ["Chest Strap", "Armband", "Wristband"],
                          "Status": ["Disconnected", "Disconnected", "Disconnected"]}

        _global_mobile = {"ID":     ["MB001"],
                          "Name":   ["Mobile Phone"],
                          "Status": ["Disconnected"]}
        
        _global_iot = {"ID":    ["IoT001", "IoT002"],
                       "Name":  ["Weight Scale", "BP Monitor"],
                       "Status":["Disconnected", "Disconnected"]}
        
        _global_MD = {"ID":     ["MD001"],
                      "Name":   ["Multi-signals Monitor"],
                      "Status": ["Disconnnected"]} 
        
        _global_priority = {0: "ERROR",
                            1: "WARNING",
                            2: "ADVISORY",
                            3: "WATCH",
                            4: "INFO"}
        
        _global_event = {1400: "Connecting to the mobile hub...",
                         1401: "Connected to the mobile hub!"}
        
        _global_logs = Utility.read_file(_global_filepath["logs"])

        _global_height = {"h": "160"}

        if _global_logs.empty:
            _global_logs = pd.DataFrame([], columns = ["Time", "Type", "Priority", "Module", "Log Information"])
            print("aaa")
        else:
            print(_global_logs)
            print("bbb")
        
        _dict_of_dict = {"dict":        _global_dict,
                         "path":        _global_filepath,
                         "client":      _global_client,
                         "text":        _global_text,
                         "device":      _global_device,
                         "sensor":      _global_sensor,
                         "mobile":      _global_mobile,
                         "iot":         _global_iot,
                         "MD":          _global_MD,         
                         "priority":    _global_priority,
                         "event":       _global_event,
                         "logs":        _global_logs,
                         "height":      _global_height}
        
        
    def add_log(time, type, priotity, module, info):
        new_log = {"Time": time,
                   "Type": type,
                   "Priority": priotity,
                   "Module": module,
                   "Log Information": info}
        _dict_of_dict["logs"] = _dict_of_dict["logs"].append(new_log, ignore_index = True)
        
    def get_input_limit(type, limit, attr):
        try:
            return _global_limit[type][limit][attr]
        except Exception as exc:
            print("[Error] Cannot get the input limit dict: {info}".format(info = exc))
            return 0

    def set_value(dict_name, key, value):
        global _dict_of_dict
        _dict_of_dict[dict_name][key] = value
        print("[INFO] Successfully set the (key) " + str(key) + " to (value) " + str(value) + ".")

    def get_value(dict_name, key):
        try:
            return _dict_of_dict[dict_name][key]
        except Exception as err:
            print("[ERROR] GlobalVar.get_value: Failed to get the global value: {info}".format(info = err))
            
    def clear_logs(self):
        try:
            _dict_of_dict["logs"] = _dict_of_dict["logs"].iloc[0 : 0]
            print(_global_logs)
        except:
            pass
        
    def get_logs(self):
        return _global_logs
            
    def get_list(dict):
        try:
            print(_dict_of_dict[dict])
            return _dict_of_dict[dict]
        except Exception as err:
            print("[ERROR] GlobalVar.get_list: Failed to get the global list: {info}".format(info = err))
            
    def get_path(key):
        try:
            return _dict_of_dict["path"][key]
        except Exception as exce:
            print("[ERROR] GlobalVar.get_path: Failed to get the path: {}.".format(exce))
            
    def get_repeat_time(self):
        global _global_repeat_time
        print("Current time: {time}.".format(time = _global_repeat_time))
        return _global_repeat_time
    
    def increase_repeat_time(self):
        global _global_repeat_time
        _global_repeat_time += 1
        print("Set to be: {time}.".format(time = _global_repeat_time))
        return _global_repeat_time
    
    def reset_repeat_time(self):
        global _global_repeat_time
        _global_repeat_time = 1
        return _global_repeat_time
    
    def get_pic_path(key):
        return _global_pic_path[key]
    
    def get_text(key):
        return _global_text[key]
    
    #####
    # def test_add():
    #     global _test
    #     rand_num = random.randint(0, 100)
    #     _test.append(rand_num)
    #     print("Adding...")
    #     print(_test)
        
    # def test_remove():
    #     global _test
    #     if len(_test) > 0:
    #         _test.pop(0)
    #         print("Removing...")
    #         print(_test)
    #     else:
    #         print("Empty!")
    

class EventQuene():
    
    def _init(self):
        
        global _global_quene
        _global_quene = queue.PriorityQueue()
        
    def add_event(priority, event):
        _global_quene.put((priority, event))
        
    def get_event(self):
        return _global_quene.get()
    
    def print_quene(self):
        print(_global_quene.queue)
        
    def check_empty(self):
        return _global_quene.empty()