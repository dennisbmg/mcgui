from PyQt5.QtWidgets import QComboBox, QDoubleSpinBox, QSpinBox, QWidget, QTabWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QLineEdit
from PyQt5.Qt import Qt

class PiezoVariantTab(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.tabs.resize(300,200)

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        self.noTabs = 0
       

    def register_tab(self, tab):
        self.tabs.addTab(tab, f"Piezo Variant {self.noTabs}")
        #count for every tab that gets registered 
        self.noTabs += 1

class PiezoVariantView(QWidget):
    def __init__(self):
        super().__init__()

        self.grid = QGridLayout()
        self.grid.setSpacing(100)

        self.labels = {}
        self.input = {}
        self.setButtons = {}
        self.buttonAll = QPushButton("SetAll")
        self.buttonAll.setDisabled(True)
        self.grid.addWidget(self.buttonAll,5, 2, alignment=Qt.AlignLeft)
        self.setLayout(self.grid)

        self.row = 0
        
        
    def add_item(self, name, input_element):
        column_label = 0
        column_input = 1
        column_button = 2
        label = QLabel()
        label.setText(name)
        self.grid.addWidget(label, self.row, column_label, alignment=Qt.AlignCenter)
        self.labels[name] = label

        input = input_element()
        label.setText(name)
        self.grid.addWidget(input, self.row, column_input, alignment=Qt.AlignCenter)
        self.input[name] = input
#        print(f"DEBUG: Created input widget for {name}: {type(input)}")       

        button = QPushButton("Set")
        button.setDisabled(True)
        label.setText(name)
        self.grid.addWidget(button, self.row, column_button, alignment=Qt.AlignCenter)
        self.setButtons[name] = button

        self.row += 1

