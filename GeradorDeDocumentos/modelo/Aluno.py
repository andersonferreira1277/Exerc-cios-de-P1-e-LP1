# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""


class Aluno:

    def __init__(self, dadosDoAluno, dadosDeNascimento, dadosDaTurma):
        """Objeto da Classe DadosDoAluno,  Objeto da Classe DadosDeNascimento, Objeto da Classe DadosDaTurma"""
        self.ID = str()
        self.dadosDoAluno = dadosDoAluno
        self.dadosDeNascimento = dadosDeNascimento
        self.dadosDaTurma = dadosDaTurma

    def setID(self, ID):
        self.ID = ID

    def __str__(self):
        return 'ID: ' + str(self.ID) +'\nNome do Aluno: ' + self.dadosDoAluno.nomeAluno + '\nPai: ' + \
               self.dadosDoAluno.nomeDoPai + '\nMãe: '+ \
               self.dadosDoAluno.nomeDaMae + '\nData de Nacimento: ' + self.dadosDeNascimento.dataDeNascimento + \
               '\nCidade: ' + self.dadosDeNascimento.cidadeDeNascimento + '\nUF: ' + \
                self.dadosDeNascimento.estadoDeNascimento + '\nSerie: ' + self.dadosDaTurma.serie + '\nsegmento: ' + \
                self.dadosDaTurma.segmento + '\nAno Letivo: ' + str(self.dadosDaTurma.anoLetivo)

    def toList(self):
        lista = []
        lista.append(self.ID)
        lista.append(self.dadosDoAluno.nomeAluno)
        lista.append(self.dadosDoAluno.nomeDoPai)
        lista.append(self.dadosDoAluno.nomeDaMae)
        lista.append(self.dadosDeNascimento.dataDeNascimento)
        lista.append(self.dadosDeNascimento.cidadeDeNascimento)
        lista.append(self.dadosDeNascimento.estadoDeNascimento)
        lista.append(self.dadosDaTurma.serie)
        lista.append(self.dadosDaTurma.segmento)
        lista.append(self.dadosDaTurma.anoLetivo)

        return lista