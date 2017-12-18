#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
https://stackoverflow.com/questions/34779724/python-docx-replace-string-in-paragraph-while-keeping-style
"""
from docx import Document

def replace_string():
    document = Document('declaracao.docx')
    for p in document.paragraphs:
        if '{aluno}' in p.text:
            inline = p.runs
            # Loop added to work with runs (strings with same style)
            for i in range(len(inline)):
                print("Inline===============" + inline[i].text)
                if '{aluno}' in inline[i].text:
                    text = inline[i].text.replace('{aluno}', 'Anderson Ferreira Câmara')
                    inline[i].text = text
            print(p.text)

    document.save('dest1.docx')
    return 1

replace_string()