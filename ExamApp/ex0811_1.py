# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 09:44:49 2021

@author: user16
"""

import pymysql


# db접속
conn = pymysql.connect(host = '127.0.0.1', user = 'bigdata', password = '12345678', db = 'mysql', charset = 'utf8')
cursor = conn.cursor() # 커서 설정

sql = "insert into 제품 values (%s, %s, %s, %s, %s)"
cursor.execute(sql, ('p08', '컴퓨터', 500, 5000, '아이비엠'))

cursor.close()
conn.commit() # insert. update, delete 에 필요함
conn.close()