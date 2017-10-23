#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initMyWindow()

    def initMyWindow(self):
        myGrid = QGridLayout()
        self.setLayout(myGrid)

        blabels = [["7","8","9","/"],
                   ["4","5","6","*"],
                   ["1","2","3","-"],
                   ["0",".","=","+"]]
        list_buttons = []
        for i in range(4):
            for j in range(4):
                button = QPushButton(blabels[i][j])
                list_buttons.append(button)
                print("Valor de texto:", list_buttons[list_buttons.index(button)].text())
                list_buttons[list_buttons.index(button)].clicked.connect(lambda: self.doThis(self.sender()))
                myGrid.addWidget(list_buttons[len(list_buttons)-1], i, j)
                print(list_buttons[len(list_buttons) - 1])

        myField = QLineEdit()
        myGrid.addWidget(myField, 4, 0, 1, 4) #Linha, coluna, linhas ocupadas, colunas ocupadas

        self.move(90, 50)
        self.setWindowTitle("Layout")
        self.show()

    def doThis(self, texto):
        print("Hello World!!!")
        print(texto.text())

app = QApplication(sys.argv)
frame = MyWindow()
app.exec_()
