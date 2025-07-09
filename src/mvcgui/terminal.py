from PyQt5.QtCore import QObject, QThread, pyqtSignal, QMutex
import serial
import time

class TerminalWorker(QThread):
    response_received = pyqtSignal(str)
    error_occurred = pyqtSignal(str)

    def __init__(self, port="COM4", baudrate=115200):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        # self.ser = None
        self.running = False
        self.command_queue = []
        self.mutex = QMutex()  # Ensure thread safety

    def run(self):
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=2)
            print(f"Connected to {self.port} at {self.baudrate} baud.")
            self.running = True
        except serial.SerialException as e:
            self.error_occurred.emit(f"Error opening serial port: {e}")
            return

        while self.running:
            self.mutex.lock()
            has_command = bool(self.command_queue)  # Check if there's a command
            self.mutex.unlock()

            if has_command:
                self.process_command()
            else:
                self.msleep(50)  # Reduce CPU usage when idle

    def process_command(self):
        self.mutex.lock()
        if self.command_queue:
            command = self.command_queue.pop(0)
        else:
            self.mutex.unlock()
            return
        self.mutex.unlock()

        print(f"Processing command: {command}")
        try:
            self.ser.write(command.encode() + b"\n")

            # Wait for response with a timeout
            start_time = time.time()
            response = b""
            while time.time() - start_time < 2:  # 2 seconds timeout
                if self.ser.in_waiting:
                    response += self.ser.read(self.ser.in_waiting)
                time.sleep(0.05)  # Small delay to reduce CPU usage

            if response:
                response_str = response.decode("utf-8").strip()
                self.response_received.emit(response_str)
                print(f"Response: {response_str}")

        except serial.SerialException as e:
            self.error_occurred.emit(f"Serial communication error: {e}")
            self.stop()


    def send_command(self, command):
        if not self.ser or not self.ser.is_open:
            self.error_occurred.emit("Serial port not initialized.")
            return

        self.mutex.lock()
        self.command_queue.append(command)
        self.mutex.unlock()

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
        self.worker = TerminalWorker(port, baudrate)
    
        self.worker.response_received.connect(self.response_received)
        self.worker.error_occurred.connect(self.error_occurred)
    

        self.worker.start()



    def send_command(self, command):
        self.worker.send_command(command)

    def stop(self):
        self.worker.stop()
