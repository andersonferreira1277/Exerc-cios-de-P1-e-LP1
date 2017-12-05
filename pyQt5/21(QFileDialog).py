#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Anderson Ferreira CÂmara - andersonferreira1277@gmail.com
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class DemoFileDialog(QWidget):
    def __init__(self):
        super(DemoFileDialog, self).__init__()
        self.initUI()
    def initUI(self):
        layout = QVBoxLayout()

        self.btn=QPushButton("QFileDialog static method demo")
        self.btn.clicked.connect(self.getfile)
        layout.addWidget(self.btn)

        self.le=QLabel("Hello")
        layout.addWidget(self.le)

        self.btn1=QPushButton("QFileDialog object")
        self.btn1.clicked.connect(self.getfiles)
        layout.addWidget(self.btn1)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)

        self.setLayout(layout)
        self.setWindowTitle("File Dialog demo")
        self.show()

    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/',"Image files(*.jpg *.gif)")
        imagem = QPixmap(fname[0])
        imagem = imagem.scaled(700, 400)
        self.le.setPixmap(imagem)
        """a = self.frameSize()
        print("Tamanho ============" + str(a))"""
    def getfiles(self):
        dlg=QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setNameFilter("Text files (*.txt)")
        if dlg.exec_():
            print("Dlg=============" + str(dlg))
            filenames=dlg.selectedFiles()
            f = open(filenames[0], 'r')
            with f:
                data = f.read()
                self.contents.setText(data)

app = QApplication(sys.argv)
frane = DemoFileDialog()
sys.exit(app.exec_())
