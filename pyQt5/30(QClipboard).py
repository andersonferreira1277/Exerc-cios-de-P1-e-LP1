#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#andersonferreira1277@gmail.com

import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton,\
    QApplication
from PyQt5.QtGui import QClipboard

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initIU()
    def initIU(self):
        layout = QVBoxLayout()
        
        self.textEdit1 = QTextEdit()
        button1 = QPushButton("Copy")
        button1.clicked.connect(self.copy)
        
        self.textEdit2 = QTextEdit()
        self.textEdit2.setReadOnly(True)
        button2 = QPushButton("Paste")
        button2.clicked.connect(self.paste)
        
        layout.addWidget(self.textEdit1)
        layout.addWidget(button1)
        layout.addWidget(self.textEdit2)
        layout.addWidget(button2)
        
        self.qClip = QApplication.clipboard()
        
        self.setLayout(layout)
        self.setWindowTitle("Cpoy and Paste test")
        self.show()
        
    def copy(self):
        self.qClip.setText(self.textEdit1.toPlainText())
        print(self.qClip)
    def paste(self):
        self.textEdit2.setText(self.qClip.text())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MyWindow()
    sys.exit(app.exec_())