# N과 M(1)

from itertools import permutations

n,m=map(int,input().split())

arr=list(range(1,n+1))
res=list(permutations(arr,m))

for comb in res:
    print(*comb) #언패킹 사용
