#N과 M(3)
from itertools import product

n,m=map(int,input().split())
arr=list(range(1,n+1))

res=list(product(arr,repeat=m))

for i in res:
    print(*i)