import socket
import datetime
import pymysql

conn = pymysql.connect(host = '127.0.0.1', user = 'bigdata', password = '12345678', db = 'mysql', charset = 'utf8')
cursor = conn.cursor() # 커서 설정

HOST = '192.168.0.3'
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 객체생성
client_socket.connect((HOST, PORT)) # 서버에 접속
while True :

    data = client_socket.recv(1024) # 버퍼 크기는 서버와 동일하게
    now = datetime.datetime.today() # 현재 시스템 날짜 및 시간
    nowstr = now.strftime('%Y-%m-%d %H:%M:%S') #문자열로 지정
    print(nowstr)
    rs = data.decode().split(':') # 콜론을 구분자로 모든 데이터를 분리(리스트)
    print(rs)
    sql = "insert into tblsensor values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (nowstr, rs[0], rs[1], rs[2], rs[3], rs[4], rs[5], rs[6], rs[7], rs[8], rs[9]))
    conn.commit()

client_socket.close()
cursor.close()