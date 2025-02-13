#브루트포스 -> 완전탐색: 가능한 모든 경우의 수 탐색
#블랙잭
from itertools import combinations

n,m=map(int,input().split())

cards=list(map(int,input().split()))

maxVal=0

#for문으로 직접 생성
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             sum_cards=cards[i]+cards[j]+cards[k]
#             if sum_cards<=m:
#                 maxVal=max(maxVal,sum_cards)

for combination in combinations(cards,3):
    total=sum(combination)
    if total<=m:
        maxVal=max(maxVal,total)
print(maxVal)


