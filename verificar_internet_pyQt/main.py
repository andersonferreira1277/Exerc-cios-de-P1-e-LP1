#-*- coding: latin1-*-
import sys
from PyQt4 import QtGui, QtCore
from verificar import Verificar

v = Verificar()
class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,150,150)
        self.setWindowTitle('Hello QT')
        self.home()
    def home(self):
        label = QtGui.QLabel(v.teste(), self)
        label.resize(100,100)
        label.move(50,0)
        self.show()
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    while 1:
        sys.exit(app.exec_())
run()
