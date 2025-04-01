from PyQt5.QtWidgets import QLineEdit, QDoubleSpinBox, QSpinBox
from . import view
from . import model
import yaml

class Controller:
    def __init__(self, terminal):
        self.view = view.View()
        self.model = model.Model()
        self.terminal = terminal

        self.config_data = self.read_config("common_block_config.yaml")
        self.data_types = self.get_datatypes("datatypes.yaml")
        self.categories = self.get_categories(self.config_data)
        self.global_param = self.get_global_param(self.config_data)
        self.commands = self.build_commands()

        self.is_valid = {}
        for key in self.categories:
            self.is_valid[key]= False


        for name in self.categories:
            for key in self.categories[name]:
                if self.config_data[name][key]["Type"] == "char" or self.config_data[name][key]["Type"] == "string":
                    print(name + " " + key)
                    self.view.add_tab_item(name, key, QLineEdit)

                    self.view.input[key].textChanged.connect(lambda _, key=key: self.text_input_changed(key))
                    self.view.setButtons[key].clicked.connect(lambda _, key=key: self.button_pressed_text(key))

                elif self.config_data[name][key]["Type"] == float:
                    print(name + " " + key)
                    self.view.add_tab_item(name, key, QDoubleSpinBox)

                    self.view.input[key].valueChanged.connect(lambda _, key=key: self.number_input_changed(key))
                    self.view.setButtons[key].clicked.connect(lambda _, key=key: self.button_pressed_number(key))

                elif "int" in self.config_data[name][key]["Type"]:
                    print(name + " " + key)
                    self.view.add_tab_item(name, key, QSpinBox)
                    
                    self.view.input[key].valueChanged.connect(lambda _, key=key: self.number_input_changed(key))
                    self.view.setButtons[key].clicked.connect(lambda _, key=key: self.button_pressed_number(key))



                min = self.config_data[name][key]["Range"]["min"]
                if min == "MIN":
                    min = self.data_types[self.config_data[name][key]["Type"]]["min"]
                
                max = self.config_data[name][key]["Range"]["max"]  
                if max == "MAX":
                    max = self.data_types[self.config_data[name][key]["Type"]]["max"]

                if self.config_data[name][key]["ValidCallback"] == "range" or self.config_data[name][key]["ValidCallback"] == "string":
                    self.model.add_data_range(key, min, max, self.config_data[name][key]["ValidCallback"])

                elif self.config_data[name][key]["ValidCallback"] == list:
                    self.model.add_data_range(key, min, max, self.config_data[name][key]["Range"])

            button_all = self.view.inner_views[name]["button_all"]


    def text_input_changed(self, name):
        input_text = self.view.input[name].text()
        is_valid = self.model.is_valid(name, input_text)
        self.view.setButtons[name].setEnabled(is_valid)
        self.is_valid[name] = is_valid
        self.updateAllButton()
    
    def number_input_changed(self, name): 
        input_number = self.view.input[name].value()
        is_valid = self.model.is_valid(name, input_number)
        self.view.setButtons[name].setEnabled(is_valid)
        self.is_valid[name] = is_valid
        self.updateAllButton()

    def button_pressed_text(self, name):
        input_text = self.view.input[name].text()
        succeeded = self.model.set_value(name, input_text)
        command = f"eeset {self.commands[name]} {input_text}"
        self.terminal.send_command(command)
        self.view.setButtons[name].setEnabled(False)

    def button_pressed_number(self, name):
        inputNumber = self.view.input[name].value()
        succeeded = self.model.set_value(name, inputNumber)
        command = f"eeset {self.commands[name]} {inputNumber}"
        self.terminal.send_command(command)
        self.view.setButtons[name].setEnabled(False)

    def updateAllButton(self):
        allEnabled = True
        for key, flag in self.is_valid.items():
            #print(f"{key} {flag}")
            allEnabled = allEnabled and flag
        self.view.buttonAll.setEnabled(allEnabled)

    def read_config(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    def get_categories(self, data):
        cat = {}
        for name in data:
            list = []
            if name == "GlobalName":
                continue
            for key in data[name]:
                list.append(key)
            cat[name] = list
        return cat
    
    def get_global_param(self, data):
        param = data["GlobalName"]
        return param
    
    def build_commands(self):
        com = {}
        for name in self.categories:
            list = []
            for key in self.categories[name]:
                #list.append(self.global_param + "." + key)
                
                com[key] = f"{self.global_param}.{key}" 
        return com
        
    def get_datatypes(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
