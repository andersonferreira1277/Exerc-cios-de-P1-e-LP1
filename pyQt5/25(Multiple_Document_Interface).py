#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""
import sys
from PyQt5.QtWidgets import *

class DemoMultipleDocumentInterface(QMainWindow):
    count=0
    def __init__(self):
        super(DemoMultipleDocumentInterface, self).__init__()
        self.initIU()
    def initIU(self):
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        
        bar=self.menuBar()
        file=bar.addMenu("File")
        file.addAction("New")
        file.addAction("cascade")
        file.addAction("Tiled")
        file.triggered[QAction].connect(self.windowaction)
        
        self.setWindowTitle("MDI demo")
        self.show()
    def windowaction(self, q):
        if q.text()=="New":
            print("New")
            self.count=self.count+1
            sub=QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("subwindow"+str(self.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        if q.text()=="cascade":
            print("Cascade")
            self.mdi.cascadeSubWindows()
        if q.text()=="Tiled":
            print("Tiled")
            self.mdi.tileSubWindows()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = DemoMultipleDocumentInterface()
    sys.exit(app.exec_())