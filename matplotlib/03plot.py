#!/usr/bin/env python3
# -*- coding: utf-8-*-
"""
andersonferreira1277@gmail.com
"""

import matplotlib.pyplot as plt
# primeira lista do eixo x, segunda eixo y. 'ro' add pontos ao grafico
plt.plot([6, 12, 14, 24], [1, 4, 9, 16], 'ro')

plt.axis([6,24,1,16]) # comando limita os valores maximo e minimo do eixo x y [xmin, xmax, ymin, ymax]
plt.ylabel('some numbers') # legenda do eixo y
plt.xlabel("values") # legenda do eixo x
plt.title("Anderson")
plt.show()