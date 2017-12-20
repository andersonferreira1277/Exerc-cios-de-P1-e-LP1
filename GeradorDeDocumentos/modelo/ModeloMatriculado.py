#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""
from Aluno import Aluno
from DadosDoAluno import DadosDoAluno
from DadosDeNascimento import DadosDeNascimento
from DadosDaTurma import DadosDaTurma
from DataAtual import DataAtual
from docx import Document


class Modelo:

    @staticmethod
    def replaceModel(aluno):
        document = Document('declaracao.docx')

        # Obter data atual da classe
        datastr = DataAtual.getData()
        dataPorExtenso = DataAtual.getDataPorExtenso()
        #

        "Duas lista de mesmo indice, 1 com palavras que existem no documento e a 2 com palavras para substituir no " \
        "documento"
        listaDeProcura = ['nome_aluno', 'pai', 'mae', 'nascimento', 'cidade', 'estado', 'serie', 'seguimento',
                          'anoLetivo', 'data', 'xtenso']
        listaAluno = [aluno.dadosDoAluno.nomeAluno, aluno.dadosDoAluno.nomeDoPai, aluno.dadosDoAluno.nomeDaMae,
                      aluno.dadosDeNascimento.dataDeNascimento, aluno.dadosDeNascimento.cidadeDeNascimento,
                      aluno.dadosDeNascimento.estadoDeNascimento,
                      aluno.dadosDaTurma.serie, aluno.dadosDaTurma.seguimento, aluno.dadosDaTurma.anoLetivo, datastr,
                      dataPorExtenso]

        """for passa pela listaDeProcura, procurando cada item no documento declaracao.docx"""
        for p in document.paragraphs:
            print(p.text)
            for k in listaDeProcura:
                if k in p.text:
                    print('Texto ================================\n'+p.text)
                    print('FIND!!!!!!!!!!!!!')
                    inline = p.runs
                    # Loop added to work with runs (strings with same style)
                    for i in range(len(inline)):
                        print('Listas: ' + inline[i].text)
                        if k in inline[i].text:
                            text = inline[i].text.replace(k, listaAluno[listaDeProcura.index(k)])
                            inline[i].text = text

        document.save('dest1.docx')
        return 1


a = DadosDoAluno("Anderson Ferreira Câmara", "Adeilton", "Marineide")
b = DadosDeNascimento("07/03/1994", "Maceió", "Alagoas")
c = DadosDaTurma("3º ano", "Ensino Médio", "2018")
al = Aluno(a, b, c)

Modelo.replaceModel(al)