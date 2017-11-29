#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class ToolDemo(QMainWindow):
    def __init__(self):
        super(ToolDemo, self).__init__()
        self.initToolDemo()
    def initToolDemo(self):
        layout = QVBoxLayout()

        tb = self.addToolBar("File")
        new=QAction(QIcon("new.ico"),"new",self)
        tb.addAction(new)
        open=QAction(QIcon("open.png"),"open",self)
        tb.addAction(open)

        save=QAction(QIcon("save.png"),"save",self)
        tb.addAction(save)

        tb.actionTriggered[QAction].connect(self.toolbtnpressed)

        """https://stackoverflow.com/questions/37304684/qwidgetsetlayout-attempting-to-set-qlayout-on-mainwindow-which-already
        You can't set a QLayout directly on the QMainWindow.
        You need to create a QWidget and set it as the central widget on the
        QMainWindow and assign the QLayout to that."""

        wid = QWidget()
        self.setCentralWidget(wid)
        wid.setLayout(layout)

        self.setWindowTitle("toolbar demo")
        self.show()
    def toolbtnpressed(self,a):
        print("pressed tool button is "+a.text())

app = QApplication(sys.argv)
frame = ToolDemo()
app.exec_()
