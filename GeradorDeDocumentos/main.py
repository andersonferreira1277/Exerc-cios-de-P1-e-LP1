#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import uic
from view.cadastroController import ViewCadastro


class MyMainWindow(QMainWindow):
    _instance = None

    def __init__(self):
        super(MyMainWindow, self).__init__()
        uic.loadUi('mainwindowView.ui', self)
        self.cadastro.clicked.connect(self.abrirTelaCadastro)
        self.statusbar.showMessage('Anderson Ferreira Câmara - andersonferreira1277@gmail.com ')

        self.show()

    def abrirTelaCadastro(self):
        if not self._instance:
            self._instance = ViewCadastro(self)
            self._instance.exec_()
            self._instance = None
        else:
            self._instance.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MyMainWindow()
    sys.exit(app.exec_())