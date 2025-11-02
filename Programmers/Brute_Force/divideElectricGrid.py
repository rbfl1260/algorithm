#전력망 둘로 나누기
from collections import defaultdict

    

def solution(n, wires):
    answer = float('inf')
    
    graph=defaultdict(list)
    #defaultdict는 기본값 생성 함수를 넣어야 해서 list가 들어감

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    #각 간선 정보(a,b)를 사용해 양방향 그래프 만들기

    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        #그래프에서 간선 제거

        cnt=dfs(a,graph,visited=set())
        diff=abs(cnt-(n-cnt))
        #두 전력망 개수의 차이
        answer=min(answer,diff)
        #dfs로 돌린 뒤 한쪽 노드 수 세고 answer에 가장 적은 값 넣기

        graph[a].append(b)
        graph[b].append(a)
        #다시 간선 복구
    return answer

#dfs로 한쪽 전력망 세기
def dfs(node, graph, visited):
    visited.add(node)
    count = 1
    for nxt in graph[node]:
        if nxt not in visited:
            count += dfs(nxt, graph, visited)
    return count