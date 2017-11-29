#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
from PyQt5.QtWidgets import *

class MenuDemo(QMainWindow):
    def __init__(self):
        super(MenuDemo, self).__init__()
        self.initMenuDemo()
    def initMenuDemo(self):
        layout = QHBoxLayout()

        bar=self.menuBar()
        file=bar.addMenu("File")
        file.addAction("New")

        save=QAction("Save",self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)

        edit=file.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("paste")

        quit=QAction("Quit",self)

        file.addAction(quit)
        file.triggered[QAction].connect(self.processtrigger)
        
        self.setLayout(layout)
        self.setWindowTitle("menu demo")
        self.show()
    def processtrigger(self,q):
        print (q.text()+" is triggered")

app = QApplication(sys.argv)
frame = MenuDemo()
app.exec_()
