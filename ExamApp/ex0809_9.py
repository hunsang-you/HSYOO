# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 14:17:18 2021

@author: user16
"""

import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(10, 3, 20000) # 평균10, 표준편차3, 개수 200인 정규분포

plt.hist(data, bins=30, colors='green') # 30개의 구간

plt.show()

