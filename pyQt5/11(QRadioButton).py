#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Radiodemo(QWidget):
    def __init__(self):
        super(Radiodemo, self).__init__()
        self.initRadioDemo()
    def initRadioDemo(self):
        layout = QHBoxLayout()
        self.b1=QRadioButton("Button1")
        self.b1.setChecked(True)
        self.b1.toggled.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.b1)

        self.b2=QRadioButton("Button2")
        self.b2.toggled.connect(lambda:self.btnstate(self.b2))
        layout.addWidget(self.b2)

        self.setLayout(layout)
        self.setWindowTitle("RadioButton demo")
        self.show()
    def btnstate(self,b):
        if b.text()=="Button1":
            if b.isChecked()==True:
                print(b.text()+" is selected")
            else:
                print(b.text()+" is deselected")
        if b.text()=="Button2":
            if b.isChecked()==True:
                print(b.text()+" is selected")
            else:
                print(b.text()+" is deselected")

app = QApplication(sys.argv)
frane = Radiodemo()
app.exec_()
