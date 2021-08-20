# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 10:52:28 2021

@author: user16
"""

import socket

HOST = '192.168.0.3'
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 객체생성
client_socket.connect((HOST, PORT)) # 서버에 접속
while True :
    msg = input('Enter mssage : ')
    if msg == 'quit' :
        break
    client_socket.send(msg.encode()) # 다국어 시스템에서 필요
    data = client_socket.recv(1024) # 버퍼 크기는 서버와 동일하게
    print(data.decode())

client_socket.close()    