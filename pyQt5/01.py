#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
frame = QWidget()
frame.setWindowTitle("Anderson")
frame.setGeometry(90, 50, 400, 200) #altura
frame.show()
app.exec_()
