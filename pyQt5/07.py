#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initMyWindow()

    def initMyWindow(self):
        labelNome = QLabel("Name")
        lineNome = QLineEdit()

        labelAddress = QLabel("Endereço")
        addAddress1 = QLineEdit()
        addAddress2 = QLineEdit()

        fbox = QFormLayout()
        fbox.addRow(labelNome,lineNome)

        vboxAddress = QVBoxLayout()
        vboxAddress.addWidget(addAddress1)
        vboxAddress.addWidget(addAddress2)
        fbox.addRow(labelAddress, vboxAddress)

        hboxSexo = QHBoxLayout()
        radioMasculino = QRadioButton("Masculino")
        radioFeminino = QRadioButton("Feminino")
        hboxSexo.addWidget(radioMasculino)
        hboxSexo.addWidget(radioFeminino)
        #hboxSexo.stretch(1)
        fbox.addRow(QLabel("sexo"), hboxSexo)

        self.setLayout(fbox)
        self.setWindowTitle("PyQt form")
        self.show()

app = QApplication(sys.argv)
frame = MyWindow()
app.exec_()