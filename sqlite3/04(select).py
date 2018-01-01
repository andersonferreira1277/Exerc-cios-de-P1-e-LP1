#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
andersonferreira1277@gmail.com
"""

import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
url = ('1', )
cursor = conn.execute("SELECT id, name, address, salary FROM COMPANY WHERE ID=?", url)
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")
print("Operatidone successfully")
conn.close()