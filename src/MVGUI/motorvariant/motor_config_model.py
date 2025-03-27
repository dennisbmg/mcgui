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



    def add_data(self, name, data):
        self.categories.append(name)
        if data[name]["ValidCallback"] == "range":
            self.valid_callback[name] = self.is_valid_range
        elif data[name]["ValidCallback"] == "discrete": 
            self.valid_callback[name] = self.is_valid_discrete
        elif data[name]["ValidCallback"] == "string":
            self.valid_callback[name] = self.is_valid_string
        else:
            print(data[name]["ValidCallback"])
            raise NotImplementedError()

  #      if data[name]["Range"]["min"] in "MIN":
  #          self.min_threshold[name] = self.data_types[data]["Type"]["min"]
  #      if data[name]["Range"]["max"] in "MAX":
  #          self.min_threshold[name] = self.data_types[data]["Type"]["max"]
            


        self.min_threshold[name] = 0#int(data[name]["Range"]["min"])
        self.max_threshold[name] = 20#int(data[name]["Range"]["max"])





