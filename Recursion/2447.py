#별 찍기 - 10

import sys
import math

def Recursion(n,x,y,all):

    if n==1:
       all[x][y]='*'
       return
    
    size=n//3

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:  # 중앙 부분을 빈칸으로 설정
                continue
            Recursion(size, x + i * size, y + j * size, all)
    

n=int(sys.stdin.readline())
all=[[' ']*n for _ in range(n)]

Recursion(n,0,0,all)

for row in all:
    print("".join(row))

