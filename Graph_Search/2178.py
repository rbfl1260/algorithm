#미로 탐색
from collections import deque
# min_value=n*m
#
# for i in range(min_value,0,-1)
#     c=0
#     for k in range(n):
#         for j in range(m):
#             if visited[k][j]==0 and graph[k][j]==1:
#                 #이렇게 하면 안됨. 무조건 1,1 에서 출발해야함.

queue=[]
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=1

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and graph[nx][ny]==1:
                visited[nx][ny]=visited[x][y]+1
                queue.append((nx,ny))
    print(visited[n-1][m-1])

n,m=map(int,input().split())
graph=[]
x=0
y=0
visited=[[0]*m for i in range(n)]
#2차원배열 방문 리스트

for i in range(n):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0]
#   하 상
dy=[0,0,-1,1]
#       좌 우
bfs(x,y)

