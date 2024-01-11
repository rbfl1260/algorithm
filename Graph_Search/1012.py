#유기농 배추
from collections import deque


def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=1

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and visited[nx][ny]==0 and graph[nx][ny]==1:
                visited[nx][ny]=1
                queue.append((nx,ny))


dx=[-1,1,0,0]
dy=[0,0,-1,1]

t=int(input())
for i in range(t):
    m,n,k=map(int,input().split())
    graph=[[0]*n for a in range(m)]
    visited=[[0]*n for i in range(m)]
    count=0
    for j in range(k):
        x,y=map(int,input().split())
        graph[x][y]=1
    for b in range(m):
        for c in range(n):
            if visited[b][c]==0 and graph[b][c]==1:
                bfs(b,c)
                count+=1

    print(count,end='\n')


