from PyQt5.QtWidgets import QDoubleSpinBox, QLineEdit, QPushButton, QLabel, QSpinBox
from . import commonblock_tab
from . import commonblock_model
import yaml


class CommonBlockController():
    def __init__(self, index, terminal):
        self.index = index
        self.terminal = terminal

        self.config_data = self.read_config("common_block_config.yaml")
        self.data_types = self.get_datatypes("datatypes.yaml")
        self.global_param = self.get_global_param(self.config_data)
        self.categories = self.get_categories(self.config_data)
        self.commands = self.build_commands()

        self.is_valid = {}
        for key in self.categories:
            self.is_valid[key] = False

        self.view = commonblock_tab.CommonBlockView() 
        self.model = commonblock_model.CommonBlockModel()
        
#        for key in self.categories:
##            if self.config_data[key]["Type"] == "char":
#                self.view.add_item(key, QLineEdit)
#
#                # had a problem with callbacks not returning the expected key 
#                # assining key to value first is a workaround to get the expected key
#                self.view.input[key].textChanged.connect(lambda value=key, key=key: self.text_input_changed(key))
#                self.view.setButtons[key].clicked.connect(lambda value=key, key=key: self.button_pressed_text(key))
#            elif self.config_data[key]["Type"] == "string":
#                self.view.add_item(key, QLineEdit)
#
#                self.view.input[key].textChanged.connect(lambda value=key, key=key: self.text_input_changed(key))
#                self.view.setButtons[key].clicked.connect(lambda value=key, key=key: self.button_pressed_text(key))
#            elif self.config_data[key]["Type"] == "float":
#                self.view.add_item(key, QDoubleSpinBox)
#
#                self.view.input[key].valueChanged.connect(lambda value=key, key=key: self.number_input_changed(key))
#                self.view.setButtons[key].clicked.connect(lambda value=key, key=key: self.button_pressed_text(key))
#            elif "int" in self.config_data[key]["Type"]:
#                self.view.add_item(key, QSpinBox)
#
#                self.view.input[key].valueChanged.connect(lambda value=key, key=key: self.number_input_changed(key))
#                self.view.setButtons[key].clicked.connect(lambda value=key, key=key: self.button_pressed_number(key))
#
#            min = self.config_data[key]["Range"]["min"]
#            if min == "MIN":
#                min = self.data_types[self.config_data[key]["Type"]]["min"]
#            
#            max = self.config_data[key]["Range"]["max"]  
#            if max == "MAX":
#                max = self.config_data[key]["Range"]["max"]  
#
#            if self.config_data[key]["ValidCallback"] == "range" or self.config_data[key]["ValidCallback"] == "string":
#                self.model.add_data_range(key, min, max, self.config_data[key]["ValidCallback"])
#
#            elif self.config_data[key]["ValidCallback"] == list:
#                self.model.add_data_range(key, min, max, self.config_data[key]["Range"])
#

#            print(f"Key: {key} min: {min} max: {max} callback: {self.config_data[key]['ValidCallback']}")
            


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
        command =f"eeset {self.commands[name]} {inputNumber}"
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
        cat = []
        for key in data:
            if key == "GlobalName":
                continue
            cat.append(key)
        return cat
            
    def get_global_param(self, data):
        param = data["GlobalName"]
        x = param.replace("<index>", str(self.index))
        return x
    
    def build_commands(self):
        com = {}
        for key in self.categories:
            com[key] = self.global_param + "." + key
        return com
        
    def get_datatypes(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
