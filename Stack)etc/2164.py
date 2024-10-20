#카드2

import sys
from collections import deque

n=int(sys.stdin.readline())
cards=deque()

for i in range(1,n+1):
    cards.append(i)

while len(cards)!=1:
    cards.popleft()
    first=cards.popleft()
    cards.append(first)
print(cards[0])