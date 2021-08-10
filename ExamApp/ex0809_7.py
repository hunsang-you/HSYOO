# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 13:45:09 2021

@author: user16
"""

import numpy as np
import matplotlib.pyplot as plt

plt.plot([1,2,3], label ='Line 1', linestyle = '--')
plt.plot([3,2,1], label ='line 2', linewidth = 3)




plt.legend() # 범례 표시
plt.show()