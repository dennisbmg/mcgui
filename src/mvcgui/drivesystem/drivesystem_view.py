from PyQt5.QtWidgets import QComboBox, QDoubleSpinBox, QSpinBox, QWidget, QTabWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QLineEdit
from PyQt5.Qt import Qt

class DriveSystemTab(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        self.tabs = QTabWidget()

        layout.addWidget(self.tabs)
        self.setLayout(layout)

        self.noTabs = 0
       

    def register_tab(self, tab):
        self.tabs.addTab(tab, f"Drive System {self.noTabs}")
        #count for every tab that gets registered 
        self.noTabs += 1

class DriveSystemView(QWidget):
    def __init__(self):
        super().__init__()

        self.grid = QGridLayout()

        self.labels = {}
        self.input = {}
        self.setButtons = {}
        self.buttonAll = QPushButton("SetAll")
        self.buttonAll.setDisabled(True)
        self.row = 0
        self.grid.addWidget(self.buttonAll, 100, 2)
        self.setLayout(self.grid)

        
        
    def add_item(self, name, input_element):
        column_label = 0
        column_input = 1
        column_button = 2

        label = QLabel()
        label.setText(name)
        self.grid.addWidget(label, self.row, column_label)
        self.labels[name] = label

        input = input_element()
        self.grid.addWidget(input, self.row, column_input)
        self.input[name] = input
#        print(f"DEBUG: Created input widget for {name}: {type(input)}")       

        button = QPushButton("Set")
        button.setDisabled(True)
        self.grid.addWidget(button, self.row, column_button)
        self.setButtons[name] = button

        self.row += 1
