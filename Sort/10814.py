#나이순 정렬

import sys
N=int(sys.stdin.readline())
arr=[]
for _ in range(N):
    age,name=input().split()
    age=int(age)
    arr.append([age,name])

arr.sort(key=lambda pair : (pair[0]))

for age,name in arr:
    print(age,name)