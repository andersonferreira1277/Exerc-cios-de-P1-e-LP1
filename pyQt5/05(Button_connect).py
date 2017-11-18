#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initMyWindow()

    def initMyWindow(self):
        self.setGeometry(98, 50, 200, 200)
        closeButton = QPushButton("Close", self)
        closeButton.move(50, 80)
        closeButton.clicked.connect(self.doThis)
        closeButton.clicked.connect(self.close)
        self.show()

    def doThis(self):
        print("The close button has been clicked")

app = QApplication(sys.argv)
frame = MyWindow()
app.exec_()
