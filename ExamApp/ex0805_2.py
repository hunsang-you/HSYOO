# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 14:15:01 2021

@author: user16
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyApp(QWidget) : #QWidget 클래스를 상속
    def __init__(self) : #생성자
        super().__init__() #부모클래스 생성자 호출(최초라인에 작성)
        self.initUI()
    
    def initUI(self) :
        btn1 = QPushButton('&Button1', self) # 버튼생성
        btn2 = QPushButton('&Button2', self)
        btn3 = QPushButton('&Button3', self)
        
        
        vbox = QVBoxLayout() # 박스레이아웃 객체 생성
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        self.setLayout(vbox) # 레이아웃 관리자 선언
        
        self.setWindowTitle('My Window')
        self.setGeometry(30, 30, 400, 600)
        self.show()

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    