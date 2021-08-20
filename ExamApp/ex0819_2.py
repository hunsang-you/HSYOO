# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:38:49 2021

@author: user16
"""

from pymongo import MongoClient
conn = MongoClient('mongodb://localhost:27017/') # mongodb 접속

# print(conn.list_database_names()) # 설치된 db 명칭(show dbs)

db = conn['test'] # db 반환
collection = db['product'] # 컬렉션 반환

#x =collection.insert_one({'name' : '콘', 'price' : '2000'}) # 1개 입력
#print(x.inserted_id) # insert_one 가능

dicts = [{'name' : '배추', 'price' : 3000}, 
         {'name' : '감자', 'price' : 2000}]

x = collection.insert_many(dicts)  # one 과 many 는 _id 반환 가능
print(x.inserted_ids)