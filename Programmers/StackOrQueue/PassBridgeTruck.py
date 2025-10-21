#다리를 지나는 트럭
from collections import deque

def solution(bridge_length, weight, truck_weights):

    bridge=deque([0]*bridge_length)
    time=0
    total_w=0
    trucks=deque(truck_weights)

    while bridge:
        time+=1
        total_w-=bridge.popleft()

        if trucks:
            if total_w+trucks[0]<=weight:
                t=trucks.popleft()
                bridge.append(t)
                total_w+=t
            else:
                bridge.append(0)
        if not trucks and total_w==0:
            break
    return time

b=2
w=10
tw=[7,4,5,6]
solution(b,w,tw)