from . import command_view
from PyQt5.QtWidgets import QWidget

class CommandController(QWidget):
    def __init__(self, terminal):
        super().__init__()
        self.view = command_view.CommandView()
        self.terminal = terminal
        
        self.terminal.response_received.connect(self.display_response)
        self.terminal.error_occurred.connect(self.display_error)


        self.view.btn_read_param.clicked.connect(lambda: self.terminal.send_command("EEREAD PAR"))
        self.view.btn_read_memory.clicked.connect(lambda: self.terminal.send_command("EEREAD MEM"))
        self.view.btn_load_default.clicked.connect(lambda: self.terminal.send_command(f"EELOAD DEFAULT {self.view.cmb_load_param.currentText()}")\
                if self.view.cmb_load_param.currentText() != "-" else self.terminal.send_command(f"EELOAD DEFAULT"))
        self.view.btn_erase_param.clicked.connect(lambda: self.terminal.send_command("EERASE PAR"))
        self.view.btn_erase_logdata.clicked.connect(lambda: self.terminal.send_command("EERASE LOG"))
    
    def display_response(self, response):
        self.view.box_eeprom_output.append(response)

    def display_error(self, error_message):
        self.view.box_eeprom_output.append(f"Error: {error_message}")

    def closeEvent(self, a0):
        self.terminal.stop()
        super().closeEvent(a0)
