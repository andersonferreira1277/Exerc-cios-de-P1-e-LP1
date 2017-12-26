#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""

from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtGui import QIntValidator
from PyQt5 import uic
import os

from modelo.Aluno import Aluno
from persistencia.DB import GeradorDB
from modelo.DadosDaTurma import DadosDaTurma
from modelo.DadosDeNascimento import DadosDeNascimento
from modelo.DadosDoAluno import DadosDoAluno


class ViewCadastro(QDialog):

    def __init__(self, parent=None):
        super(ViewCadastro, self).__init__(parent)
        self.initCadastro()

    def initCadastro(self):
        url = os.path.abspath('view/cadastro.ui')
        uic.loadUi(url, self)

        # QLineEdit Ano Letivo, só pode ter um número e no máximo 4 números.
        self.anoLetivoLineEdit.setValidator(QIntValidator())
        self.anoLetivoLineEdit.setMaxLength(4)

        self.cadastrarButton.clicked.connect(self.inserirNoBD)

        self.show()

    def inserirNoBD(self):
        nomeAluno = self.nomeDoAlunoLineEdit.text()
        nomeDoPai = self.nomeDoPaiDoAlunoLineEdit.text()
        nomeDaMae = self.nomeDaMEDoAlunoLineEdit.text()
        dataDeNascimento = self.dataDeNascimentoAlunoDateEdit.text()
        cidadeDeNascimento = self.naturalidadeLineEdit.text()
        estadoDeNascimento = self.uFLineEdit.text()
        #segmentoEducacionalComboBox
        #serieComboBox
        anoLetivo = self.anoLetivoLineEdit.text()

        messageBox = QMessageBox.Yes
        gerador = GeradorDB()
        if len(gerador.select(nomeAluno)) > 0:
            messageBox = QMessageBox.warning(self, 'Nome já existe no Banco de dados.',
                                             'O nome do aluno já existe. Deseja cadastrar assim mesmo?',
                                             QMessageBox.Yes | QMessageBox.No)

        if messageBox == QMessageBox.Yes:
            a = DadosDoAluno(nomeAluno, nomeDoPai, nomeDaMae)
            b = DadosDeNascimento(dataDeNascimento, cidadeDeNascimento, estadoDeNascimento)
            c = DadosDaTurma("3º ano", "Ensino Médio", anoLetivo)
            al = Aluno(a, b, c)

            gerador.insert(al)

        self.close()