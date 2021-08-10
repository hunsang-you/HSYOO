# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 15:06:08 2021

@author: user16
"""

from bs4 import BeautifulSoup
import pandas as pd
import urllib.request as ulib

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=zzO70SwM6TUvS%2Fa99iS5LE%2FxGsIpP2GEcjHH6egWD4S75oOLWCBluKc206jvjn6HqcUkIB4DlrkZypj1wI4MMg%3D%3D&returnType=xml&numOfRows=100&pageNo=1&sidoName=%EC%B6%A9%EB%B6%81&ver=1.0'

res = ulib.urlopen(url) # 지정된 주소로부터 xmL을 반환(단순파일)

air =  BeautifulSoup(res, "html.parser") # xml

#print(air)


df1 = [] # 측정소명
df2 = [] # pm10
df3 = [] # pm25
for item in air.findAll("item") : # 반복되는 item 태그로부터 item 변수에 항목을 반환시킨다
    for stationname in item.findAll("stationname") :
      #  print(stationname.string)
      df1.append(stationname.string)
    for pm10value in item.findAll("pm10value"):
      #  print(pm10value.string)
      df2.append(pm10value.string)
    for pm25value in item.findAll("pm25value"):
      df3.append(pm25value.string)
#print(df1)
#print(df2)
#print(df3)

df = pd.DataFrame({'station' : df1, 'pm10' : df2, 'pm25' : df3}) #딕셔너리 형싱
df.head() # 상위 5개 항목 출력
print(df.head())
df.to_csv("test.csv", encoding = 'euc-kr') # csv 형식 파일 저장(구문자로 구성됨)