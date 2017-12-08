#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#andersonferreira1277@gmail.com

import sys
from PyQt5 import QtSql
from PyQt5.QtWidgets import *

def createDB():
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('sports.db')
    if not db.open():
        QMessageBox.critical(None, "Cannot open database","Unable to establish a database connection.\n"+
                                                                           "This example needs SQLite support."+
                                                                           " Please read the Qt SQL driver documentation"+
                                                                           " for information how to build it.\n\nClick Cancel to exit.",
                                                                           QMessageBox.Cancel)
        return False
    query = QtSql.QSqlQuery()
    query.exec_("create table sportsmen(id int primary key, "+
                "firstname varchar(20), lastname varchar(20))")
    query.exec_("insert into sportsmen values(101, 'Roger', 'Federer')")
    query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo')")
    query.exec_("insert into sportsmen values(103, 'Ussain', 'Bolt')")
    query.exec_("insert into sportsmen values(104, 'Sachin', 'Tendulkar')")
    query.exec_("insert into sportsmen values(105, 'Saina', 'Nehwal')")
    QMessageBox.information(None, "Informação", "Registro salvo no banco de dados", QMessageBox.Ok)
    return True
if __name__ == '__main__':
    app = QApplication(sys.argv)
    createDB()