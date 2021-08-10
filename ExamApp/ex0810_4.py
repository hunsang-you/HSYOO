# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 13:37:28 2021

@author: user16
"""

import pymysql
import pandas as pd
import urllib.request as ulib
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem


class MyApp(QWidget) : # 정의
    def __init__(self) :
        super().__init__()  # 부모클래스 생성자 호출
        
       
        
        self.initUI()
        
        
    def initUI(self) :
        # db 접속
        conn = pymysql.connect(host='127.0.0.1', user='bigdata', password='12345678', db = 'mysql', charset='utf8')
        cursor = conn.cursor() # 커서 설정


        sql = 'select * from 제품'
        cursor.execute(sql)  # sql 실행
        result = cursor.fetchall() # 모든 레코드를 반환해서 result 변수에 저장
        cnt = len(result)

        
        self.tbl = QTableWidget(cnt, 5, self)
        self.tbl.setGeometry(30, 30, 600, 400)
        self.col_head = ['제품번호', '제품명', '제조량', '단가', '제조업체']
        self.tbl.setHorizontalHeaderLabels(self.col_head)        
        
        
        row = 0
        for item in result :
            for col in range(5) : # 열 구성 
                self.tbl.setItem(row, col, QTableWidgetItem(str(item[col])))
            row += 1
            
        
        self.setWindowTitle('Table Exam')
        self.setGeometry(50, 50, 500, 300) # 위치와 가로,세로 크기
        self.show() # 윈도우보이기

        cursor.close()
        conn.close()
        
if __name__=='__main__' :
    app = QApplication(sys.argv)
    ex = MyApp() # 클래스 객체 생성
    sys.exit(app.exec_())
        