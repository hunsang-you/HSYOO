# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 13:30:39 2021

@author: user16
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDial, QLCDNumber


class MyApp(QWidget) : # 정의
    def __init__(self) :
        super().__init__()  # 부모클래스 생성자 호출
        self.initUI()
        
    def initUI(self):
        self.lcd = QLCDNumber(self)
        self.lcd.move(30,30)
        
        self.dial = QDial(self)
        self.dial.move(30,80)
        
        self.dial.valueChanged.connect(self.lcd.display) # 이벤트 연결
        
        
        self.btn1 = QPushButton('button 1', self) # 버튼생성
        self.btn1.setGeometry(30,250,150,50)
        
        self.btn1.clicked.connect(self.btn1Event) # 이벤트 연결
        
        self.btn2 = QPushButton('button 2', self) # 버튼생성
        self.btn2.setGeometry(200,250,150,50)
        
        self.btn2.clicked.connect(self.btn2Event)
        
        
        self.setWindowTitle('Event Exam')
        
        self.setGeometry(50, 50, 500, 300) # 위치와 가로,세로 크기
        self.show() # 윈도우보이기
        
    def btn1Event(self):
        self.resize(700,500)
    def btn2Event(self):
        self.resize(500,500)
        
        
if __name__=='__main__' :
    app = QApplication(sys.argv)
    ex = MyApp() # 클래스 객체 생성
    sys.exit(app.exec_())
        