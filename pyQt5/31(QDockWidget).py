#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#andersonferreira1277@gmail.com

import sys
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QDockWidget, QListWidget, QTextEdit, QApplication
from PyQt5.QtCore import *

class DockDemo(QMainWindow):
    def __init__(self):
        super(DockDemo, self).__init__()
        self.initUi()
    def initUi(self):
        layout = QHBoxLayout()
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("save")
        file.addAction("quit")
        self.items = QDockWidget("Dockable", self)
        self.listWidget = QListWidget()
        self.listWidget.addItem("item1")
        self.listWidget.addItem("item2")
        self.listWidget.addItem("item3")
        self.items.setWidget(self.listWidget)
        self.items.setFloating(False)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)
        self.setLayout(layout)
        self.setWindowTitle("Dock demo")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = DockDemo()
    sys.exit(app.exec_())