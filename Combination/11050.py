#이항계수

from itertools import combinations

n,k=map(int,input().split())

arr=list(range(n))

res=list(combinations(arr,k))
print(len(res))