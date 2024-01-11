#안전영역
from collections import deque
def bfs(x,y,h):
    queue= deque()
    queue.append((x,y))
    visited[x][y]=1

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and zone[nx][ny]>h:
                visited[nx][ny]=1
                queue.append((nx,ny))



n=int(input())
h=0
#현재 높이
zone=[]
maxv=0

dx=[-1,1,0,0]
#   하 상
dy=[0,0,-1,1]
#       좌 우


for i in range(n):
    zone.append(list(map(int,input().split())))
    for j in range(n):
        if maxv<zone[i][j]:
            maxv=zone[i][j]
#최대값 찾기, 변수 max로 하면 안됨. 내장함수 있기 때문에


res=1 #비가 아예 안왔다면

for height in range(1,maxv+1):
    visited=[[0]*n for i in range(n)] #각 방문마다 초기화해줘야함. 비가오는 높이가 매번 달라지기 때문
    c=0
    for i in range(n):
        for j in range(n):
            if zone[i][j]>height and visited[i][j]==0:
                bfs(i,j,height)
                c+=1
    res=max(res,c)

print(res)


