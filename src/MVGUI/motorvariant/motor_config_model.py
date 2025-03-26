class MotorConfigModel():
    def __init__(self):
        categories = ["Type", "BaseCtrlType", "DriveLabel", "ModuleName", "DriveName", "MotorType"]
        self.values = {}
        self.validCallback = {}
        self.minThreshold = {}
        self.maxThreshold = {}
        for cat in categories:
            self.values[cat] = 0
            self.minThreshold[cat] = 20
            self.maxThreshold[cat] = 100
            self.validCallback[cat] = self.isValidContinous

    def isValid(self, name, value):
        return self.validCallback[name](name, value)
        
    

    def setValue(self, name, value):
        if ((value > self.minThreshold[name]) and (value < self.maxThreshold[name])):
            print(f"Go to Write Uart to set {name} to {value}")
            writeToMcSucceeded = False

        if writeToMcSucceeded:
            self.values[name] = value

    def getValue(self, name):
        return self.values[name]
      
    def isValidContinous(self, name, value):
        min = self.minThreshold[name]
        max = self.maxThreshold[name]
        return (value > min) and (value < max)
    
    def isValidDiscrete(self, name, value):
        return True
