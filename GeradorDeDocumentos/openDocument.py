#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""

from docx import Document

document = Document()
document.save('new.docx')

f = open('test.docx', 'rb')
document = Document(f)
f.close()
print(f)