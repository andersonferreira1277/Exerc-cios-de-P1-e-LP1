#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initMyWindow()

    def initMyWindow(self):
        global myField, mySlider
        myField = QLineEdit()
        mySlider = QSlider(1) # 1 = Horizontal
        mySlider.setRange(0, 100)


        hLayout = QHBoxLayout()
        self.setLayout(hLayout)
        hLayout.addWidget(myField)
        hLayout.addWidget(mySlider)

        mySlider.valueChanged.connect(self.updateField)
        myField.textChanged.connect(self.updateSlider)

        self.setWindowTitle("Text and Slider")
        self.show()

    def updateField(self, value):
        myField.setText(str(value))

    def updateSlider(self, text):
        try:
            mySlider.setValue(int(text))
        except ValueError:
            pass

app = QApplication(sys.argv)
frame = MyWindow()
app.exec_()
