#N과 M(4)

from itertools import product

n,m=map(int,input().split())

arr=list(range(1,n+1))

flag=0
for val in product(arr,repeat=m):
   if all(val[j]>=val[j-1] for j in range(1,len(val))):
      print(*val)