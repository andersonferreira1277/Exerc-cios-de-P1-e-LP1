#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
import os
from PyQt5 import uic
from persistencia.DB import GeradorDB
from modelo.DadosDoAluno import DadosDoAluno
from modelo.DadosDeNascimento import DadosDeNascimento
from modelo.DadosDaTurma import DadosDaTurma
from modelo.Aluno import Aluno
from PyQt5.Qt import Qt
from modelo.ModeloMatriculado import Modelo


class PesquisaController(QDialog):
    gerador = GeradorDB()

    def __init__(self, parent=None):
        super(PesquisaController, self).__init__(parent)
        self.initMyUi()

    def initMyUi(self):
        url = os.path.abspath('view/pesquisa.ui')
        uic.loadUi(url, self)

        self.nomeDoAlunoLineEdit.textChanged.connect(self.procurarAluno) # ao digitar na caixa de texto
        # chama a funcão de procurar o aluno

        self.tableWidget.cellChanged.connect(self.editarRegistro) # quando o valor da celula muda, chama
        # a função que atualiza o banco de dados

        self.btnGerarDeclaracao.clicked.connect(self.gerarDeclaracao) # conectado a função
        # gerar declaração

        self.btnExcluirAluno.clicked.connect(self.excluirAluno) # conectado a função excluir aluno

        self.procurarAluno()

        self.setWindowTitle('Pesquisar aluno')
        self.show()

    def procurarAluno(self):
        """Atualiza a lista de alunos sequindo o parametro de nomeDoAlunoLineEdit quando o texto do
        componente muda"""

        # Obtendo a lista de alunos
        nomeDoAluno = self.nomeDoAlunoLineEdit.text()
        lista = self.gerador.selectNomeLike(nomeDoAluno)

        # list(map(lambda x: print(x), lista)) # imprime todos os alunos retornados. Para testes.

        # Inserindo a lista de alunos na tabela
        if len(lista) > 0:
            self.tableWidget.setRowCount(0)
            for i in range(len(lista)):
                self.tableWidget.insertRow(i)
                aluno = lista[i].toList()

                for x in range(len(aluno)):
                    item = QTableWidgetItem(str(aluno[x]))
                    column = x
                    if column == 0:
                        item.setFlags(Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, column, item)
        else:
            self.tableWidget.setRowCount(0)

    def itemSelecionado(self):
        """Retorna o item selecionado"""

        al = None

        linha = self.tableWidget.currentRow() # linha selecionada pelo usuario

        aluno = {}
        listaParaChaves = ['id', 'nome_aluno', 'pai', 'mae', 'data', 'cidade_nascimento',
                           'estado_nascimento', 'serie', 'segmento', 'ano_letivo']

        if linha > -1: # cellChanged retorna -1 caso não tenha nenhuma celula com mudança
            for i in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(linha, i)
                aluno[listaParaChaves[i]] = item.text() # adiciona em cada chave o item da tabela
                # relacionado

            a = DadosDoAluno(aluno['nome_aluno'], aluno['pai'], aluno['mae'])
            b = DadosDeNascimento(aluno['data'], aluno['cidade_nascimento'], aluno['estado_nascimento'])
            c = DadosDaTurma(aluno['serie'], aluno['segmento'], aluno['ano_letivo'])
            al = Aluno(a, b, c)
            al.setID(aluno['id'])

        return al

    def editarRegistro(self):
        al = self.itemSelecionado()
        if al:
            self.gerador.update(al)

    def gerarDeclaracao(self):
        al = self.itemSelecionado()
        Modelo.replaceModel(al, self.gerador.obterCaminho())

    def excluirAluno(self):
        al = self.itemSelecionado()
        self.gerador.deleteById(al.ID)
        self.procurarAluno() # atualiza a tabela