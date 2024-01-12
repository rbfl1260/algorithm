#나이트의 이동문

from collections import deque

t=int(input())

queue=[]
def bfs(x,y,ex,ey):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=1

    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                if nx==ex and ny==ey:
                    visited[nx][ny]=visited[x][y]+1 #이부분이 없으면 끝나는 위치값이 0이므로
                    #0이 리턴됨.
                    return(visited[nx][ny]-1) #함수 호출지점으로 되돌아감.함수 끝
                visited[nx][ny]=visited[x][y]+1
                queue.append((nx,ny))
dx=[-2,-1,-2,-1,2,1,2,1]
dy=[-1,-2,1,2,1,2,-1,-2]

for i in range(t):
    n=int(input())
    visited=[[0]*n for i in range(n)]
    x,y=map(int,input().split())
    ex,ey=map(int,input().split())
    if x==ex and y==ey:
        print(0)
    else:
        a=bfs(x,y,ex,ey)
        print(a)