from . import motor_variant_tab
from . import motor_config_model


class MotorConfigController():
    def __init__(self, index):
        self.index = index
        categories = ["Type", "BaseCtrlType", "DriveLabel", "ModuleName", "DriveName", "MotorType"]

        self.isValid = {}
        for key in categories:
            self.isValid[key] = True

        self.view = motor_variant_tab.MotorConfigView()
        self.model = motor_config_model.MotorConfigModel()

        for key in categories:
            self.view.input[key].editingFinished.connect(lambda key=key: self.textInputChanged(key))
            self.view.setButtons[key].pressed.connect(lambda key=key: self.buttonPressed(key))

    def textInputChanged(self, name):
        inputNumber = int(self.view.input[name].text())
        isValid = self.model.isValid(name, inputNumber)
        self.view.setButtons[name].setEnabled(isValid)
        self.isValid[name] = isValid
        self.updateAllButton()
       

    def buttonPressed(self, name):
        inputNumber = int(self.view.input[name].text())
        succeeded = self.model.setValue(name, inputNumber)
       
        if not succeeded:
            self.view.input[name].setText(str(self.model.getValue(name)))

    def updateAllButton(self):
        allEnabled = True
        for key, flag in self.isValid.items():
            print(f"{key} {flag}")
            allEnabled = allEnabled and flag

        self.view.buttonAll.setEnabled(allEnabled)
