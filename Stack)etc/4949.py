#균형잡힌 세상
from collections import deque
import sys

stack=deque()
res=[]

while True:
    line=sys.stdin.readline().rstrip()

    if line=='.':
        break

    if not any(ch in "([])" for ch in line):
        #any는 하나라도 true라면 if문이 true가 됨.
        res.append('yes')
        continue

    stack.clear()

    for x in line:
        if x in "([])":
            stack.append(x)
            while len(stack)>1:
                if(stack[-2]=='(' and stack[-1]==')') or (stack[-2]=='[' and stack[-1]==']'):
                    stack.pop()
                    stack.pop()
                else:
                    break
   
    if not stack:
        res.append('yes')
    else:
        res.append('no')

for i in res:
    print(i,end='\n')