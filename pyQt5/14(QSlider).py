#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class SliderDemo(QWidget):
    def __init__(self):
        super(SliderDemo, self).__init__()
        self.initSliderDemo()
    def initSliderDemo(self):
        layout = QVBoxLayout()
        self.l1=QLabel("Hello")
        self.l1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l1)

        self.sl=QSlider(Qt.Horizontal)
        self.sl.setMinimum(10)
        self.sl.setMaximum(40)
        self.sl.setValue(20)
        self.sl.setTickPosition(QSlider.TicksAbove)
        self.sl.setTickInterval(5)
        layout.addWidget(self.sl)
        self.sl.valueChanged.connect(self.valuechange)
        self.setLayout(layout)
        self.setWindowTitle("SpinBox demo")
        self.show()
    def valuechange(self):
        size=self.sl.value()
        self.l1.setFont(QFont("Arial",size))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = SliderDemo()
    app.exec_()
