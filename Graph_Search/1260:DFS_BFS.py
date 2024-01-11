n,m,v=map(int,input().split())

graph=[[0]*(n+1) for i in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    graph[x][y]=1
    graph[y][x]=1

#행렬에 넣어줌

visited_d=[0]*(n+1)
visited_b=visited_d.copy()

def dfs(v):#스택 사용. 선입후출=>재귀함수
    visited_d[v]=1
    print(v,end=' ')
    for i in range(1,n+1):
        if visited_d[i]==0 and graph[v][i]==1:
            dfs(i)

def bfs(v): #큐 사용해야 함.선입선출
    queue=[v]
    visited_b[v]=1
    while(queue):
        v=queue.pop(0)
        print(v,end=' ')
        for i in range(1,n+1):
            if visited_b[i]==0 and graph[v][i]==1:
                queue.append(i)
                visited_b[i]=1

dfs(v)
print()
bfs(v)

