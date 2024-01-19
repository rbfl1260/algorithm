#맥주 마시기
from collections import deque

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft() #현재 내 위치

        if abs(fx-x)+abs(fy-y)<=1000: #1000=> 맥주 1병=50m 그러므로 맥주 20병=1000m
            return ('happy')
        for i in range(n):
            if visited[i]==0:#방문하지 않은 편의점이면
                nx,ny=graph[i]#편의점의 위치 가져옴.
                if abs(nx-x) + abs(ny-y) <=1000: #절댓값
                    visited[i]=1
                    queue.append((nx,ny))
    return ('sad')

t=int(input())

for i in range(t):
    n=int(input())
    visited=[0]*n
    graph=[]
    homex,homey=map(int,input().split()) #시작 위치

    # queue.append((homex,homey)) #큐에 시작 위치 넣어주기
    # #bfs안에 넣어주는게 좋음. 큐 초기화도 bfs안에서 하는게 좋음.(값이 여러개 일땐 헷갈려짐)

    for i in range(n):#편의점 위치 n개 입력받기
       graph.append(list(map(int,input().split())))
    #도착 위치
    fx,fy=map(int,input().split())
    res=bfs(homex,homey)
    print(res)