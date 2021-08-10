# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 10:53:54 2021

@author: user16
"""

from bs4 import BeautifulSoup
import pandas as pd
import urllib.request as ulib

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=zzO70SwM6TUvS%2Fa99iS5LE%2FxGsIpP2GEcjHH6egWD4S75oOLWCBluKc206jvjn6HqcUkIB4DlrkZypj1wI4MMg%3D%3D&returnType=xml&numOfRows=100&pageNo=1&stationName=%EC%9A%A9%EB%8B%B4%EB%8F%99&dataTerm=DAILY&ver=1.0'


df1 = [] # 측정소명
df2 = [] # pm10
df3 = [] # pm25



res = ulib.urlopen(url) # 접속해서 xmL 파일 다운로드

air = BeautifulSoup(res, "html.parser") # DOM 구조로 변환

for item in air.findAll("item"): # item 태그에 접근(여러개)
    for pm10value in item.findAll("pm10value"):
       # print(pm10value.string) # 태그 내부의 데이터
        df1.append(pm10value.string)
    for pm25value in item.findAll("pm25value"):
       # print(pm25value.string)
        df2.append(pm25value.string)
    for datatime in item.findAll("datatime"):
       # print(datatime.string)
        df3.append(datatime.string)
        
df = pd.DataFrame({'pm10' : df1, 'pm25' : df2, 'datatime' : df3}) #딕셔너리 형싱
df.head() # 상위 5개 항목 출력
print(df)
df.to_csv("station.csv") # csv 형식 파일 저장(구문자로 구성됨)
        
        
    
