from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QComboBox, QTextEdit
from PyQt5.Qt import Qt
from terminal import Terminal

class CommandView(QWidget):
    def __init__(self):
        super().__init__()
        self.grid = QGridLayout()
#        self.terminal = Terminal()
        self.combobox_items = ["-","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        self.lbl_eeprom_read = QLabel("EEPROM READ", self)
        self.grid.addWidget(self.lbl_eeprom_read, 0, 0, alignment=Qt.AlignCenter)
        self.btn_read_param = QPushButton("Read Parameter", self)
        self.grid.addWidget(self.btn_read_param, 1, 0, alignment=Qt.AlignCenter)
        self.btn_read_memory = QPushButton("Read Memory", self)
        self.grid.addWidget(self.btn_read_memory, 2, 0, alignment=Qt.AlignCenter)

        self.lbl_eeprom_load = QLabel("EEPROM LOAD", self)
        self.grid.addWidget(self.lbl_eeprom_load, 0, 1, alignment=Qt.AlignCenter)
        self.cmb_load_param = QComboBox()
        self.cmb_load_param.addItems(self.combobox_items)
        self.grid.addWidget(self.cmb_load_param, 1, 1, alignment=Qt.AlignCenter)
        self.btn_load_default = QPushButton("Load Default", self)
        self.grid.addWidget(self.btn_load_default, 2, 1, alignment=Qt.AlignCenter)

        self.lbl_eeprom_erase = QLabel("EEPROM ERASE", self)
        self.grid.addWidget(self.lbl_eeprom_erase, 0, 2, alignment=Qt.AlignCenter)
        self.btn_erase_param = QPushButton("Erase Parameter", self)
        self.grid.addWidget(self.btn_erase_param, 1, 2, alignment=Qt.AlignCenter)
        self.btn_erase_logdata = QPushButton("Erase Logdata", self)
        self.grid.addWidget(self.btn_erase_logdata, 2, 2, alignment=Qt.AlignCenter)

        self.box_eeprom_output = QTextEdit()
        self.grid.addWidget(self.box_eeprom_output, 3, 0, 15, 3)

        

        self.load_style()

        self.setLayout(self.grid)


    def load_style(self):
        with open("style.qss", "r") as file:
            stylesheet = file.read()

        self.setStyleSheet(stylesheet)

#    def display_response(self):
#        self.box_eeprom_output.clear()
##        while True:
#            line = self.terminal.ser.readline().decode("utf-8")
#            if not line:
#                break
#            self.box_eeprom_output.append(line)
        



