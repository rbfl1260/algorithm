
def solution(n, computers):
    answer = 0
    #행과 열이 이미 연결행렬로 그래프가 필요 없음
    visited=[False]*n
    for i in range(n):
        #dfs는 한번에 하나의 연결 덩어리만 탐색하므로 for문이 필요함
        #전체 노드 중 방문 되지 않은 노드가 있음 새 네트워크의 시작점으로 삼음
        if not visited[i]:
            dfs(i,computers,visited)
            answer+=1
    return answer

def dfs(index,computers,visited):
    visited[index]=True
    for j in range(len(computers)):
        #현재 노드와 연결된 아직 방문 안한 노드 찾기 위한 for문
        # 그래서 False가 있을 수 있음 visited에
        if computers[index][j]==1 and not visited[j]:
            dfs(j,computers,visited)