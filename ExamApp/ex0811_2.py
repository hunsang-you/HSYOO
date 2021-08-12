# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 09:56:46 2021

@author: user16
"""
import pymysql
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas



class MyApp(QWidget) : # 정의
    def __init__(self) :
        super().__init__()  # 부모클래스 생성자 호출
        self.dbconn()
        self.initUI()
      
        
    def initUI(self) :
        
        self.lbltitle = ['제품번호', '제품명', '재고량', '단가', '제조업체']
       
        self.lbl1 = QLabel('제품번호', self)
        self.lbl1.setGeometry(0, 30, 100, 30)
        self.lbl1.setStyleSheet("color : blue;" 
                                "background-color : #6699cc;"
                                "border-style : dashed;"
                                "border-width : 2px;")

        self.lel = QLineEdit(self)
        self.lel.setGeometry(110, 30, 100, 30)
                
        

        self.lbl2 = QLabel('제품명', self)
        self.lbl2.setGeometry(0, 60, 100, 30)
        self.lbl2.setStyleSheet("color : blue;" 
                                "background-color : #6699cc;"
                                "border-style : dashed;"
                                "border-width : 2px;")
                        
        self.le2 = QLineEdit(self)
        self.le2.setGeometry(110, 60, 100, 30)
        
        
        self.lbl3 = QLabel('재고량', self)
        self.lbl3.setGeometry(0,90, 100, 30)
        self.lbl3.setStyleSheet("color : blue;" 
                                "background-color : #6699cc;"
                                "border-style : dashed;"
                                "border-width : 2px;")
               
        
        self.le3 = QLineEdit(self)
        self.le3.setGeometry(110, 90, 100, 30)
        

        self.lbl4 = QLabel('단가', self)
        self.lbl4.setGeometry(0,120, 100, 30)
        self.lbl4.setStyleSheet("color : blue;" 
                                "background-color : #6699cc;"
                                "border-style : dashed;"
                                "border-width : 2px;")

        self.le4 = QLineEdit(self)
        self.le4.setGeometry(110, 120, 100, 30)
        
        
        self.lbl5 = QLabel('제조업체', self)
        self.lbl5.setGeometry(0,150, 100, 30)
        self.lbl5.setStyleSheet("color : blue;" 
                                "background-color : #6699cc;"
                                "border-style : dashed;"
                                "border-width : 2px;")
        


        self.le5 = QLineEdit(self)
        self.le5.setGeometry(110, 150, 100, 30)
        
        self.btn1 = QPushButton('Insert', self)
        self.btn1.setGeometry(0, 190, 100, 30)
        self.btn1.clicked.connect(self.btn1Handler)
        
        self.btn2 = QPushButton('Load', self)
        self.btn2.setGeometry(110, 190, 100, 30)
        self.btn2.clicked.connect(self.btn2Handler)
        
        self.btn3 = QPushButton('Previous', self)
        self.btn3.setGeometry(220, 190, 100, 30)
        self.btn3.clicked.connect(self.btn3Handler)
        
        self.btn4 = QPushButton('Next', self)
        self.btn4.setGeometry(330, 190, 100, 30)
        self.btn4.clicked.connect(self.btn4Handler)
        
        self.lbl6 = QLabel(self)
        self.lbl6.setGeometry(440, 190, 100, 30)
        self.lbl6.setStyleSheet("background-color : #6699cc;")

        self.leFind = QLineEdit(self)
        self.leFind.setGeometry(0, 230, 100, 30)        

        self.btnFind = QPushButton('Find', self)
        self.btnFind.setGeometry(110, 230, 100, 30)
        self.btnFind.clicked.connect(self.btnFindHandler)
        
        self.tbl = QTableWidget(self)
        self.tbl.setRowCount(1)
        self.tbl.setColumnCount(5)
        self.tbl.setGeometry(0, 270, 600, 400)
        self.col_head = ['제품번호', '제품명', '재고량', '단가', '제조업체']
        self.tbl.cellClicked.connect(self.tblCellHandler)
        
        self.setWindowTitle('DB Exam')
        self.setGeometry(50, 50, 1200, 600) # 위치와 가로,세로 크기
        self.show() # 윈도우보이기
        
    def btn1Handler(self):
       # QMessageBox.about(self, '테스트', 'btn1이벤트')
        sql = "insert into 제품 values (%s, %s, %s, %s, %s)"
        val1 = self.le1.text()
        val2 = self.le2.text()
        val3 = self.le3.text()
        val4 = self.le4.text()
        val5 = self.le5.text()
        self.cursor.execute(sql, (val1, val2, val3, val4, val5))
        self.conn.commit()
        
        # 메세지상자 출력
        QMessageBox.about(self, '정보', '입력되었습니다')
        
        # 기존상자 내용 지우기
        self.lel.setText('')
        self.le2.setText('')
        self.le3.setText('')
        self.le4.setText('')
        self.le5.setText('')
    
    def btn2Handler(self):
       # QMessageBox.about(self, '테스트', 'btn2이벤트')
        sql = "select * from 제품"
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall() # result 변수에 모든 레코드가 반환됨
        
        self.cnt = len(self.result) # 전체 레코드 갯수]
        self.tbl.setRowCount(self.cnt)
        
        
        self.currec = 0 # 레코드 번호
        
        item = self.result[self.currec] # 첫번째 레코드 반환
        self.le1.setText(item[0])
        self.le2.setText(item[1])
        self.le3.setText(str(item[2]))
        self.le4.setText(str(item[3]))
        self.le5.setText(item[4])
        
        strrec = "%d / %d" % (self.currec+1, self.cnt)
        self.lbl6.setText(strrec)
        
        row = 0
        for item in self.result :
            for col in range(5) : # 열 구성 
                self.tbl.setItem(row, col, QTableWidgetItem(str(item[col])))
            row += 1
        
        
        QMessageBox.about(self, '정보', '제품 테이블이 로드되었습니다.')
        
    def btn3Handler(self):
       self.currec -= 1
       if self.currec < 0 :
           self.currec = 0
       item = self.result[self.currec] # 첫번째 레코드 반환    
       self.le1.setText(item[0])
       self.le2.setText(item[1])
       self.le3.setText(str(item[2]))
       self.le4.setText(str(item[3]))
       self.le5.setText(item[4])
   
    def btn4Handler(self):
       self.currec += 1
       if self.currec >= self.cnt :
           self.currec = self.cnt-1
           QMessageBox.about(self, '정보', '레코드의 마지막입니다')
       item = self.result[self.currec] # 첫번째 레코드 반환    
       self.le1.setText(item[0])
       self.le2.setText(item[1])
       self.le3.setText(str(item[2]))
       self.le4.setText(str(item[3]))
       self.le5.setText(item[4])
    
       
    def btnFindHandler(self):
        sql = "select * from 제품 where 제품명 = %s"
        self.cursor.execute(sql, (self.leFind.text()))
        self.result = self.cursor.fetchall()
        
        total = len(self.result)
        if total > 0 :
            item = self.result[self.currec] # 첫번째 레코드 반환    
            self.le1.setText(item[0])
            self.le2.setText(item[1])
            self.le3.setText(str(item[2]))
            self.le4.setText(str(item[3]))
            self.le5.setText(item[4])
            
        else :   # 조회실패시    
            QMessageBox.about(self, '정보', '검색 결과가 없습니다.')
    
    def tblCellHandler(self, row, col) :
        cellinfo = "%d : %d" & (row, col)
        QMessageBox(self, "정보", cellinfo)
            
            
    def dbconn(self):
        self.conn = pymysql.connect(host = '127.0.0.1', user = 'bigdata', password = '12345678', db = 'mysql', charset = 'utf8')
        self.cursor = self.conn.cursor() # 커서 설정
        
        
        

       
        
if __name__=='__main__' :
    app = QApplication(sys.argv)
    ex = MyApp() # 클래스 객체 생성
    sys.exit(app.exec_())
        