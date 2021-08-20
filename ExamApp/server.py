import socket
from _thread import *
import time
import numpy as np

def functhread(client_socket, addr) :
    print(addr[0], addr[1]) # 클라이언트의 접속정보 출력
    while True :
        try : # 예외가 발생할 가능성이 있는 코드

            data = ''
            for item in range(9) :
                data = data + str(np.random.randint(20, 30)) + ':'
            data = data + str(np.random.randint(20, 30))
            
            client_socket.send(data.encode()) # 온도데이터 10개 전송
            time.sleep(60) # 60초 지연
            
            
        except ConnectionResetError as e:
            break
    client_socket.close()

HOST = '192.168.0.3' # local Loopback address, Localhost와 동일
PORT = 9999 # 0~ 65535 범위에서 사용가능

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소킷 객체 생성
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 소킷 옵션 설정

server_socket.bind((HOST, PORT)) # 문자열과 정수
server_socket.listen() # 클라이언트로부터 수신 준비, 서버시작

while True :
    print('wait')
    client_socket, addr = server_socket.accept() # 대기상태, 아래 라인으로 내려가지 않음, 접속할 경우 클라이언트소킷과 IP주소를 반환
    start_new_thread(functhread, (client_socket, addr)) # 스레드 함수 호출
    
    