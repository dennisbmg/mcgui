from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow
import master_tab


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "MC GUI" 
        self.left = 0
        self.top = 0
        self.setWindowTitle(self.title)
        #self.setGeometry(self.left, self.top, self.width, self.height)

        self.menu_bar = self.menuBar()
        self.connect_menu = self.menu_bar.addMenu("Connect")

        
        self.table_widget = master_tab.MasterTabView()
        self.setCentralWidget(self.table_widget)
        
        self.show()


    def addTabView(self, tab, name):
        self.table_widget.tabs.addTab(tab, name)
