# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 14:20:53 2021

@author: user16
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLineEdit, QProgressBar,  QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class MyApp(QWidget) : # 정의
    def __init__(self) :
        super().__init__()  # 부모클래스 생성자 호출
        self.pbarvalue = 50  # 초기 프로그레스바 위치
        self.initUI()
        
    def initUI(self) :
        cb = QComboBox(self) # 콤보박스 생성
        cb.addItem('Seoul')
        cb.addItem('Busan')
        cb.addItem('ChengJu')
        cb.move(0,0)
        
        q1 = QLineEdit(self)
        q1.move(0,30)
        
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(10, 60, 450, 30)
        self.pbar.setValue(self.pbarvalue)
        
        self.btn1 = QPushButton('button 1', self)
        self.btn1.setGeometry(10, 100, 150, 50)
        
        self.btn2 = QPushButton('button 2', self)
        self.btn2.setGeometry(300, 100, 150, 50)
        
        self.btn1.clicked.connect(self.btn1Handler)
        self.btn2.clicked.connect(self.btn2Handler)
        
        self.setWindowTitle('Progress Bar')
        self.setGeometry(50, 50, 500, 300) # 위치와 가로,세로 크기
        self.show() # 윈도우보이기
        
        
    def btn1Handler(self):
        self.pbarvalue -= 10
            
        if self.pbarvalue < 0 :
            self.pbarvalue = 0
        self.pbar.setValue(self.pbarvalue)
            
    def btn2Handler(self):
        self.pbarvalue += 10
            
        if self.pbarvalue > 100 :
            self.pbarvalue = 100
        self.pbar.setValue(self.pbarvalue)    
            
    def keyPressEvent(self, e) : # 키보드 이벤트 핸들러, 반드시 지정된 이름
        if e.key() == Qt.Key_Left :
            self.pbarvalue -= 10
            if self.pbarvalue < 0 :
                self.pbarvalue = 0
            self.pbar.setValue(self.pbarvalue)
        elif e.key() == Qt.Key_Right :
            self.pbarvalue += 10
            if self.pbarvalue > 100 :
                self.pbarvalue = 100
            self.pbar.setValue(self.pbarvalue)
        elif e.key() == Qt.Key_Escape : # esc가 눌렸을 경우 창닫기 (self.close())
         #   self.pbar.setValue(self.close())
        #elif e.key() == Qt.Key_1 :
            QMessageBox.about(self, 'caption', 'Message')
         #   self.pbar.setvalue(self.Message)
        
            
if __name__=='__main__' :
    app = QApplication(sys.argv)
    ex = MyApp() # 클래스 객체 생성
    sys.exit(app.exec_())
        