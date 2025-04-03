from PyQt5.QtWidgets import QTabWidget, QMainWindow, QVBoxLayout, QWidget


# Subclass QMainWindow to customize your application's main window
class MasterTabView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.setWindowTitle("My App")
        self.tabs = QTabWidget()
        self.tabs.resize(300,200)

        layout.addWidget(self.tabs)
        self.setLayout(layout)

