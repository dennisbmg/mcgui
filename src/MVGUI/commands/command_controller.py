from command_view import CommandView
from terminal import Terminal

class CommandController:
    def __init__(self):
        self.view = CommandView()
        self.terminal = Terminal()

        self.view.btn_read_param.clicked.connect(self.terminal.read_parameter)
        self.view.btn_read_param.clicked.connect(self.display_response)


    def display_response(self):
        self.view.box_eeprom_output.clear()
        while True:
            line = self.terminal.ser.readline().decode("utf-8")
            if not line:
                break
            self.view.box_eeprom_output.append(line)
        

