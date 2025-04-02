from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTabWidget, QGridLayout
from PyQt5.QtCore import Qt

class CommonBlockView(QWidget):
    def __init__(self):
        super().__init__()


        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.inner_tabs = QTabWidget()
        self.layout.addWidget(self.inner_tabs)

        self.inner_views = {}  # Track each tab's UI data
        self.labels = {}
        self.input = {}
        self.setButtons = {}

    def add_tab_item(self, tab_name, param_name, input_field):
        column_label = 0
        column_input = 1
        column_button = 2
        if tab_name not in self.inner_views:
            inner_widget = QWidget()
            inner_layout = QGridLayout()
            inner_layout.setSpacing(10)
            inner_widget.setLayout(inner_layout)

            self.inner_tabs.addTab(inner_widget, tab_name)

            self.inner_views[tab_name] = {
                "widget": inner_widget,
                "layout": inner_layout,
                "row": 0,
                "labels": {},
                "inputs": {},
                "buttons": {},
                "button_all": None
            }

        data = self.inner_views[tab_name]
        row = data["row"]

        label = QLabel(param_name)
        input = input_field()
        button = QPushButton("Set")
        button.setDisabled(True)

        self.labels[param_name] = label
        self.input[param_name] = input
        self.setButtons[param_name] = button

        data["layout"].addWidget(label, row, column_label, alignment=Qt.AlignLeft)
        data["layout"].addWidget(input, row, column_input)
        data["layout"].addWidget(button, row, column_button)

        data["labels"][param_name] = label
        data["inputs"][param_name] = input_field
        data["buttons"][param_name] = button

        data["row"] += 1


        if data["button_all"] is None:
            self.btn_all = QPushButton("Set All")
            self.btn_all.setDisabled(True)
            data["layout"].addWidget(self.btn_all, 20, 2)
            data["button_all"] = self.btn_all
            data["row"] += 1  # move row count up so future widgets are still clean



