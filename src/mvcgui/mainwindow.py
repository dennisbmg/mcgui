from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QMenuBar, QAction
import master_tab
from terminal import Terminal
from serial_dialog import SerialConnectDialog



class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "MVC GUI" 
        self.left = 0
        self.top = 0
        height = 0
        width = 670
        size = QSize(width, height)
        self.init_menu()
        self.terminal =  Terminal

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, size.width(), size.height())
        self.statusBar().showMessage("Ready")
        self.table_widget = master_tab.MasterTabView()
        self.setCentralWidget(self.table_widget)
        self.show()

    def init_menu(self):
            menubar = self.menuBar()
            connection_menu = menubar.addMenu('Connection')
            connect_action = QAction('Connect', self)
            connect_action.triggered.connect(self.show_connect_dialog)
            connection_menu.addAction(connect_action)

    def show_connect_dialog(self):
        dialog = SerialConnectDialog(self)
        if dialog.exec_():
            port, baudrate = dialog.get_selection()
            try:
                self.terminal.connect(port, baudrate)
                QMessageBox.information(self, "Connection", f"Connected to {port} at {baudrate} baud.")
            except Exception as e:
                QMessageBox.critical(self, "Connection Error", str(e))


    def addTabView(self, tab, name):
        self.table_widget.tabs.addTab(tab, name)

    def update_statusbar(self, message):
        self.statusBar().showMessage(message)

