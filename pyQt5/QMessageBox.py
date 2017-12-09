#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

def message():
    QMessageBox.critical(None, 'PyQt5 message', "Do you like PyQt5?", QMessageBox.Yes)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    message()