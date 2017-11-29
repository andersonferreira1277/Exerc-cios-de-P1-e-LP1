#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
from PyQt5.QtWidgets import *
class DemoQFontDialog(QWidget):
    def __init__(self):
        super(DemoQFontDialog, self).__init__()
        self.initUI()
    def initUI(self):
        layout = QVBoxLayout()
        self.btn=QPushButton("choose font")
        self.btn.clicked.connect(self.getfont)
        layout.addWidget(self.btn)

        self.le=QLabel("Hello")
        layout.addWidget(self.le)
        self.setLayout(layout)
        self.setWindowTitle("Font Dialog demo")
        self.show()
    def getfont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.le.setFont(font)
app = QApplication(sys.argv)
frame = DemoQFontDialog()
sys.exit(app.exec_())
