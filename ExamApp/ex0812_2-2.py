# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 13:46:08 2021

@author: user16
"""

import pymysql
import sys
from bs4 import BeautifulSoup
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
        self.leArea = QLineEdit()
        self.btnFind = QPushButton('Find')
        self.tbl = QTableWidget(5, 4)
        self.col_head = ['Date', 'pm10', 'pm25', 'o3']
        self.tbl.setHorizontalHeaderLabels(self.col_head)        
        
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        
        layoutTop = QHBoxLayout()
        layoutTop.addWidget(self.leArea)
        layoutTop.addWidget(self.btnFind)
        
        layoutBottom = QVBoxLayout()
        layoutBottom.addWidget(self.tbl)
        layoutBottom.addWidget(self.canvas)
        
        layout = QVBoxLayout() # 외부 레이아웃
        layout.addLayout(layoutTop)
        layout.addLayout(layoutBottom)
        
        self.setLayout(layout) # 윈도우에 레이아웃 설정
        
        self.btnFind.clicked.connect(self.btnFindHandler)

        
        self.setWindowTitle('Table Exam')
        self.setGeometry(10, 30, 500, 600) # 위치와 가로,세로 크기
        self.show() # 윈도우보이기            
        
        
    def btnFindHandler(self) :
        df1 = [] # dateTime
        df2 = [] # pm10

        
        strArea = self.leArea.text() # 한글일 경우 인코딩 필요
        encodeArea = parse.quote_plus(strArea)
        
        url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=zzO70SwM6TUvS%2Fa99iS5LE%2FxGsIpP2GEcjHH6egWD4S75oOLWCBluKc206jvjn6HqcUkIB4DlrkZypj1wI4MMg%3D%3D&returnType=xml&numOfRows=5&pageNo=1&stationName=" + encodeArea + "&dataTerm=DAILY&ver=1.0"
        
        res = ulib.urlopen(url) # 지정된 주소로부터 xmL를 반환(단순 파일)
        air = BeautifulSoup(res,"html.parser") #xmL 파싱
        # self.tbl.setRowCount(5)
        row = 0 # 행번호
        for item in air.findAll("item"): 
            for datatime in item.findAll("datatime") :
              self.tbl.setItem(row, 0, QTableWidgetItem(datatime.string))
              strTime = datatime.string
              df1.append(strTime[11:])
              
            for pm10value in item.findAll("pm10value") :
              self.tbl.setItem(row, 1, QTableWidgetItem(pm10value.string))  
              df2.append(int(pm10value.string))
            for pm25value in item.findAll("pm25value") : 
              self.tbl.setItem(row, 2, QTableWidgetItem(pm25value.string))    
            for o3value in item.findAll("o3value") : 
              self.tbl.setItem(row, 3, QTableWidgetItem(o3value.string))     
            row += 1
        ax = self.fig.add_subplot(111)
        ax.plot(df1, df2)
        
        self.canvas.draw()
        
if __name__=='__main__' :
    app = QApplication(sys.argv)
    ex = MyApp() # 클래스 객체 생성
    sys.exit(app.exec_())        