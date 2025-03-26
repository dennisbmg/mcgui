import serial
import time


class Terminal:
    def __init__(self, port="COM4", baudrate=115200):
        try:
            self.ser = serial.Serial(port, baudrate, timeout=1)
            print(f"Connected to {port} at {baudrate} baud.")
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")


    def is_connected(self):
        pass

    def read_parameter(self):
        print("reading parameter")
        self.ser.write(b"EEREAD PAR\n")

    def read_memory(self):
        print("reading memory")
        self.ser.write(b"EEREAD MEM\n")

    def set_parameter(self, parameter, value, old_value):
        if value != old_value:
            command = f"eeset {parameter} {value}\n"
            self.ser.write(command.encode()) 
            print(command.encode())
            time.sleep(0.1)
        else:
            print("value already set")

    def load_default(self, default_char=None):
        if default_char == None:
            command = (f"EELOAD DEFAULT\n")
            self.ser.write(command.encode())
        else:
            command = (f"EELOAD DEFAULT {default_char}\n")
            self.ser.write(command.encode())

    def erase_parameter(self):
        command = "eerase par\n"
        self.ser.write(command.encode())

    def erase_log(self):
        command = "eerase log\n"
        self.ser.write(command.encode())

    def erase_all(self):
        command = "eerase all\n"
        self.ser.write(command.encode())

    def read_response(self):
        response = self.ser.readline()
        return response


