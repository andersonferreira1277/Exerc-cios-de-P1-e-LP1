#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#andersonferreira1277@gmail.com

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QTextEdit, QStatusBar, QPushButton, QApplication


class StatusDemo(QMainWindow):

    def __init__(self):
        super(StatusDemo, self).__init__()
        self.initUi()

    def initUi(self):
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("show")
        file.addAction("add")
        file.addAction("remove")
        file.triggered[QAction].connect(self.processTrigger)
        self.setCentralWidget(QTextEdit())
        self.statusBar = QStatusBar()
        self.b = QPushButton("click here")
        self.setWindowTitle("QStatusBar Example")
        self.setStatusBar(self.statusBar)
        self.show()

    def processTrigger(self, q):
        if (q.text()=="show"):
            self.statusBar.showMessage(q.text()+" is clicked",2000)
        if q.text()=="add":
            self.statusBar.addWidget(self.b)
        if q.text()=="remove":
            self.statusBar.removeWidget(self.b)
            self.statusBar.show()


if __name__ == '__main':
    app = QApplication(sys.argv)
    frame = StatusDemo()
    sys.exit(app.exec_())