# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 10:58:56 2021

@author: user16
"""

# Dictionary(딕셔너리)
# Key 와 Value 조합


fruit = {'사과' : 1000, '배' : 2000, '포도' : 1500} # 3개
print(fruit)
print(fruit['사과']) # Key 를 입력하여 Value를 받

print('사과' in fruit.keys()) # 사과 존재 여부 반환
print(1200 in fruit.values()) # value 존재 여부 반환

for k, v in fruit.items() :
    print(k, v)