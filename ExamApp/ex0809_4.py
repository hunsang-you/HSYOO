# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 11:15:53 2021

@author: user16
"""

# 데이터 시각화
import matplotlib.pyplot as plt
import numpy as np

'''
mydata = [100, 120, 130, 145, 165, 180]
plt.plot(mydata)  # y축 데이터
'''

'''
Markers : _ o v ^ < > 
Line : - -- -. :
Color : b g r c m y k w
'''

plt.plot([1,2,3,4], [1, 4, 9, 16], 'rv:')
plt.ylabel('number') # y축 제목
plt.axis([0, 6, 0, 20])  # [xmin, xmax, ymin, ymax]
plt.show() # 그리기 작업의 마지막 코드