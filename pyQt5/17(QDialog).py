#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class DialogDemo(QWidget):
    def __init__(self):
        super(DialogDemo, self).__init__()
        self.initUI()
    def initUI(self):
        b = QPushButton(self)
        b.setText("Hello World!")
        b.move(50,50)
        b.clicked.connect(self.showDialog)
        self.setWindowTitle("PyQt Dialog demo")
        self.show()
    def showDialog(self):
        d = QDialog()
        b1 = QPushButton("ok",d)
        b1.clicked.connect(d.close)
        b1.move(50,50)
        d.setWindowTitle("Dialog")
        d.setWindowModality(Qt.ApplicationModal)
        d.exec_()

app = QApplication(sys.argv)
frame = DialogDemo()
sys.exit(app.exec_())
