#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""

from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit
from PyQt5.QtGui import QIntValidator, QPalette, QColor
from PyQt5 import uic
import os

from modelo.Aluno import Aluno
from persistencia.DB import GeradorDB
from modelo.DadosDaTurma import DadosDaTurma
from modelo.DadosDeNascimento import DadosDeNascimento
from modelo.DadosDoAluno import DadosDoAluno
from modelo.ModeloMatriculado import Modelo


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

        segmento = ['Curso da Educação Infantil', 'Ensino Fundamental I', 'Ensino Fundamental II', 'Ensino Médio']
        self.segmentoEducacionalComboBox.addItems(segmento)
        self.segmentoEducacionalComboBox.currentIndexChanged.connect(self.mudarSerie)
        self.mudarSerie()

        self.cadastrarButton.clicked.connect(self.inserirNoBD)

        self.show()

    def inserirNoBD(self):
        """Insere as informações digitadas no banco de dados, cria o arquivo e abre"""
        if self.verificaCamposVazios()> 0: # Verifica se existe alguma campo vazio
            return 1 # se existir algum campo vazio, termina a função aqui

        nomeAluno = self.nomeDoAlunoLineEdit.text()
        nomeDoPai = self.nomeDoPaiDoAlunoLineEdit.text()
        nomeDaMae = self.nomeDaMEDoAlunoLineEdit.text()
        dataDeNascimento = self.dataDeNascimentoAlunoDateEdit.text()
        cidadeDeNascimento = self.naturalidadeLineEdit.text()
        estadoDeNascimento = self.uFLineEdit.text()
        segmentoEducacional = self.segmentoEducacionalComboBox.currentText()
        serie = self.serieComboBox.currentText()
        anoLetivo = self.anoLetivoLineEdit.text()

        messageBox = QMessageBox.Yes
        gerador = GeradorDB()

        # Verifica se o nome já existe no banco de dados
        if len(gerador.selectNomeIgual(nomeAluno)) > 0:
            messageBox = QMessageBox.warning(self, 'Nome já existe no Banco de dados.',
                                             'O nome do aluno já existe. Deseja cadastrar assim mesmo?',
                                             QMessageBox.Yes | QMessageBox.No)

        # Se não existir ou o usuario queria inserir, é criado um Objeto aluno inserido no banco de dados
        # e criada a declaração.
        if messageBox == QMessageBox.Yes:
            a = DadosDoAluno(nomeAluno, nomeDoPai, nomeDaMae)
            b = DadosDeNascimento(dataDeNascimento, cidadeDeNascimento, estadoDeNascimento)
            c = DadosDaTurma(serie, segmentoEducacional, anoLetivo)
            al = Aluno(a, b, c)

            gerador.insert(al)

            Modelo.replaceModel(al)

        self.close()

    def mudarSerie(self):
        if self.segmentoEducacionalComboBox.currentText() == 'Curso da Educação Infantil':
            self.serieComboBox.clear()
            self.serieComboBox.addItems(['Maternal I', 'Maternal II', 'Infantil I', 'Alfabetização'])
        elif self.segmentoEducacionalComboBox.currentText() == 'Ensino Fundamental I':
            self.serieComboBox.clear()
            self.serieComboBox.addItems(['1º ano', '2º ano', '3º ano', '4º ano', '5º ano'])
        elif self.segmentoEducacionalComboBox.currentText() == 'Ensino Fundamental II':
            self.serieComboBox.clear()
            self.serieComboBox.addItems(['6º ano', '7º ano', '8º ano', '9º ano'])
        elif self.segmentoEducacionalComboBox.currentText() == 'Ensino Médio':
            self.serieComboBox.clear()
            self.serieComboBox.addItems(['1º ano', '2º ano', '3º ano'])

    def verificaCamposVazios(self):
        count = 0
        for i in self.children(): # Obtem todos componentes da view
            for x in i.children(): # obtem todos os componentes de i
                # print(type(x)) # mostra a lista de classe de i
                if type(x) == QLineEdit: # se o componente for do tipo QLineEdit, Verifica se está vazio
                    if x.text() =='':
                        count+=1
                        pallete = QPalette()
                        pallete.setColor(x.backgroundRole(), QColor(255, 80, 80)) # cor
                        x.setPalette(pallete) # seta a cor para campos vazios

        if count > 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Por favor, preencha os campos obrigatórios.")
            msg.setWindowTitle("Informação")
            msg.exec_()

        return count