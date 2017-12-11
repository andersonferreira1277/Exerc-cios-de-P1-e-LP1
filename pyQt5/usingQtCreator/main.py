#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#andersonferreira1277@gmail.com

import sys
from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWindow(Ui_MainWindow):
    def __init__(self, qMain):
        Ui_MainWindow.__init__(self)
        self.setupUi(qMain)
        self.pushButton.clicked.connect(self.mudarTexto)
    
    def mudarTexto(self):
        self.label.setText("Anderson")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    qMain = QMainWindow()    
    frame = MyWindow(qMain)
    qMain.show()
    sys.exit(app.exec_())
        