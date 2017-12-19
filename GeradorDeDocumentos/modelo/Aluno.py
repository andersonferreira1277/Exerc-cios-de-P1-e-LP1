# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""

from DadosDoAluno import DadosDoAluno
from DadosDeNascimento import DadosDeNascimento
from DadosDaTurma import DadosDaTurma


class Aluno:

    def __init__(self, dadosDoAluno, dadosDeNascimento, dadosDaTurma):
        """Objeto da Classe DadosDoAluno,  Objeto da Classe DadosDeNascimento, Objeto da Classe DadosDaTurma"""
        self.dadosDoAluno = dadosDoAluno
        self.dadosDeNascimento = dadosDeNascimento
        self.dadosDaTurma = dadosDaTurma
