from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QGridLayout
from PyQt5.Qt import Qt


class PiezoVariantTab(QWidget):
    def __init__(self):
        super().__init__()
        self.grid = QGridLayout()
        self.grid.setSpacing(100)

        self.pushButton1 = QPushButton("PyQt5 button", self)
        self.grid.addWidget(self.pushButton1, 0, 1, alignment=Qt.AlignCenter)
        self.pushButton2 = QPushButton("Second button", self)
        self.grid.addWidget(self.pushButton2, 0, 2, alignment=Qt.AlignCenter)
        self.label = QLabel("Draftlabel", self)
        self.label.setText("Testlabel")
        self.label.adjustSize()
        self.grid.addWidget(self.pushButton1, 0, 3, alignment=Qt.AlignCenter)
        self.textbox = QLineEdit(self)
        self.grid.addWidget(self.pushButton1, 0, 4, alignment=Qt.AlignCenter)
        self.setLayout(self.grid)

