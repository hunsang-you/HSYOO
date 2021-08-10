# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 10:44:36 2021

@author: user16
"""

tscore = (88, 76, 55, 90, 83)
print(tscore)
print(tscore[2:4])

# Lvalue = rvalue(복합구조)

tu = ("빅데이터", "프로그래밍")
var1, var2 = tu # 2개 이상의 변수에 저장가능
print(var1, var2)

var1, _ = tu
print(var1)