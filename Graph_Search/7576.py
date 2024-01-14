#토마토 문제
import sys
from collections import deque

queue=deque()
def bfs():
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<m:
                if tomato[nx][ny]==0 or tomato[x][y]+1<tomato[nx][ny]:
                    tomato[nx][ny]=tomato[x][y]+1
                    queue.append((nx,ny))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

m,n=map(int,input().split())#n은 세로,m은 가로
tomato=[list(map(int,input().split())) for i in range(n)]
#1=익은 토마토, 0=익지 않은 토마토, -1=없음

for i in range(n):
    for j in range(m):
        if tomato[i][j]==1:
            queue.append((i,j))

bfs()
res=0
for k in tomato:
    for j in k:
        if j==0:
            print(-1)
            exit()
        res=max(j,res)
print(res-1)
