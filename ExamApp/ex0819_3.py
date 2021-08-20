# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 11:15:57 2021

@author: user16
"""
from pymongo import MongoClient
import sys
import pandas as pd
import urllib.request as ulib
import urllib.parse as parse
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MyApp(QWidget) : # 정의
    def __init__(self) :
        super().__init__()  # 부모클래스 생성자 호출
        self.initUI()
        

        
    def initUI(self) :
        
        self.leArea = QLineEdit(self)
        self.leArea.setGeometry(10, 30, 200, 30)
        
        self.btnFind = QPushButton("Find", self)
        self.btnFind.setGeometry(220, 30, 200, 30)
        
        self.tbl = QTableWidget(self)
        self.tbl.setGeometry(10, 70, 500, 300)
        self.tbl.setColumnCount(2)
        self.col_head = ['name', 'price']
        self.tbl.setHorizontalHeaderLabels(self.col_head)
        
        self.btnFind.clicked.connect(self.btnFindHandler)
        
        
        
        self.setWindowTitle('Table Exam')
        self.setGeometry(50, 50, 600, 400) # 위치와 가로,세로 크기
        self.show() # 윈도우보이기        
        
        
    def btnFindHandler(self) :
        conn = MongoClient('mongodb://localhost:27017/') # mongodb 접속
        db = conn['test'] # db 반환
        collection = db['product'] # 컬렉션 반환
        
        findstr = self.leArea.text()
        if len(findstr) > 0 :
            query = {'name' : findstr}
            cnt =  collection.find(query).count() # 조회결과 행수
        else :
            query = {}
            cnt =  collection.find().count()        
        #라인에디트에 문자열이 있는지확인
        result = collection.find(query) # 조건 검색



        
        if cnt > 0 :
            self.tbl.setRowCount(cnt)
            row = 0 # 행번호
        
        for item in result : 
            self.tbl.setItem(row, 0, QTableWidgetItem(item['name']))
            self.tbl.setItem(row, 1, QTableWidgetItem(str(int(item['price']))))
            row += 1
        
        else :
            self.tbl.setRowCount(cnt)
                
        result = collection.find() # 전체 검색
        
        
        
        #cnt가 0일 경우와 그렇지 않을경우 분리
        
        self.tbl.setRowCount(cnt)
        row = 0 # 행번호
        
        for item in result : 
            self.tbl.setItem(row, 0, QTableWidgetItem(item['name']))
            self.tbl.setItem(row, 1, QTableWidgetItem(str(int(item['price']))))
            row += 1
        
        
          # self.tbl.setItem(row, 0, QTableWidgetItem(datatime.string))
        
          #  row += 1
        
        
if __name__=='__main__' :
    app = QApplication(sys.argv)
    ex = MyApp() # 클래스 객체 생성
    sys.exit(app.exec_())