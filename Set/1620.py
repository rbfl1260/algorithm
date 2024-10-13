#나는야 포켓몬 마스터 이다솜

import sys
#포켓몬의 개수, 맞춰야하는 문제 수
n,m=map(int,sys.stdin.readline().split())
poket_name={}
poket_number={}

for i in range(n):
    name=sys.stdin.readline().strip()
    poket_number[name]=i+1
    poket_name[i+1]=name



for i in range(m):
    q=sys.stdin.readline().strip()
    
    res=poket_number.get(q,'not')

    if res=='not':
        res=poket_name.get(int(q),'not')
        print(res)
    else:
        print(res)