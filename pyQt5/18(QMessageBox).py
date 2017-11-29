#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
from PyQt5.QtWidgets import *

class MessageDemo(QWidget):
    def __init__(self):
        super(MessageDemo, self).__init__()
        self.initUI()
    def initUI(self):
        b = QPushButton(self)
        b.setText("Show message!")
        b.move(50,50)
        b.clicked.connect(self.showdialog)

        self.setWindowTitle("PyQt Dialog demo")
        self.show()

    def showdialog(self):
        msg=QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("This is a message box")
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("MessageBox demo")
        msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self.msgbtn)
        retval = msg.exec_()
        #if (retval==QMessageBox.Ok):
        print("value of pressed message box button: " + str(retval))
    def msgbtn(self, i):
        print("Button pressed is: " + i.text())

app = QApplication(sys.argv)
frame = MessageDemo()
sys.exit(app.exec_())
