#아기상어2
from collections import deque

queue=[]
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=1

    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==0 and graph[nx][ny]!=1:
                    visited[nx][ny]=visited[x][y]+1
                    queue.append((nx,ny))
                elif visited[nx][ny] > visited[x][y]+1 and graph[nx][ny]!=1:
                    visited[nx][ny]=visited[x][y]+1
    print(visited)

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

dx=[-1,1,0,0,1,-1,-1,1]
dy=[0,0,-1,1,1,1,-1,-1]

visited=[[0]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        if visited[i][j]==0 and graph[i][j]==1:
            bfs(i,j)