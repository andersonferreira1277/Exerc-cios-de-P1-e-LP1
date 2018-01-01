# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""
from modelo.Aluno import Aluno
from modelo.DadosDoAluno import DadosDoAluno
from modelo.DadosDeNascimento import DadosDeNascimento
from modelo.DadosDaTurma import DadosDaTurma

import sqlite3
import os
import sys


class GeradorDB:

    def connect(self):
        try:
            url = os.path.abspath('bd.db')
            self.conn = sqlite3.connect(url)
        except:
            print("Erro ao conectar ao banco de dados:", sys.exc_info()[0])
            raise

    def insert(self, aluno):
        """Recebe um Objeto Aluno e grava no Banco de dados"""
        try:
            self.connect()
            param = (aluno.dadosDoAluno.nomeAluno, aluno.dadosDoAluno.nomeDoPai, aluno.dadosDoAluno.nomeDaMae,
                     aluno.dadosDeNascimento.dataDeNascimento, aluno.dadosDeNascimento.cidadeDeNascimento,
                     aluno.dadosDeNascimento.estadoDeNascimento, aluno.dadosDaTurma.serie,
                     aluno.dadosDaTurma.segmento, aluno.dadosDaTurma.anoLetivo)
            sql = "insert INTO dados_do_aluno(nome_aluno, pai, mae, data, cidade_nascimento, estado_nascimento, " \
                  "serie, segmento, ano_letivo) values(?, ?, ?, ?, ?,?, ?, ?, ?)"
            self.conn.execute(sql, param)
            self.conn.commit()
            linhas = int(self.conn.total_changes)
            self.close()
            return linhas
        except:
            self.close()
            print("Erro ao inserir dados:", sys.exc_info()[0])
            raise

    def select(self, sql):
        """"Retorna uma lista de Alunos com o nome relacionado ao paramentro passado"""
        try:
            self.connect()
            lista = []
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
                segmento = i[8]
                anoLetivo = i[9]
                a = DadosDoAluno(nome, pai, mae)
                b = DadosDeNascimento(dataDeNascimento, cidadeDeNascimento, estadoDeNascimento)
                c = DadosDaTurma(serie, segmento, anoLetivo)
                al = Aluno(a, b, c)
                al.setID(ID)
                lista.append(al)
            self.close()
            return lista

        except:
            self.close()
            print("Erro ao executar select:", sys.exc_info()[0])
            raise

    def update(self, aluno):
        """Recebe um objeto Aluno com seu ID já setado pelo banco de dados, realiza o update dos dados e
        retorna o valor de linhas alteradas"""
        try:
            self.connect()
            sql = "UPDATE dados_do_aluno " \
                  "SET nome_aluno= ?, pai= ?, mae= ?, data= ?,cidade_nascimento=?," \
                  "estado_nascimento=?, serie=?, segmento=?, ano_letivo=? WHERE id=?;"

            param = (aluno.dadosDoAluno.nomeAluno, aluno.dadosDoAluno.nomeDoPai, aluno.dadosDoAluno.nomeDaMae,
                     aluno.dadosDeNascimento.dataDeNascimento, aluno.dadosDeNascimento.cidadeDeNascimento,
                     aluno.dadosDeNascimento.estadoDeNascimento, aluno.dadosDaTurma.serie,
                     aluno.dadosDaTurma.segmento, aluno.dadosDaTurma.anoLetivo, aluno.ID)

            self.conn.execute(sql, param)
            self.conn.commit()
            linhas = int(self.conn.total_changes)
            self.close()
            return linhas
        except:
            self.close()
            print("Erro ao fazer update do registro:", sys.exc_info()[0])
            raise

    def deleteById(self, idAluno):
        """Recebe um ID e tenta deletar do Banco de Dados.
        Retorna a quatidade de linhas alteradas"""
        try:
            self.connect()
            sql = 'DELETE FROM dados_do_aluno WHERE id=?;'
            param = (idAluno, )
            self.conn.execute(sql, param)
            self.conn.commit()
            linhas = int(self.conn.total_changes)
            self.close()
            return linhas
        except:
            self.close()
            print("Erro ao deletar pelo ID:", sys.exc_info()[0])
            raise

    def close(self):
        self.conn.close()

    def selectNomeLike(self, nome):
        sql = "SELECT * FROM dados_do_aluno WHERE nome_aluno LIKE '%{}%'".format(nome)
        return self.select(sql)

    def selectNomeIgual(self, nome):
        sql = "SELECT * FROM dados_do_aluno WHERE nome_aluno LIKE '{}'".format(nome)
        return self.select(sql)

    def obterCaminho(self):
        """Retorna string com o caminho para salvar o arquivo"""
        url = str()
        try:
            self.connect()
            sql = 'SELECT caminho FROM config WHERE id=1;'
            cursor = self.conn.execute(sql)
            for i in cursor:
                url = '"'+i[0]+'"'
        except:
            self.close()
            print("Erro ao obter caminho para salvar arquivo:", sys.exc_info()[0])
            raise

        return url

    def salvarCaminho(self, caminho):
        try:
            sql = "UPDATE config SET caminho='{}' WHERE id=1;".format(caminho)
            self.connect()
            self.conn.execute(sql)
            self.conn.commit()
            self.close()
        except:
            self.close()
            print("Erro ao inserir caminho para salvar arquivo:", sys.exc_info()[0])
            raise