# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""
from Aluno import Aluno
from DadosDoAluno import DadosDoAluno
from DadosDeNascimento import DadosDeNascimento
from DadosDaTurma import DadosDaTurma

import sqlite3
import os
import sys


class GeradorDB:

    def connect(self):
        url = os.path.abspath('../bd.db')
        self.conn = sqlite3.connect(url)

    def insert(self, aluno):
        try:
            self.connect()
            param = (aluno.dadosDoAluno.nomeAluno, aluno.dadosDoAluno.nomeDoPai, aluno.dadosDoAluno.nomeDaMae,
                     aluno.dadosDeNascimento.dataDeNascimento, aluno.dadosDeNascimento.cidadeDeNascimento,
                     aluno.dadosDeNascimento.estadoDeNascimento, aluno.dadosDaTurma.serie,
                     aluno.dadosDaTurma.seguimento, aluno.dadosDaTurma.anoLetivo)
            sql = "insert INTO dados_do_aluno (nome_aluno, pai, mae, data, cidade_nascimento, estado_nascimento, " \
                  "serie, seguimento, ano_letivo) values(?, ?, ?, ?, ?,?, ?, ?, ?)"
            self.conn.execute(sql, param)
            self.conn.commit()
            self.close()
            return 1
        except:
            self.close()

    def select(self, nome):
        """"Retorna uma lista de Alunos com o nome relacionado ao paramentro passado"""
        try:
            lista = []
            self.connect()
            sql = "SELECT * FROM dados_do_aluno WHERE nome_aluno LIKE '%{}%'".format(nome)
            cursor = self.conn.execute(sql)
            for i in cursor:
                ID = i[0]
                nome = i[1]
                pai = i[2]
                mae = i[3]
                dataDeNascimento = i[4]
                cidadeDeNascimento = i[5]
                estadoDeNascimento = i[6]
                serie = i[7]
                seguimento = i[8]
                anoLetivo = i[9]
                a = DadosDoAluno(nome, pai, mae)
                b = DadosDeNascimento(dataDeNascimento, cidadeDeNascimento, estadoDeNascimento)
                c = DadosDaTurma(serie, seguimento, anoLetivo)
                al = Aluno(a, b, c)
                al.setID(ID)
                lista.append(al)
            return lista

        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise


    def update(self, aluno):
        pass

    def deleteById(self, aluno):
        pass

    def close(self):
        self.conn.close()


"""a = DadosDoAluno("Anderson Ferreira Câmara", "Adeilton", "Marineide")
b = DadosDeNascimento("07/03/1994", "Maceió", "Alagoas")
c = DadosDaTurma("3º ano", "Ensino Médio", "2018")
al = Aluno(a, b, c)

gerador = GeradorDB()
gerador.insert(al)"""

gerador = GeradorDB()
imprimir = gerador.select('A')
for i in imprimir:
    print(i)