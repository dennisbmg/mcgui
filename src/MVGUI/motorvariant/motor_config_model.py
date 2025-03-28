class MotorConfigModel():

    def __init__(self):
        self.categories = []
        self.values = {}
        self.valid_callback = {}
        self.min_threshold = {}
        self.max_threshold = {}
        self.data_types = {}

    def is_valid(self, name, value):
        return self.valid_callback[name](name, value)
        
    

    def set_value(self, name, value):
        if ((value > self.min_threshold[name]) and (value < self.max_threshold[name])):
            print(f"Go to Write Uart to set {name} to {value}")
            writeToMcSucceeded = True
        else:
            writeToMcSucceeded = False
            

        if writeToMcSucceeded:
            self.values[name] = value

    def get_value(self, name):
        return self.values[name]
      
    def is_valid_range(self, name, value):
        min = self.min_threshold[name]
        max = self.max_threshold[name]
        return (value >= min) and (value <= max)
    
    def is_valid_discrete(self, name, value):
        return True
    
    def is_valid_string(self, name, value):
        try:
            if len(value) <= 20:
                return True
        except TypeError:
            return False
        except Exception as e:
            return False 



    def add_data(self, name, min, max, callback):
        self.min_threshold[name] = min
        self.max_threshold[name] = max
        if callback == "range":
            self.valid_callback[name] = self.is_valid_range

        elif callback == "string":
            self.valid_callback[name] = self.is_valid_string

        elif callback == "discrete":
            self.valid_callback[name] = self.is_valid_discrete











