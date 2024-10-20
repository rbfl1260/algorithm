#덱 2

import sys
from collections import deque

n=int(sys.stdin.readline())
arr=deque()

for i in range(n):

    order=list(map(int,sys.stdin.readline().split()))
    #리스트가 만들어짐

    if order[0]==1:
        arr.append(order[1])
    elif order[0]==2:
        arr.appendleft(order[1])
    elif order[0]==3:
        print(arr.pop() if arr else -1)
    elif order[0]==4:
        print(arr.popleft() if arr else -1)
    elif order[0]==5:
        print(len(arr))
    elif order[0]==6:
        print(1 if not arr else 0)
    elif order[0]==7:
        print(arr[-1] if arr else -1)
    elif order[0]==8:
        print(arr[0] if arr else -1)