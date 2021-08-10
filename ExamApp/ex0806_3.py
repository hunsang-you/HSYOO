# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 11:09:44 2021

@author: user16
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDateEdit, QTimeEdit, QDateTimeEdit, QTextEdit
from PyQt5.QtCore import QDate, QTime, QDateTime


class MyApp(QWidget) : # 정의
    def __init__(self) :
        super().__init__()  # 부모클래스 생성자 호출
        self.initUI()
        
        
        
    def initUI(self) :
        dateedit = QDateEdit(self)
        dateedit.move(30,30)
        dateedit.setDate(QDate.currentDate())
        
        timeedit = QTimeEdit(self)
        timeedit.move(30, 60)
        timeedit.setTime(QTime.currentTime())
        
        datetimeedit = QDateTimeEdit(self)
        datetimeedit.move(30, 90)
        datetimeedit.setDateTime(QDateTime.currentDateTime())
        
        te = QTextEdit()
        te.setGeometry(30., 120, 300., 200)
        
        
        self.setWindowTitle('Slider Exam')
        self.setGeometry(50, 50, 500, 400) # 위치와 가로, 세로 크기
        self.show() # 윈도우보이기
        
if __name__=='__main__' :
    app = QApplication(sys.argv)
    ex = MyApp() # 클래스 객체 생성
    sys.exit(app.exec_())
        