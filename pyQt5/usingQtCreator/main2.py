#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#andersonferreira1277@gmail.com

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('mainwindow.ui',self)
        self.pushButton.clicked.connect(self.mudarTexto)
        self.show()
    
    def mudarTexto(self):
        self.label.setText("Anderson")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MyWindow()
    sys.exit(app.exec_())