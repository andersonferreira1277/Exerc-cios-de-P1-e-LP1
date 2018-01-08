#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""
import sys
from PyQt5.QtWidgets import *

class DemoDragAndDrop(QComboBox):
    def __init__(self, title, parent):
        super(DemoDragAndDrop, self).__init__(parent)
        self.setAcceptDrops(True)
    def dragEnterEvent(self, e):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()
    def dropEvent(self, e):
        self.addItem(e.mimeData().text())

class Example(QWidget): #
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
    def initUI(self):
        lo=QFormLayout()
        lo.addRow(QLabel("Type some text in textbox and drag it into combo box"))
        
        edit = QLineEdit()
        edit.setDragEnabled(True)
        com = DemoDragAndDrop("Button", self)
        lo.addRow(edit,com)
        
        self.setLayout(lo)
        self.setWindowTitle('Simple drag & drop')
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Frame = Example()
    sys.exit(app.exec_())