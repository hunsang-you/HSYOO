# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 11:50:47 2021

@author: user16
"""

# numpy 활용 그래프
import matplotlib.pyplot as plt
import numpy as np

'''
#동일 공간에 그리기

t = np.arange(0.0, 5.0, 0.2)
plt.plot(t, t, 'r--', t, t**2, 'b^', t, t**3, 'g')
'''
# 분리된 공간에 그리기
# X축에 각각의 그래프 제목 표시(t, t**2, t**3)
plt.figure(figsize =(9, 3))
plt.subplot(1, 3, 1) #1행 3열의 첫번째
plt.xlabel('y=t')
plt.plot(t, t, 'r--')


plt.subplot(1, 3, 2)
plt.xlabel('y=t**2')
plt.plot(t, t**2, 'b^')


plt.subplot(1, 3, 3)\

plt.plot(t, t**3, 'g')
plt.xlabel('y=t**3')
plt.suptitle('Categorical Plotting')

plt.show()
