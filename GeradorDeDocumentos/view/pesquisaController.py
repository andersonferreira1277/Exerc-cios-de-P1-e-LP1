#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""

from PyQt5.QtWidgets import QDialog, QHeaderView
import os
from PyQt5 import uic


class PesquisaController(QDialog):

    def __init__(self, parent=None):
        super(PesquisaController, self).__init__(parent)
        self.initMyUi()

    def initMyUi(self):
        url = os.path.abspath('view/pesquisa.ui')
        uic.loadUi(url, self)

        #self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # expandir até onde
        # for possivel

        self.setWindowTitle('Pesquisar aluno')
        self.show()