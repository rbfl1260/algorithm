#도키도키 간식드리미

import sys
from collections import deque

n=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))

res=[] #결과 저장
wait=deque() #대기열 저장

# 1부터 n까지 학생번호
line=deque(range(1,n+1))

for num in nums:
  while line:
     if line[0] ==num:
        res.append(num)
        line.popleft()
        break
     else:
        wait.append(num)
        break

if list(wait) == sorted(wait,reverse=True):
   print('Nice')
else:
   print('Sad')