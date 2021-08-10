# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 09:45:57 2021

@author: user16
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLineEdit, QProgressBar


class MyApp(QWidget) : # 정의
    def __init__(self) :
        super().__init__()  # 부모클래스 생성자 호출
        self.initUI()
        
    def initUI(self) :
        cb = QComboBox(self) # 콤보박스 생성
        cb.addItem('Seoul')
        cb.addItem('Busan')
        cb.addItem('ChengJu')
        cb.move(0,0)
        
        ql = QLineEdit(self)
        ql.move(0,30)
        
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(10, 60, 450, 30)
        
        self.setWindowTitle('Combobox and Textbox Exam')
        self.setGeometry(50, 50, 500, 300) # 위치와 가로,세로 크기
        self.show() # 윈도우보이기
        
if __name__=='__main__' :
    app = QApplication(sys.argv)
    ex = MyApp() # 클래스 객체 생성
    sys.exit(app.exec_())
        