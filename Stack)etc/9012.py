#괄호
from collections import deque
t=int(input())

stack=deque()

for i in range(t):
    line=list(input().rstrip())

    stack.clear()
    for x in line:
        stack.append(x)
        while len(stack)>1:
            if (stack[-2]=='(' and stack[-1]==')'):
                stack.pop()
                stack.pop()
            else:
                break
    if not stack:
        print('YES')
    else:
        print('NO')