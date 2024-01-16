#보물섬
#L은 육지 W는 바다
#상하좌우 육지로만 이동 가능, 최단거리로 이동하는데 있어서 가장 긴 시간이 걸리는 육지 2곳에 나누어져있음
#육지를 나타내는 2곳 사이를 최단거리로 이동하려면 같은 곳을 두 번이상 지나거나 멀리 돌아가면 안됨
#한칸 이동= 한시간
from collections import deque
#L의 각 위치마다 함수를 돌려 최단거리 최대값을 찾아내는 아이디어로 구현해야함.
dx=[-1,1,0,0]
dy=[0,0,-1,1]

queue=deque()
def bfs(x,y):
    c=0
    visited=[[0]*m for i in range(n)] #visited 초기화
    queue.append((x,y))
    visited[x][y]=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]=='L'and visited[nx][ny]==0:
                visited[nx][ny]=visited[x][y]+1
                queue.append((nx,ny))
                c=max(visited[nx][ny],count)
    return c

n,m=map(int,input().split()) #n세로 m가로
graph=[list(input()) for i in range(n)]
res=0

visited=[[0]*m for i in range(n)]

count=0
for i in range(n):
    for j in range(m):
        if graph[i][j]=='L'and visited[i][j]==0:
            count=max(count,bfs(i,j))

print(count-1)
