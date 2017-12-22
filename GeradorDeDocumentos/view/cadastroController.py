#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""

from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
import os


class ViewCadastro(QDialog):

    def __init__(self, parent=None):
        super(ViewCadastro, self).__init__(parent)
        self.initCadastro()

    def initCadastro(self):
        url = os.path.abspath('view/cadastro.ui')
        uic.loadUi(url, self)

        self.show()