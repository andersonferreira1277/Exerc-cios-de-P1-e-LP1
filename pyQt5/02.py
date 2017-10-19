import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.myInit()
    def myInit(self):
        self.setWindowTitle("Button")
        self.setGeometry(90, 50, 400, 200)

        myButton = QPushButton("A cute button", self)
        myButton.setToolTip("Click me")
        myButton.move(150, 80)
        self.show()

app = QApplication(sys.argv)
frame = MyWindow()
app.exec_()
