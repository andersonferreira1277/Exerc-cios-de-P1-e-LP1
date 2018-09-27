#!/usr/bin/env python3
"""
andersonferreira1277@gmail.com
"""

from os import listdir
from os.path import getsize, isfile, join, abspath, dirname
import matplotlib.pyplot as plt


a = dirname(abspath(__file__))
lista = listdir(a)
listaDeDados = []
for i in lista:
    if isfile(join(a, i)):
        listaDeDados.append(getsize(join(a, i))/1024)
        print(str(i)+ " - " +str(getsize(join(a, i))/1024) + " Kbytes")

fig, ax = plt.subplots()
ax.hist(listaDeDados, orientation='horizontal')
plt.show()