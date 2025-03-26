from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QLineEdit
from PyQt5.Qt import Qt

class CommonBlockTab(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.tabs.resize(300,200)

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        self.noTabs = 0
       

    def register_tab(self, tab):
        self.tabs.addTab(tab, f"Motor Variant {self.noTabs}")
        #count for every tab that gets registered 
        self.noTabs += 1

class CommonBlockView(QWidget):
    def __init__(self):
        super().__init__()

        self.grid = QGridLayout()
        self.grid.setSpacing(100)

        categories = ["Type", "BaseCtrlType", "DriveLabel", "ModuleName", "DriveName", "MotorType"]
        self.labels = {}
        self.input = {}
        self.setButtons = {}

        row = 0
        for cat in categories:
            label = QLabel()
            label.setText(cat)
            self.grid.addWidget(label, row, 0, alignment=Qt.AlignLeft)

            text = QLineEdit()
            self.grid.addWidget(text, row, 1, alignment=Qt.AlignLeft)


            button = QPushButton("Set")
            self.grid.addWidget(button, row, 2, alignment=Qt.AlignLeft)

            
            self.labels[cat] = label
            self.input[cat] = text
            self.setButtons[cat] = button
            row += 1

        self.buttonAll = QPushButton("SetAll")
        self.grid.addWidget(self.buttonAll, row, 2, alignment=Qt.AlignLeft)
        self.setLayout(self.grid)
