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
        
        self.strArea = ['종로구', '용암동', '용담동']
        self.cboArea = QComboBox()
        self.cboArea.addItems(self.strArea)
        #self.cboArea.addItem('종로구')
        #self.cboArea.addItem('용암동')
        #self.cboArea.addItem('용담동')
        
        
        
        self.tbl = QTableWidget(10, 4)
        self.col_head = ['Date', 'pm10', 'pm25', 'o3']
        self.tbl.setHorizontalHeaderLabels(self.col_head)        
        
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        
        layoutTop = QHBoxLayout()
        layoutTop.addWidget(self.leArea)
        layoutTop.addWidget(self.cboArea)
        layoutTop.addWidget(self.btnFind)
        
        layoutBottom = QVBoxLayout()
        layoutBottom.addWidget(self.tbl)
        layoutBottom.addWidget(self.canvas)
        
        layout = QVBoxLayout() # 외부 레이아웃
        layout.addLayout(layoutTop)
        layout.addLayout(layoutBottom)
        
        self.setLayout(layout) # 윈도우에 레이아웃 설정
        
        self.cboArea.currentTextChanged.connect(self.cboAreahandler) # 콤보박스 항목을 변경해서 선택했을 경우 이벤트
        self.btnFind.clicked.connect(self.btnFindHandler)
                
        self.setWindowTitle('Table Exam')
        self.setGeometry(10, 30, 500, 600) # 위치와 가로,세로 크기
        self.show() # 윈도우보이기     
        
    def cboAreahandler(self) : # 콤보박스 항목이 변화할 때 호출
        self.leArea.setText(self.cboArea.currentText())
        QMessageBox.about(self, 'title', str(self.cboArea.currentIndex()))
        
    def btnFindHandler(self) :
        df1 = [] # dateTime
        df2 = [] # pm10
        df3 = [] # pm25
        
        strArea = self.leArea.text() # 한글일 경우 인코딩 필요
        encodeArea = parse.quote_plus(strArea) # 인코딩
        
        url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=zzO70SwM6TUvS%2Fa99iS5LE%2FxGsIpP2GEcjHH6egWD4S75oOLWCBluKc206jvjn6HqcUkIB4DlrkZypj1wI4MMg%3D%3D&returnType=xml&numOfRows=10&pageNo=1&stationName=" + encodeArea + "&dataTerm=DAILY&ver=1.0"
        
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
              df3.append(int(pm25value.string))
            for o3value in item.findAll("o3value") : 
              self.tbl.setItem(row, 3, QTableWidgetItem(o3value.string))     
            row += 1
            
        df1.reverse()
        df2.reverse()
        df3.reverse()
            
        ax1 = self.fig.add_subplot(111)
        ax1.clear() # 그래프 영역 초기화(subplot 각각 필요)
        ax1.plot(df1, df2, 'r--', label = 'pm10')
        ax1.plot(df1, df3, 'b--', label = 'pm25')
        ax1.legend()
        
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