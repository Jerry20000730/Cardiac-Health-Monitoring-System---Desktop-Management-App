
class Counter(object):
    global bar_counter
    global process_counter
    bar_counter = 1
    process_counter = 0
    def init_bar_counter(self,file_number):
        global bar_counter
        bar_counter = 100/(file_number*3*6)

    def get_counter(self):
        return bar_counter

    def add_process_counter(self):
        global process_counter
        process_counter = process_counter + bar_counter

    def get_process_counter(self):
        return process_counter