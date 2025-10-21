#프로세스
from collections import deque

def solution(priorities, location):
    answer = 0
    queue=deque([(p,i) for i,p in enumerate(priorities)]) #인덱스,원소 로 이루어진 튜플을 만들어줌
    while queue:
        current=queue.popleft()
        if any(current[0] < q[0] for q in queue):
            #현재 프로세스보다 높은 우선순위가 있음 뒤로 보냄
            queue.append(current)
        else:
            answer+=1
            if current[1]==location:
                return answer

arr=[1, 1, 9, 1, 1, 1]	
location=0
print(solution(arr,location))