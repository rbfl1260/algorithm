k=int(input()) #컴퓨터 수 = 노드
n=int(input()) #쌍의 수 = 간선
v=1
c=0

infection=[0]*(k+1)
graph=[[0]*(k+1) for i in range(k+1)]

for i in range(n):
    x,y=map(int,input().split())
    graph[x][y]=graph[y][x]=1

queue=[v]
infection[v]=1
while(queue):
    v=queue.pop(0)
    # c+=1 큐에서 하나씩 pop될 때마다 1씩 더해줌. 근데 컴퓨터 1번은 제외하므로 1빼줘야함
    for i in range(1,k+1):
        if infection[i]==0 and graph[v][i]==1:
            queue.append(i)
            c+=1 #1번 제외하고 나머지 append될 때마다 1씩 더해줌
            infection[i]=1
print(c)