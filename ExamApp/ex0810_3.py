# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 14:17:13 2021

@author: user16
"""

import pymysql


# db 접속
conn = pymysql.connect(host='127.0.0.1', user='bigdata', password='12345678', db = 'mysql', charset='utf8')
cursor = conn.cursor() # 커서 설정


sql = 'select * from 제품'
cursor.execute(sql)  # sql 실행

result = cursor.fetchall() # 모든 레코드를 반환해서 result 변수에 저장
print(len(result))
for item in result :
    print(item[0], item[1], item[2], item[3], item[4])



print('----------------------------------------')
# 고객정보 출력


sql = 'select * from 고객'
cursor.execute(sql)

result = cursor.fetchall()
for customer in result :
     print(customer[0], customer[1], customer[2], customer[3], customer[4], customer[5])



cursor.close()
conn.close() # 접속종료