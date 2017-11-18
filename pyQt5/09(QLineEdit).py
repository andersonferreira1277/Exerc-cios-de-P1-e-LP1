#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initMyWindow()
    def initMyWindow(self):
        e1 = QLineEdit()
        e1.setValidator(QIntValidator())
        e1.setMaxLength(4)
        e1.setAlignment(Qt.AlignRight)
        e1.setFont(QFont("Arial",20))

        e2=QLineEdit()
        e2.setValidator(QDoubleValidator(0.99,99.99,2))

        flo=QFormLayout()
        flo.addRow("integer validator", e1)
        flo.addRow("Double validator",e2)

        e3=QLineEdit()
        e3.setInputMask('+99_9999_999999')
        flo.addRow("Input Mask",e3)

        e4=QLineEdit()
        e4.textChanged.connect(lambda: self.textchanged(self.sender()))
        flo.addRow("Text changed",e4)

        e5=QLineEdit()
        e5.setEchoMode(QLineEdit.Password)
        flo.addRow("Password",e5)

        e6=QLineEdit("Hello Python")
        e6.setReadOnly(True)
        flo.addRow("Read Only",e6)

        e5.editingFinished.connect(lambda: self.enterPress(self.sender()))

        self.setLayout(flo)
        self.setWindowTitle("PyQt")
        self.show()

    def textchanged(self, lineEdit):
        print("Texto mudado "+lineEdit.text())
    def enterPress(self, lineEdit):
        print("edited")

app = QApplication(sys.argv)
frame = MyWindow()
app.exec_()
