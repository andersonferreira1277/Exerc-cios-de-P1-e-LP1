#!/usr/bin/env python3
# -*- coding: utf-8-*-
"""
andersonferreira1277@gmail.com
"""

import matplotlib.pyplot  as plt

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]


plt.figure(1, figsize=(9, 3))

plt.subplot(131)
barlist = plt.bar(names, values)
barlist[1].set_color('r')
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()