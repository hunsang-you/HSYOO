# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 14:03:20 2021

@author: user16
"""

import matplotlib.pyplot as plt
import numpy as np

names = ['group_a', 'groub_b', 'groub_c']
values = [1, 10, 100]


plt.figure(figsize=(9,3)) #  가로세로 9인치, 3인
plt.subplot(1, 3, 1) # 1행 3열의 첫번째
plt.bar(names, values) # 세로 막대그래프


plt.subplot(1, 3, 2)
plt.scatter(names, values) # 산정도


plt.subplot(1, 3, 3)


plt.show()