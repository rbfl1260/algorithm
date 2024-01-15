#아기상어2
from collections import deque

queue=deque()
def bfs():
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

dx=[-1,1,0,0,1,-1,-1,1]
dy=[0,0,-1,1,1,1,-1,-1]

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            queue.append((i,j))
bfs()

res=0
for i in graph:
    for j in i:
        res=max(res,j)
print(res-1)