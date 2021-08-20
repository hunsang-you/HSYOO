# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 14:05:45 2021

@author: user16
"""

import pymysql
import sys
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import font_manager, rc

class MyApp(QWidget) : # 정의
    def __init__(self) :
        super().__init__()  # 부모클래스 생성자 호출
        self.initUI()
        
    def initUI(self) :
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.conn = pymysql.connect(host='127.0.0.1', user='bigdata', password='12345678', db = 'mysql', charset='utf8')
        self.cursor = self.conn.cursor() # 커서 설정
        

        font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
        rc('font', family=font_name)
        
        self.tbl = QTableWidget(20, 11)
        self.col_head = ['Date', 'Temp1', 'Temp2', 'Temp3', 'Temp4', 'Temp5', 'Temp6', 'Temp7', 'Temp8', 'Temp9', 'Temp10',]
        self.tbl.setHorizontalHeaderLabels(self.col_head)        
        
        self.leEdit = QLineEdit()
        
        self.dbupdate()
        

        

        
        layoutTbl = QVBoxLayout()
        layoutTbl.addWidget(self.tbl)
        
        layoutSelect = QHBoxLayout()
        layoutSelect.addWidget(self.leEdit)
        
        layoutGraph = QVBoxLayout()
        layoutGraph.addWidget(self.canvas)
        
        layout = QVBoxLayout() # 외부 레이아웃
        layout.addLayout(layoutTbl)
        layout.addLayout(layoutSelect)
        layout.addLayout(layoutGraph)
        
        self.setLayout(layout) # 윈도우에 레이아웃 설정
                
        self.setWindowTitle('sensor Exam')
        self.setGeometry(10, 30, 1200, 650) # 위치와 가로,세로 크기
        self.show() # 윈도우보이기     
        


    
    def dbupdate(self) :
        self.df0 = [] # 시간
        self.df1 = [] # 온도1
        
        
        sql = 'select * from tblsensor order by ts_date desc'
        self.cursor.execute(sql)  # sql 실행
        
        result = self.cursor.fetchall() # 모든 레코드를 반환해서 result 변수에 저장
        row = 0 # 행 처리용
        for item in result :
            for col in range(11) :
                self.tbl.setItem(row, col, QTableWidgetItem(str(item[col])))
            strtime = item[0]
            self.df0.append(strtime[11:]) # 시간데이터
            self.df1.append(item[1]) # 첫번째 센서데이터
            row += 1
        self.df0.reverse()
        self.df1.reverse()
        self.graph1()
        
    def graph1(self):
        self.fig.clear()
         
        
        ax1 = self.fig.add_subplot(111)
     
        ax1.clear() # 그래프 영역 초기화(subplot 각각 필요)
        ax1.bar(self.df0, self.df1)
        '''
        ax2 = self.fig.add_subplot(212)
        ax2.clear() # 그래프 영역 초기화(subplot 각각 필요)
        ax2.plot(df1, df3)
        '''
        
        
        self.canvas.draw()
        
    

        

        

        
if __name__=='__main__' :
    app = QApplication(sys.argv)
    ex = MyApp() # 클래스 객체 생성
    sys.exit(app.exec_())  