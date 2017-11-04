#!/usr/bin/env python3
import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initMyWindow()

    def initMyWindow(self):
         label1 = QLabel()
         label2 = QLabel()
         label3 = QLabel()
         label4 = QLabel()

         label1.setText("Hello World")
         label4.setText("<a href='https://www.python.org/'>Python</a>")
         label2.setText("<a href='#'>Welcome To programming in Python GUI</a>")

         label1.setAlignment(Qt.AlignCenter)
         label2.setAlignment(Qt.AlignCenter)
         label3.setAlignment(Qt.AlignCenter)
         label4.setAlignment(Qt.AlignCenter)

         label3.setPixmap(QPixmap("python.jpg"))

         vbox = QVBoxLayout()
         vbox.addWidget(label1)
         vbox.addStretch(0)
         vbox.addWidget(label2)
         vbox.addStretch(0)
         vbox.addWidget(label3)
         vbox.addStretch(0)
         vbox.addWidget(label4)
         vbox.addStretch(0)

         label4.setOpenExternalLinks(True)
         label4.linkActivated.connect(self.clicked)
         label2.linkHovered.connect(self.hovered)
         label1.setTextInteractionFlags(Qt.TextSelectableByMouse)
         self.setLayout(vbox)
         self.setWindowTitle("PyQt5")
         self.show()
    def clicked(self):
        print("Clicked")

    def hovered(self):
        print("Hovered")

app = QApplication(sys.argv)
frame = MyWindow()
app.exec_()