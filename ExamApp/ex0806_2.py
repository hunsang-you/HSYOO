# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 10:40:22 2021

@author: user16
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QCalendarWidget
from PyQt5.QtCore import Qt

class MyApp(QWidget) : # 정의
    def __init__(self) :
        super().__init__()  # 부모클래스 생성자 호출
        self.initUI()
        
        
    def initUI(self) :
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.move(30,30)
        self.slider.setRange(0,50)
        self.slider.setSingleStep(2)
        
        self.dial = QDial(self)
        self.dial.move(30,70)
        self.dial.setRange(0,50)
        
        cal = QCalendarWidget(self)
        cal.move(30,200)
        cal.setGridVisible(True)
        
        self.setWindowTitle('Slider Exam')
        self.setGeometry(50, 50, 500, 400) # 위치와 가로, 세로 크기
        self.show() # 윈도우보이기
        
if __name__=='__main__' :
    app = QApplication(sys.argv)
    ex = MyApp() # 클래스 객체 생성
    sys.exit(app.exec_())
        