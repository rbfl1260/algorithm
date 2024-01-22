#빙산
from collections import deque

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    # visited[x][y]=1
    while queue:
        c=0
        x,y=queue.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==0 and visited[x][y]!=-2:
                    c+=1
                    # graph[x][y]-=1
                    # if graph[x][y]==0:
                    #     graph[x][y]=0
                elif graph[nx][ny]>0 and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    # print(graph[nx][ny])
                    queue.append((nx,ny))

        graph[x][y]=graph[x][y]-c
        if graph[x][y]<0:
            graph[x][y]=0
            visited[x][y]=-2
        print(graph)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,m=map(int,input().split())
graph=[list(map(int,input().split())) for i in range(n)]
visited=[[0]*m for i in range(n)]
count=0

#빙산 분리 최초의 시간을 어떻게 구할건지?

for i in range(n):
    for j in range(m):
        if graph[i][j]>0:
            bfs(i,j)
            count+=1
print(graph)


#맞은 코드
#     melt=[]라는 배열을 하나 만들어서 해줘도 됨. 이 방법을 더 많이 씀.
# #빙산
# from collections import deque
#
# def bfs(x,y):
#     queue=deque()
#     queue.append((x,y))
#     visited[x][y]=1
#
#     while queue:
#         c=0
#         x,y=queue.popleft()
#
#         for i in range(4):
#             nx=dx[i]+x
#             ny=dy[i]+y
#             if 0<=nx<n and 0<=ny<m:
#                 if graph[nx][ny]==0 and visited[nx][ny]==0:
#                     c+=1
#                 elif graph[nx][ny]>0 and visited[nx][ny]==0:
#                     visited[nx][ny]=1
#                     queue.append((nx,ny))
#
#         if graph[x][y]-c<=0:
#             graph[x][y]=0
#             visited[x][y]=1
#         else:
#             graph[x][y]-=c
#
# dx=[-1,1,0,0]
# dy=[0,0,-1,1]
#
# n,m=map(int,input().split())
# graph=[list(map(int,input().split())) for i in range(n)]
# visited=[[0]*m for i in range(n)]
# year=0
# while(True):
#     visited=[[0]*m for i in range(n)] #초기화
#     count=0 #while밖에다 해주면 count는 영역을 게속 셀 수가 없음. 계속 바뀌는 영역을 체크해주기 위해
#     #안에다가 선언해줘야함.
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j]>0 and visited[i][j]==0:
#                 bfs(i,j)
#                 count+=1
#     if count>=2:
#         print(year)
#         break
#     elif count==0:
#         print(0)
#         break
#     year+=1 #count랑 년도는 다르게. count는 단지 영역 개수 세는 것일 뿐임.
#
# # print(graph)

