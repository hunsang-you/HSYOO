# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 11:47:26 2021

@author: user16
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem


class MyApp(QWidget) : # 정의
    def __init__(self) :
        super().__init__()  # 부모클래스 생성자 호출
        self.initUI()
        
        
    def initUI(self) :
        
        self.tbl = QTableWidget(10, 5, self)
        self.tbl.setGeometry(30, 30, 600, 400)
        
        #self.tbl.setItem(0,0, QTableWidgetItem('data1'))
        #self.tbl.setItem(0,1, QTableWidgetItem('data2'))
        #self.tbl.setItem(5,10, QTableWidgetItem('data3'))
        #1 ~ 59 을 순서대로 테이블에 출력
        
        self.tbl.setItem(i,j, QTableWidgetItem(a))
         for i in range(10): # 0~9까지 반복
            for j in range(5): # 0~4
               fcnt = '%02d-%d' % (i+1,j+1)
               self.tbl.setItem(i, j, QTableWidgetItem(fcnt))
               cnt += 1
            
        
        self.setWindowTitle('Table Exam')
        self.setGeometry(50, 50, 500, 300) # 위치와 가로,세로 크기
        self.show() # 윈도우보이기
        
if __name__=='__main__' :
    app = QApplication(sys.argv)
    ex = MyApp() # 클래스 객체 생성
    sys.exit(app.exec_())
        