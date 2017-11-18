#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class SpinDemo(QWidget):
    def __init__(self):
        super(SpinDemo, self).__init__()
        self.initSpinDemo()
    def initSpinDemo(self):
        layout = QVBoxLayout()
        self.l1=QLabel("current value:")
        self.l1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l1)

        self.sp=QSpinBox()
        layout.addWidget(self.sp)
        self.sp.valueChanged.connect(self.valuechange)

        self.setLayout(layout)
        self.setWindowTitle("SpinBox demo")
        self.show()
    def valuechange(self):
        self.l1.setText("current value:"+str(self.sp.value()))
app = QApplication(sys.argv)
frame = SpinDemo()
app.exec_()
