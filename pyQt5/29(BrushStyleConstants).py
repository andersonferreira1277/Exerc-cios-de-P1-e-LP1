#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#andersonferreira1277@gmail.com

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import *

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.text = "hello world"
        self.setGeometry(250, 50, 800, 610)
        self.setWindowTitle('Draw Demo')
        self.show()
        
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(Qt.red))
        qp.setFont(QFont('Arial', 20))
        qp.drawText(10,50, "hello Python")
        
        qp.setPen(QColor(Qt.blue))
        qp.drawLine(10,100,100,100) #linha Azul
        
        qp.drawRect(10,150,150,100) #retângulo azul
        
        qp.setPen(QColor(Qt.yellow))
        qp.drawEllipse(100,50,100,50) #Elipse amarela
        
        qp.drawPixmap(220,10,QPixmap("python.png")) #imagem
        
        qp.fillRect(200,175,150,100,QBrush(Qt.SolidPattern)) #retângulo preto
        
        qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = Example()
    sys.exit(app.exec_())