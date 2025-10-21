from collections import deque

def solution(prices):
    queue=deque(prices)
    answer=[]
    while queue:
        count=0
        price=queue.popleft()
        for i in queue: #가격이 떨어지는 순간 멈춰야해
            if i<price:
                count+=1
                break
            else:
                count+=1
        answer.append(count)
    print(answer)

prices=[1, 2, 3, 2, 3]
solution(prices)