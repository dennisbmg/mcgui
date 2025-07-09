from PyQt5.QtWidgets import QDialog, QVBoxLayout, QComboBox, QDialogButtonBox, QLabel, QLineEdit
import serial.tools.list_ports

class SerialConnectDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Microcontroller")
        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Serial Port:"))
        self.port_combo = QComboBox()
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.port_combo.addItem(port.device)
        layout.addWidget(self.port_combo)

        layout.addWidget(QLabel("Baudrate:"))
        self.baudrate_edit = QLineEdit("115200")
        layout.addWidget(self.baudrate_edit)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def get_selection(self):
        return self.port_combo.currentText(), int(self.baudrate_edit.text())

