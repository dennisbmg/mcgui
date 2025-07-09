from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QMenuBar
import master_tab


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "MC GUI" 
        self.left = 0
        self.top = 0
        height = 0
        width = 670
        size = QSize(width, height)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, size.width(), size.height())

        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)
        self.connect_menu = self.menu_bar.addMenu("Connect")

        self.statusBar().showMessage("Ready")


        
        self.table_widget = master_tab.MasterTabView()
        self.setCentralWidget(self.table_widget)
        
        self.show()


    def addTabView(self, tab, name):
        self.table_widget.tabs.addTab(tab, name)

    def update_statusbar(self, message):
        self.statusBar().showMessage(message)

