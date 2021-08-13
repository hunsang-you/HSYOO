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
from matplotlib import font_manager, rc


class MyApp(QWidget) : # 정의
    def __init__(self) :
        super().__init__()  # 부모클래스 생성자 호출
        self.initUI()
        
    def initUI(self) :
        font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
        rc('font', family=font_name)
        self.leArea = QLineEdit()
        self.btnFind = QPushButton('Find')
        
        self.strArea1 = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주', '세종']
        self.strArea2 = ['종로구', '태종대', '수창동', '신흥', '서석동', '읍내동',' 울산항',' 목감동',' 중앙로', '용담동',' 서천읍',' 삼천동','용담동', '청송읍', '대산면', '이도동', '신흥동']
        self.cboArea = QComboBox()
        self.cboArea.addItems(self.strArea1)
        
        #self.cboArea.addItem('종로구')
        #self.cboArea.addItem('용암동')
        #self.cboArea.addItem('용담동')
        self.radio1 = QRadioButton('Graph Type 1')
        self.radio2 = QRadioButton('Graph Type 2')
        self.radio3 = QRadioButton('Graph Type 3')
        
        self.radio1.setChecked(True)
        
        
        
        self.tbl = QTableWidget(10, 4)
        self.col_head = ['Date', 'pm10', 'pm25', 'o3']
        self.tbl.setHorizontalHeaderLabels(self.col_head)        
        
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        
        layoutTop = QHBoxLayout()
        layoutTop.addWidget(self.leArea)
        layoutTop.addWidget(self.cboArea)
        layoutTop.addWidget(self.btnFind)
        
        layoutTbl = QVBoxLayout()
        layoutTbl.addWidget(self.tbl)
        
        layoutRadio = QHBoxLayout()
        layoutRadio.addWidget(self.radio1)
        layoutRadio.addWidget(self.radio2)
        layoutRadio.addWidget(self.radio3)
        
        layoutGraph = QVBoxLayout()
        layoutGraph.addWidget(self.canvas)
        
        layout = QVBoxLayout() # 외부 레이아웃
        layout.addLayout(layoutTop)
        layout.addLayout(layoutTbl)
        layout.addLayout(layoutRadio)
        layout.addLayout(layoutGraph)
        
        self.setLayout(layout) # 윈도우에 레이아웃 설정
        
        self.cboArea.currentTextChanged.connect(self.cboAreahandler) # 콤보박스 항목을 변경해서 선택했을 경우 이벤트
        self.radio1.clicked.connect(self.radioHandler)
        self.radio2.clicked.connect(self.radioHandler)
        self.radio3.clicked.connect(self.radioHandler)
        
        self.btnFind.clicked.connect(self.btnFindHandler)
              
        
        
        
        self.setWindowTitle('Table Exam')
        self.setGeometry(40, 50, 800, 600) # 위치와 가로,세로 크기
        self.show() # 윈도우보이기     
        
    def cboAreahandler(self) : # 콤보박스 항목이 변화할 때 호출
        self.leArea.setText(self.strArea2[self.cboArea.currentIndex()])
        
       # QMessageBox.about(self, 'title', str(self.cboArea.currentIndex()))
       
    def radioHandler(self):
        if self.radio1.isChecked():
            self.graph1()
           # QMessageBox(self, 'title', "타입 1")
           
        elif self.radio2.isChecked():
            self.graph2()
           # QMessageBox(self, 'title', "타입 2")
        else :
            self.graph3()
           # QMessageBox(self, 'title', "타입 3")
        
    def btnFindHandler(self) :
        self.df1 = [] # dateTime
        self.df2 = [] # pm10
        self.df3 = [] # pm25
        self.df4 = [] # o3
        
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
              self.df1.append(strTime[11:])
              
            for pm10value in item.findAll("pm10value") :
              self.tbl.setItem(row, 1, QTableWidgetItem(pm10value.string))  
              self.df2.append(int(pm10value.string))
            for pm25value in item.findAll("pm25value") : 
              self.tbl.setItem(row, 2, QTableWidgetItem(pm25value.string))
              self.df3.append(int(pm25value.string))
            for o3value in item.findAll("o3value") : 
              self.tbl.setItem(row, 3, QTableWidgetItem(o3value.string))     
              self.df4.append(float(o3value.string))
            row += 1
            
        self.df1.reverse()
        self.df2.reverse()
        self.df3.reverse()
        
        self.graph1()
        
        
    def graph1(self) :
        
        self.fig.clear()
        
        ax1 = self.fig.add_subplot(111)
        ax1.clear() # 그래프 영역 초기화(subplot 각각 필요)
        ax1.plot(self.df1, self.df2, 'r--', label = '미세먼지')
        ax1.plot(self.df1, self.df3, 'b--', label = '초미세먼지')
        ax1.legend()
              
        self.canvas.draw()
    def graph2(self):
        self.fig.clear()
        
        ax1 = self.fig.add_subplot(211)
        ax1.clear() # 그래프 영역 초기화(subplot 각각 필요)
        ax1.plot(self.df1, self.df2, 'r--')
        
        ax2 = self.fig.add_subplot(212)
        ax2.clear() # 그래프 영역 초기화(subplot 각각 필요)
        ax2.plot(self.df1, self.df3)
        
        self.canvas.draw()
    def graph3(self):
        self.fig.clear()
        
        ax1 = self.fig.add_subplot(311)
        ax1.clear() # 그래프 영역 초기화(subplot 각각 필요)
        ax1.plot(self.df1, self.df2, 'r--')
        
        ax2 = self.fig.add_subplot(312)
        ax2.clear() # 그래프 영역 초기화(subplot 각각 필요)
        ax2.plot(self.df1, self.df3, 'b^')
        
        ax3 = self.fig.add_subplot(313)
        ax3.clear()
        ax3.plot(self.df1, self.df4, 'k--')
        
        self.canvas.draw()
        
        
       
        
        
        '''
        
        '''
        
        
  
        
if __name__=='__main__' :
    app = QApplication(sys.argv)
    ex = MyApp() # 클래스 객체 생성
    sys.exit(app.exec_())        