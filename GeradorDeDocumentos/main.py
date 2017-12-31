#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from view.cadastroController import ViewCadastro
from view.pesquisaController import PesquisaController


class MyMainWindow(QMainWindow):
    _instanceJanelaCadastro = None
    _instanceJanelaPesquisa = None

    def __init__(self):
        super(MyMainWindow, self).__init__()
        uic.loadUi('mainwindowView.ui', self)
        self.cadastro.clicked.connect(self.abrirTelaCadastro)
        self.pesquisa.clicked.connect(self.abrirTelaPesquisa)
        self.statusbar.showMessage('Anderson Ferreira Câmara - andersonferreira1277@gmail.com ')

        self.show()

    def abrirTelaCadastro(self):
        if not self._instanceJanelaCadastro:
            self._instanceJanelaCadastro = ViewCadastro(self)
            self._instanceJanelaCadastro.exec_()
            self._instanceJanelaCadastro = None

    def abrirTelaPesquisa(self):
        if not self._instanceJanelaPesquisa:
            self._instanceJanelaPesquisa = PesquisaController(self)
            self._instanceJanelaPesquisa.exec_()
            self._instanceJanelaPesquisa = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MyMainWindow()
    sys.exit(app.exec_())
