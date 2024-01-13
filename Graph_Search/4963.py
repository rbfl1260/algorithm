#섬의 개수 문제
from collections import deque

queue=[]
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    graph[x][y]=-1
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<h and 0<=ny<w and graph[nx][ny]==1:
                graph[nx][ny]=-1
                queue.append((nx,ny))

dx=[-1,1,0,0,1,-1,-1,1]
dy=[0,0,-1,1,1,1,-1,-1]

while True:
    c=0
    graph=[]
    w,h=map(int,input().split())
    if(w==0 and h==0):
        break
    #위의 이프문 어디에 놓아야할지 잘 생각해야함. 아무데나 놓으면 안됨.
    #w=0,h=0일 때 while문 바로 종료 시켜야함. 안그러면 bfs 함수 실행됨.
    for i in range(h):
        graph.append(list(map(int,input().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j]==1:
                bfs(i,j)
                c+=1
    print(c)