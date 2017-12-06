#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""
import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSplitter, QApplication, QTextEdit, QStyleFactory, QFrame
from PyQt5.QtCore import *

class DemoQSplitter(QWidget):
    def __init__(self):
        super(DemoQSplitter, self).__init__()
        self.initUI()
    def initUI(self):
        hbox = QHBoxLayout(self)
        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)
        
        splitter1 = QSplitter(Qt.Horizontal)
        textedit=QTextEdit()
        splitter1.addWidget(topleft)
        splitter1.addWidget(textedit)
        splitter1.setSizes([100,200])
        
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        hbox.addWidget(splitter2)
        
        self.setLayout(hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter demo')
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = DemoQSplitter()
    sys.exit(app.exec_())