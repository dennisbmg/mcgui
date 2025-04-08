from PyQt5.QtWidgets import QComboBox, QDoubleSpinBox, QSpinBox, QWidget, QTabWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QLineEdit

class MotorVariantTab(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        self.tabs = QTabWidget()

        layout.addWidget(self.tabs)
        self.setLayout(layout)

        self.noTabs = 0
       

    def register_tab(self, tab):
        self.tabs.addTab(tab, f"Motor Variant {self.noTabs}")
        #count for every tab that gets registered 
        self.noTabs += 1

class MotorConfigView(QWidget):
    def __init__(self):
        super().__init__()

        self.grid = QGridLayout()

        self.labels = {}
        self.input = {}
        self.setButtons = {}
        self.buttonAll = QPushButton("SetAll")
        self.buttonAll.setDisabled(True)
        self.grid.addWidget(self.buttonAll,5, 2)
        self.setLayout(self.grid)

        self.row = 0
        
        
    def add_item(self, name, input_element):
        column_label = 0
        column_input = 1
        column_button = 2

        label = QLabel(name)
        self.grid.addWidget(label, self.row, column_label)
        self.labels[name] = label
        

        if input_element == QSpinBox or input_element == QDoubleSpinBox:
            print(f"im in if thats the input_element: {input_element}")
            input = input_element()
            input.setMaximum(10000)
        else:
            input = input_element()

        self.grid.addWidget(input, self.row, column_input)
        self.input[name] = input

        button = QPushButton("Set")
        button.setDisabled(True)
        self.grid.addWidget(button, self.row, column_button)
        self.setButtons[name] = button

        self.row += 1
