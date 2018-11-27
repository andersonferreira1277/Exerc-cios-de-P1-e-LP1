#!/usr/bin/env python3
# -*- coding: utf-8-*-
"""
andersonferreira1277@gmail.com
"""

import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

x_list = [1, 3, 6] # Dados
label_list = ['Internet', 'Cartão', 'Combustível'] # Labels
plt.axis('equal') # pizza não ficar oval
plt.pie(x_list, labels=label_list, autopct='%1.f%%')
plt.title('Despesas')
fig = pylab.gcf()
fig.canvas.set_window_title('Despesas')
plt.show()