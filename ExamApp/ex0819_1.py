# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:12:17 2021

@author: user16
"""

from pymongo import MongoClient
conn = MongoClient('mongodb://localhost:27017/') # mongodb 접속

# print(conn.list_database_names()) # 설치된 db 명칭(show dbs)

db = conn['test'] # db 반환
collection = db['product'] # 컬렉션 반환
x = collection.find_one()
#print(x)


productname = '냉장고'

query = {'name' : productname}
#query = {'price' : {$gte : 100000}}
result = collection.find(query)
result = collection.find().sort('name', -1) # 내림차순 정렬
#result = collection.find({'price' : {'$gte': 100000, '$lte' : 300000}})
    
    
for item in result :
    print(item['name'], item['price'])
#    print(item)

    
# print(x['name'], x['price'])   

# 비교연산자
# $eq, $ne, $lt, $lte, $gt, $gte
