#문자열 집합

import sys

n,m = map(int,sys.stdin.readline().split())
#n개의 문자열로 이루어진 집합 s가 주어짐
s=set([sys.stdin.readline().strip() for _ in range(n)])

count=0

for _ in range(m):
    if sys.stdin.readline().strip() in s:
        count+=1

print(count)