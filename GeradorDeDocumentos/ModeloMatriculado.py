#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""
from aluno import Aluno
from docx import Document


class Modelo:

    @staticmethod
    def replace_string(aluno):
        document = Document('declaracao.docx')
        listaDeProcura = ['nome_aluno', '{pai}', '{mae}', '{nascimento}', '{cidade}', '{estado}']
        listaAluno = [aluno.nomeAluno, aluno.nomeDoPai, aluno.nomeDaMae, aluno.dataDeNascimento,
                      aluno.cidadeDeNascimento, aluno.estadoDeNascimento]
        """for passa pela listaDeProcura, procurando cada item no documento declaracao.docx"""
        for p in document.paragraphs:
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


a = Aluno("Anderson Ferreira Câmara", "Adeilton", "Marineide", "07/03/1994",
          "Maceió", "Alagoas")

Modelo.replace_string(a)