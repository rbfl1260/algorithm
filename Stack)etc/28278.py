#스택2

import sys
stack=[]
n=int(sys.stdin.readline())
for i in range(n):
    num=list(map(int,sys.stdin.readline().split()))

    if num[0]==1:
        stack.append(num[1])
    elif num[0]==2:
        if len(stack)!=0:
            print(stack.pop())
        else:
            print(-1)
    elif num[0]==3:
        print(len(stack))
    elif num[0]==4:
        # if len(stack)==0:
        #     print(1)
        # else:
        #     print(0)
        print(1 if not stack else 0)
    
    else:
        print(stack[-1] if stack else 0)
