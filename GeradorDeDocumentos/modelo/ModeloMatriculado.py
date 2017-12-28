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
import platform, os


class Modelo:

    @staticmethod
    def replaceModel(aluno):
        url = os.path.abspath('modelo/declaracao.docx')
        document = Document(url)

        # Obter data atual da classe
        datastr = DataAtual.getData()
        dataPorExtenso = DataAtual.getDataPorExtenso()
        #

        "Duas lista de mesmo indice, 1 com palavras que existem no documento e a 2 com palavras para substituir no " \
        "documento"
        listaDeProcura = ['nome_aluno', 'pai', 'mae', 'nascimento', 'cty', 'UF', 'serie', 'segmento',
                          'anoLetivo', 'data', 'xtenso']
        listaAluno = [aluno.dadosDoAluno.nomeAluno, aluno.dadosDoAluno.nomeDoPai, aluno.dadosDoAluno.nomeDaMae,
                      aluno.dadosDeNascimento.dataDeNascimento, aluno.dadosDeNascimento.cidadeDeNascimento,
                      aluno.dadosDeNascimento.estadoDeNascimento,
                      aluno.dadosDaTurma.serie, aluno.dadosDaTurma.segmento, aluno.dadosDaTurma.anoLetivo, datastr,
                      dataPorExtenso]

        """for passa pela listaDeProcura, procurando cada item no documento declaracao.docx"""
        for p in document.paragraphs:
            # retirar comentario dos prints para testar o arquivo declaracao.docx
            # print(p.text)
            for k in listaDeProcura:
                if k in p.text:
                    # print('Texto ================================\n'+p.text)
                    # print('FIND!!!!!!!!!!!!!')
                    inline = p.runs
                    # Loop added to work with runs (strings with same style)
                    for i in range(len(inline)):
                        print('Listas: ' + inline[i].text)
                        if k in inline[i].text:
                            text = inline[i].text.replace(k, listaAluno[listaDeProcura.index(k)])
                            inline[i].text = text

        # Salva o arquivo com o nome do Aluno seguido da data atual
        urlDestino = aluno.dadosDoAluno.nomeAluno
        datastr = datastr.replace('/', '-')
        nomeDoArquivo = 'Devidamente matrículado '+urlDestino+' '+datastr+'.docx'

        # Salvar documento
        document.save(os.path.abspath('modelo/'+nomeDoArquivo))

        so = platform.system()
        nomeDoArquivo = os.path.abspath('modelo/'+nomeDoArquivo)
        nomeDoArquivo = '"'+nomeDoArquivo+'"'
        if so == 'Linux':
            # Abre o Libre Office com o parametro do path absoluto do arquivo criado na linha 57

            os.system('libreoffice --writer '+nomeDoArquivo)
        if so == 'Windows':
            # O sistema recebe o parametro do path absoluto do arquivo criado na linha 57, e abre o
            # programa adequado (Provalvelmente o Microsoft Word)

            print('Caminho do arquivo: ' + nomeDoArquivo)
            os.system(nomeDoArquivo)
        return 1
