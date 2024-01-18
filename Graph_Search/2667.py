#단지 번호 붙이기
#흠 단지 수 세는 건 쉬운 듯 영역 구하는거니까
#근데 단지 안의 수를 세려면 어케 해야 할까 배열 따로 필요?
#반드시 dfs로 풀기
def dfs(x,y):
    global count #count를 전역변수로 사용하겠다 선언.
    graph[x][y]=2
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1:#순서 바뀌면 안됨. 범위 검사가 먼저임.
            count+=1
            dfs(nx,ny)
    return count

dx=[-1,1,0,0]
dy=[0,0,-1,1]
n=int(input())
c=0
count=1
res=[]
graph=[list(map(int,input())) for i in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            res.append(dfs(i,j))
            count=1
            c+=1
res.sort()
print(c)
for i in res:
    print(i)

#아예 dfs에 영역 개수 세는 인자 c를 넣어주기
#이 코드에서 dfs에 있는 c는 리턴될 때마다 값이 초기화되어 dfs로 다시 들어옴.
def dfs(x,y,c):
    graph[x][y]=2
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1:#순서 바뀌면 안됨. 범위 검사가 먼저임.
            c=dfs(nx,ny,c+1)
    return c

dx=[-1,1,0,0]
dy=[0,0,-1,1]
n=int(input())
c=1
cnt=0
res=[]
graph=[list(map(int,input())) for i in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            res.append(dfs(i,j,c))

            cnt+=1
res.sort()
print(cnt)
for i in range(len(res)):
    print(res[i])