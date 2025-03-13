#N과 M(2)
from itertools import combinations

n,m=map(int,input().split())
arr=list(range(1,n+1))
res=list(combinations(arr,m))

for comb in res:
    print(*comb)