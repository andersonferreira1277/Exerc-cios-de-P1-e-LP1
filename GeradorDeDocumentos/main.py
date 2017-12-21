#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton,QWidget
from PyQt5 import uic


class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        uic.loadUi('mainwindowView.ui', self)
        self.statusbar.showMessage('Anderson Ferreira Câmara - andersonferreira1277@gmail.com ')

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MyMainWindow()
    sys.exit(app.exec_())