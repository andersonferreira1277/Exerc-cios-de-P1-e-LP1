#-*- coding: latin1-*-
import sys
from PyQt5.QtWidgets import *
from verificar import Verificar

v = Verificar()
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,150,150)
        self.setWindowTitle('Hello QT')
        self.home()
    def home(self):
        label = QLabel(v.teste(), self)
        label.resize(100,100)
        label.move(50,0)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
