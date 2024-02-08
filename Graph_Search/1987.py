#알파벳

def dfs(x,y,visited,c):
    global count
    count=max(count,c)
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny] not in visited:
                # alphabet.append(graph[nx][ny]) #이렇게 하면 되돌아가야할 때 이전상태로 돌아갈수 없음
                dfs(nx,ny,visited+graph[nx][ny],c+1)#인수로 c값과 방문한 알파벳 배열을 넣어줘야함

dx=[-1,1,0,0]
dy=[0,0,-1,1]
count=0
c=1
n,m=map(int,input().split())
graph=[list(input()) for i in range(n)]
dfs(0,0,graph[0][0],c)
print(count)

#설마 연구소처럼 모든 경우 다 해보고 최대값 출력해야 하나???
#상하좌우 다 가본 후에 최대값을 내야하니 한번에 방문처리 하면 안됨.?
#위치 방문 처리가 아닌, 알파벳 방문 처리?
#처음에 들어온 알파벳과 같은 알파벳이 있다면 그위치를 1로 바꿔놓음.=>3번째 테스트케이스 통과 못함.

#Dfs를 돌리면서 현재 변수랑 매개변수로 문자열을 줌. 문자열안에 방문한 문자를 집어넣음.
