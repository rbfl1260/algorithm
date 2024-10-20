#요세푸스 문제 0

import sys
# from collections import deque
n,k=map(int,sys.stdin.readline().split())

res=[]
circle=list(range(1,n+1))
#1부터 n까지의 숫자를 리스트로 생성

index=k-1

while len(circle)>0:
    index %= len(circle)
    #리스트의 크기보다 큰 인덱스가 나오지 않도록 해줌
    res.append(circle.pop(index))
    index += k - 1

print("<" + ", ".join(map(str, res)) + ">")