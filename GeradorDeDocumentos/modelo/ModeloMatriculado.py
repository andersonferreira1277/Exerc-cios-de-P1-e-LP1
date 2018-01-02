#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""
import subprocess
from modelo.DataAtual import DataAtual
from docx import Document
import platform, os


class Modelo:

    @staticmethod
    def replaceModel(aluno, caminho):
        url = os.path.abspath('modelo/declaracao.docx')
        document = Document(url)

        # Obter data atual da classe
        datastr = DataAtual.getData()
        dataPorExtenso = DataAtual.getDataPorExtenso()

        "Duas lista de mesmo indice, 1 com palavras que existem no documento e a 2 com palavras para " \
        "substituir no documento"

        # Existe umas exceção para usar "no" antes da serie, se for alfabetização usasse "na"
        comserie = 'na' if aluno.dadosDaTurma.serie == 'Alfabetização' else 'no'

        listaDeProcura = ['nome_aluno', 'pai', 'mae', 'nascimento', 'cty', 'UF', 'comserie',  'serie', 'segmento',
                          'anoLetivo', 'data', 'xtenso']
        listaAluno = [aluno.dadosDoAluno.nomeAluno, aluno.dadosDoAluno.nomeDoPai, aluno.dadosDoAluno.nomeDaMae,
                      aluno.dadosDeNascimento.dataDeNascimento, aluno.dadosDeNascimento.cidadeDeNascimento,
                      aluno.dadosDeNascimento.estadoDeNascimento, comserie,
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
                        # print('Listas: ' + inline[i].text)
                        if k in inline[i].text:
                            text = inline[i].text.replace(k, listaAluno[listaDeProcura.index(k)])
                            inline[i].text = text

        # Salva o arquivo com o nome do Aluno seguido da data atual
        urlDestino = aluno.dadosDoAluno.nomeAluno
        datastr = datastr.replace('/', '-')
        nomeDoArquivo = 'Devidamente matrículado '+urlDestino+' '+datastr+'.docx'

        # juntando path recebido no parametro com o nome do arquivo e adicionando ""
        caminho = caminho.replace('"','')
        caminho = os.path.join(caminho, nomeDoArquivo)

        # Salvar documento
        document.save(caminho)
        caminho = '"' + caminho + '"' # adicionando "" para poder abrir

        so = platform.system()
        if so == 'Linux':
            caminho = caminho.replace('"', '') # comando não recebe ""
            subprocess.call(['xdg-open', caminho])
        if so == 'Windows':
            os.startfile(caminho) # usa biblioteca do sistema para abrir o arquivo
        return 1
