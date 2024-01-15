#토마토2
#3차원 문제!!,,,!!
#상하좌우 위 아래까지
from collections import deque

#dx, dy, dz까지 필요함 [z][y][x]순으로

dz=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dx=[0,0,0,0,-1,1]

queue=deque()

def  bfs():
    while queue:
        z,y,x=queue.popleft()
        for i in range(6):
            nz=dz[i]+z
            ny=dy[i]+y
            nx=dx[i]+x
            if 0<=nz<h and 0<=ny<n and 0<=nx<m and tomato[nz][ny][nx]==0:
                tomato[nz][ny][nx]=tomato[z][y][x]+1
                queue.append((nz,ny,nx))


m,n,h=map(int,input().split())

tomato=[[list(map(int,input().split())) for j in range(n)] for i in range(h)]
#3차원 리스트 입력받음

#저장될 때부터 익어있음 0출력, 모두 익지 못하면 -1출력

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k]==1:
                queue.append((i,j,k))

bfs()
res=0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k]==0:
                print(-1)
                exit()
            res=max(tomato[i][j][k],res)
print(res-1)