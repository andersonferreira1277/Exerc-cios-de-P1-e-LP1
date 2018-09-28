#!/usr/bin/env python3
# -*- coding: utf-8-*-
"""
andersonferreira1277@gmail.com
"""

import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2) # número de 0 a 4.8 passo 0.2

# x, y , corTipoDeTraco, x, y , corTipoDeTraco, x, y , corTipoDeTraco
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^') # red dashes, blue squares and green triangles

plt.axis([0, 5, 0, 5**3+1]) # limite x, y
plt.show()
