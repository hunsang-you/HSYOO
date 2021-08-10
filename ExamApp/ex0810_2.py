# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 11:47:26 2021

@author: user16
"""
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request as ulib
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem


class MyApp(QWidget) : # 정의
    def __init__(self) :
        super().__init__()  # 부모클래스 생성자 호출
        url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=zzO70SwM6TUvS%2Fa99iS5LE%2FxGsIpP2GEcjHH6egWD4S75oOLWCBluKc206jvjn6HqcUkIB4DlrkZypj1wI4MMg%3D%3D&returnType=xml&numOfRows=100&pageNo=1&stationName=%EC%9A%A9%EB%8B%B4%EB%8F%99&dataTerm=DAILY&ver=1.0'
        
        res = ulib.urlopen(url)
        
        
        self.air = BeautifulSoup(res, "html.parser")
        
        self.df1 = []
        self.df2 = []
        self.df3 = []
        
        self.initUI()
        
        
    def initUI(self) :
        
        
        cnt = len(air.findAll("item"))  # 행의 갯수
        self.tbl = QTableWidget(cnt, 3, self)
        self.tbl.setGeometry(30, 30, 600, 400)
        self.col_head = ['station', 'pm10', 'pm25']
        self.tbl.setHorizontalHeaderLabels(self.col_head)        
        
        
        #self.tbl.setItem(0,0, QTableWidgetItem('data1'))
        #self.tbl.setItem(0,1, QTableWidgetItem('data2'))
        #self.tbl.setItem(5,10, QTableWidgetItem('data3'))
        #1 ~ 59 을 순서대로 테이블에 출력
        
        
        row = 0 # 행번호
        for item in self.air.findAll("item"): # 0 ~ 30까지 반복
            for stationName in item.findAll("stationName") :
              self.tbl.setItem(row, 0, QTableWidgetItem(stationName.string))
            for pm10value in item.findAll("pm10value") :
              self.tbl.setItem(row, 1, QTableWidgetItem(pm10value.string))  
            for pm25value in item.findAll("pm25value") : 
              self.tbl.setItem(row, 2, QTableWidgetItem(pm25value.string))    
            row += 1
            
            
        
        self.setWindowTitle('Table Exam')
        self.setGeometry(50, 50, 500, 300) # 위치와 가로,세로 크기
        self.show() # 윈도우보이기
        
if __name__=='__main__' :
    app = QApplication(sys.argv)
    ex = MyApp() # 클래스 객체 생성
    sys.exit(app.exec_())
        