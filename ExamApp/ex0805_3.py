# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 14:47:15 2021

@author: user16
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QVBoxLayout, QRadioButton
from PyQt5.QtCore import Qt

class MyApp(QWidget) :
        def __init__(self) : #생성자
            super().__init__()
            self.initUI()            
        
        def initUI(self) :
            label1 = QLabel('My Label 1', self) #레이블 객체 생성
            label1.setAlignment(Qt.AlignCenter) #가운데 정렬
            font1 = label1.font() # 해당 위젯의 폰트 변수 설정
            font1.setPointSize(20) #폰트 크기
            font1.setBold(True)
            
            label2 = QLabel('My Label 2', self) #레이블 객체 생성
            label2.setAlignment(Qt.AlignCenter) #가운데 정렬
            font2 = label2.font() # 해당 위젯의 폰트 변수 설정
            font2.setPointSize(30) #폰트 크기
            font2.setBold(True)
            
            
            cb = QCheckBox('My Checkbox', self) # 체크박스 생성
            
            rbtn1 = QRadioButton("My Radio Button 1")
            rbtn2 = QRadioButton("My Radio Button 2")

            rbtn1.setChecked(True)
            
            label1.setFont(font1) # 폰트 적용
            label2.setFont(font2)          
    

            layout = QVBoxLayout() #레이아웃 객체 생성
            
            layout.addWidget(label1)
            layout.addWidget(label2)
            layout.addWidget(cb)
            layout.addWidget(rbtn1)
            layout.addWidget(rbtn2)
            
            
            self.setLayout(layout) # 박스레이아웃 설정            
            self.setWindowTitle('My Window')
            self.setGeometry(30, 30, 400, 600)
            self.show()
        

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    