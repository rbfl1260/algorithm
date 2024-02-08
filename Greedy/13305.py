#주유소
#1km 당 1L기름 사용
import sys
n=int(input())
km=list(map(int,sys.stdin.readline().split()))
cost=list(map(int,sys.stdin.readline().split()))
res=[]
# km=[2,3,1]
# cost=[5,2,4,1]
Min=cost[0]
for i in range(n-1):
    if cost[i]<Min:
        Min=cost[i]
        result=Min*km[i]
    else:
        result=Min*km[i]
    res.append(result)
print(sum(res))






