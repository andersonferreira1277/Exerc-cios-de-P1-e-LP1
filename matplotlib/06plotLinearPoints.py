#!/usr/bin/env python3
# -*- coding: utf-8-*-
"""
andersonferreira1277@gmail.com
"""
import numpy
from matplotlib import pyplot

x1 = numpy.arange(10)
x = ['Pri', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Set', 'oit', 'Nov', 'Dec']
y = numpy.array([5,3,4,2,7,5,4,6,3,2])

fig = pyplot.figure()
ax = fig.add_subplot(111)
ax.set_ylim(0,10)
pyplot.plot(x,y)
for i,j in zip(x1,y):
    ax.annotate(str(j),xy=(i,j+0.2))

pyplot.show()