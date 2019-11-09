#!/usr/bin/env python3
# -*- coding: utf-8-*-
"""
andersonferreira1277@gmail.com
"""

import matplotlib.pyplot as plt

plt.plot(['01/2018', '02/2018', '03/2018', '04/2018'], [500.15, 700.5, 850.56, 450.56] )
plt.ylabel('some numbers') # legenda do eixo y
plt.xlabel("values") # legenda do eixo x
plt.title("Histórico de saldo")
# plt.savefig('meuGrafico.png') # salvar figura
plt.show()