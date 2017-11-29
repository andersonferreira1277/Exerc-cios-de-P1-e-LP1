#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
from PyQt5.QtWidgets import *

class DemoQInputDialog(QWidget):
    def __init__(self):
        super(DemoQInputDialog, self).__init__()
        self.initUI()
    def initUI(self):
        layout = QFormLayout()
        self.btn=QPushButton("Choose from list")
        self.btn.clicked.connect(self.getItem)
        self.le=QLineEdit()
        layout.addRow(self.btn,self.le)

        self.btn1=QPushButton("get name")
        self.btn1.clicked.connect(self.gettext)
        self.le1=QLineEdit()
        layout.addRow(self.btn1,self.le1)

        self.btn2=QPushButton("Enter an integer")
        self.btn2.clicked.connect(self.getint)
        self.le2=QLineEdit()
        layout.addRow(self.btn2,self.le2)

        self.setLayout(layout)
        self.setWindowTitle("Input Dialog demo")
        self.show()
    def getItem(self):
        items = ("C", "C++", "Java", "Python")
        item, ok = QInputDialog.getItem(self, "select input dialog",
            "list of languages", items, 0, False)
        if ok and item:
            self.le.setText(item)
    def gettext(self):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:')
        if ok:
            self.le1.setText(str(text))
    def getint(self):
        num,ok = QInputDialog.getInt(self,"integer input dualog","enter a number")
        if ok:
            self.le2.setText(str(num))
app = QApplication(sys.argv)
frame = DemoQInputDialog()
sys.exit(app.exec_())
