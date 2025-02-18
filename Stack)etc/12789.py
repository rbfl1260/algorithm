#도키도키 간식드리미

import sys
from collections import deque

n=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))

stack=deque()
waitingNum=1

for x in nums:
    stack.append(x)
    while stack and stack[-1] ==waitingNum:
        stack.pop()
        waitingNum+=1
if not stack:
    print("Nice")
else:
    print("Sad")