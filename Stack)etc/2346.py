#풍선 터뜨리기

import sys

n=int(sys.stdin.readline())

balloons=list(map(int,sys.stdin.readline().split()))

balloons = [(i + 1, num) for i, num in enumerate(balloons)]

index = 0  # 첫 번째 풍선에서 시작
res = []

while balloons:
    idx,move=balloons.pop(index)
    res.append(idx)
    if not balloons:
        break
    if move>0:
        index=(index+(move-1))%len(balloons)
    else:
        index=(index+move)%len(balloons)
        print(index+move)

print(' '.join(map(str,res)))