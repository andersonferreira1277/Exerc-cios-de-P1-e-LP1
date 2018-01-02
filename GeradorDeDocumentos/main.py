#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""
import sys, os, platform
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic
from view.cadastroController import ViewCadastro
from view.pesquisaController import PesquisaController
from persistencia.DB import GeradorDB


class MyMainWindow(QMainWindow):
    _instanceJanelaCadastro = None
    _instanceJanelaPesquisa = None
    gerador = GeradorDB()

    def __init__(self):
        super(MyMainWindow, self).__init__()
        uic.loadUi('mainwindowView.ui', self)

        self.cadastro.clicked.connect(self.abrirTelaCadastro)

        self.pesquisa.clicked.connect(self.abrirTelaPesquisa)

        self.mostrarCaminho()

        self.btnSelecionar.clicked.connect(self.escolherCaminho)

        self.btnAbrirPasta.clicked.connect(self.abrirPasta)

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

    def mostrarCaminho(self):
        self.lineEditCaminho.setText(self.gerador.obterCaminho())

    def escolherCaminho(self):
        dlg = QFileDialog.getExistingDirectory(self, 'Onde salvar?', '/')
        dlg = os.path.abspath(dlg)
        self.gerador.salvarCaminho(dlg)
        self.mostrarCaminho()

    def abrirPasta(self):
        sistema = platform.system()
        if sistema == 'Linux':
            os.startfile(self.gerador.obterCaminho())
        if sistema == 'Windows':
            os.startfile(self.gerador.obterCaminho())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MyMainWindow()
    sys.exit(app.exec_())
