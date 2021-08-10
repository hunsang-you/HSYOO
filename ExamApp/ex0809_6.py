# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 13:28:10 2021

@author: user16
"""

import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0.0, 5.0) # 균일간격 점생성
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi*x1) * np.exp(-x1) # damping
y2 = np.cos(2 * np.pi*x2)   # cos 그래프

plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'bo-')



plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')