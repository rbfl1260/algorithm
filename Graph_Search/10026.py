#적록색약
from collections import deque

queue=deque()

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    queue.append((x,y))
    visited[x][y]=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                if color[x][y]==color[nx][ny]:
                    visited[nx][ny]=1
                    queue.append((nx,ny))

n=int(input())

color=[list(input()) for i in range(n)]

visited=[[0]*n for i in range(n)]
c=0

#적록색약이 아닌 사람
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            bfs(i,j)
            c+=1

#적록색약인 사람
for i in range(n):
    for j in range(n):
        if color[i][j]=='G':
            color[i][j]='R'

#방문배열 다시 초기화
visited=[[0]*n for i in range(n)]

c1=0
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            bfs(i,j)
            c1+=1

print(c, c1)

#처음에 방문배열 없이 풀려고 함. 근데 없이 풀려했더니 안의 값이 바뀌어서 적록색약일 경우를 구할 수가 없게 됨
#따라서 방문 배열 만들어서 2가지(적록색약o, 적록색약x) 경우로 나누어서 풀음.

#visited1 으로 따로 선언하려 했더니 bfs에서 안됨. 왜냐면 visited[x][y]=1 인데
#그 안에 visited1[x][y]=1을 넣게 되면 visited[x][y]가 1로 들어갈 때 동시에 visited1에도
#값이 들어가기 때문에 안됨. 물론 밑에서 새로 초기화해주긴 하지만 낭비임. 차라리 기존에 쓰던걸
#다시 초기화하고 쓰는게 나음