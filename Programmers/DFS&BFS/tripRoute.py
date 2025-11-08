#여행 경로

def solution(tickets):
    tickets.sort()
    visited=[False for _ in range(len(tickets))]
    answer=["ICN"]

    dfs("ICN",0,tickets,visited,answer)
   
    return answer

def dfs(curr,used,tickets,visited,answer):
    if used==len(tickets):
        return True
    for i in range(len(tickets)):
        a,b=tickets[i]
        if not visited[i] and a==curr:
            visited[i]=True
            answer.append(b)

            if dfs(b,used+1,tickets,visited,answer):
                #지금 선택한 b공항에서 출발하는 다음 항공권 이어서 찾기
                return True
            #만약 False를 반환한다면
            #방금 넣은 b제거
            #티켓 사용 취소
            answer.pop()
            visited[i]=False
    return False