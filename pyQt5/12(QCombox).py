#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class ComboDemo(QWidget):
    def __init__(self):
        super(ComboDemo, self).__init__()
        self.initComboDemo()
    def initComboDemo(self):
        layout = QHBoxLayout()
        self.cb = QComboBox()
        self.cb.addItem("C")
        self.cb.addItem("C++")
        self.cb.addItems(["Java", "C#", "Python"])
        self.cb.currentIndexChanged.connect(self.selectionchange)

        layout.addWidget(self.cb)
        self.setLayout(layout)
        self.setWindowTitle("combo box demo")
        self.show()
    def selectionchange(self,i):
        print("Items in the list are :")
        for count in range(self.cb.count()):
            print(self.cb.itemText(count))
        print("Current index "+str(i)+" selection changed "+self.cb.currentText())
app = QApplication(sys.argv)
frame = ComboDemo()
app.exec_()
