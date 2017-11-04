#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initMyWindow()

    def initMyWindow(self):
        self.setGeometry(90, 50, 200, 200)
        label = QLabel("Hello World", self)
        label.move(25, 40)
        closebutton = QPushButton("Close", self)
        closebutton.move(50, 80)
        closebutton.clicked.connect(lambda: self.doThis(closebutton))
        closebutton.clicked.connect(self.close)
        self.show()

    def doThis(self, button):
        print("Hello world")
        print(button.text(), "Opa")


    """def labelText(self):
        sender = self.sender()

        if sender is self.closebutton:"""


app = QApplication(sys.argv)
frame = MyWindow()
app.exec_()