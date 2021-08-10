# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 10:00:53 2021

@author: user16
"""

score = [75, 88, 92 , 65, 99]
title = ['빅데이터', '프로그래밍']
data = ['홍길동', 90, '이도령', 85]

tot = 0
for i in score:
    tot += i
print(tot, tot/len(score)) # 합계, 평균

print(score[0])
print(score[2:]) #2~마지막까지
print(score[2:4]) #2 ~ (4-1)
print(score) # 리스트 전체


score[2] = 95 # 2번 원소 수정
print(score)

del(score[2]) # 2번 원소 삭제
print(score)

score.append(73) # 마지막 위치에 추가
print(score)


score.insert(2, 85) # 지정된 위치에 값 추가
print(score)

score.sort() # 오름차순 정렬(데이터 변경됨)
print(score)

score.reverse()
print(score)

myList = [] #비어있는 리스트 생성
for i in range(1, 11, 1): # 1 ~ 10
    myList.append(i*10)
print(myList)

myList.remove(50)
print(myList)