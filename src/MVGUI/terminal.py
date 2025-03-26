from PyQt5.QtCore import QObject, QThread, pyqtSignal
import serial
import time

class Terminalworker(QThread):
    response_received = pyqtSignal(str)
    error_occurred = pyqtSignal(str)

    def __init__(self, port="COM4", baudrate=115200):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.ser = None
        self.running = False
        self.command_queue = []

    def run(self):
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=2)
            print(f"Connected to {self.port} at {self.baudrate} baud.")
            self.running = True
        except serial.SerialException as e:
            self.error_occurred.emit(f"Error opening serial port: {e}")
            return

        self.running = True
        while self.running:
            if self.command_queue:
                command = self.command_queue.pop(0)
                print(f"processing command: {command}")
                try:
                    self.ser.write(command.encode()+b"\n")
                    time.sleep(0.1)
                    while True:
                        response = self.ser.readline().decode("utf-8")
                        if not response:
                            break

                        self.response_received.emit(response)
                    print(f" response: {response}")
                except serial.SerialException as e:
                    self.error_occurred.emit(f"Serial communication error: {e}")
                    self.stop()   

    def send_command(self, command):
        if self.ser is None:
            self.error_occurred.emit("Serial port not initialized.")
            return
        self.command_queue.append(command)
        print(self.command_queue)

    def stop(self):
        self.running = False
        if self.ser and self.ser.is_open:
            self.ser.close()
        self.quit()
        self.wait()

class Terminal(QObject):
    response_received = pyqtSignal(str)
    error_occurred = pyqtSignal(str)

    def __init__(self, port="COM4", baudrate=115200):
        super().__init__()
        self.worker = Terminalworker(port, baudrate)
    
        self.worker.response_received.connect(self.response_received)
        self.worker.error_occurred.connect(self.error_occurred)
    

        self.worker.start()



    def send_command(self, command):
        self.worker.send_command(command)

    def stop(self):
        self.worker.stop()
