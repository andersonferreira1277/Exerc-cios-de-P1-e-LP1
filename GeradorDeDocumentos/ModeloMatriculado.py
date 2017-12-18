#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""

from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

document = Document()
paragraph = document.add_paragraph()
paragraph = document.add_picture('logo.jpg', Inches(1.00))
paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
document.add_paragraph('Alguma coisa')
document.save('Demo.docx')