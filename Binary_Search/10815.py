#숫자카드

def binary_search(a,target,s,e):
    if s>e:
        return 0
    mid=(s+e)//2
    if a[mid]==target:
        return 1
    elif a[mid]>target:
        e=mid-1
        return binary_search(a,target,s,e)
    else:
        s=mid+1
        return binary_search(a,target,s,e)

n=int(input())
A=list(map(int,input().split()))
A.sort()
m=int(input())
M=list(map(int,input().split()))

for i in range(m):
    res=binary_search(A,M[i],0,n-1)
    print(res)

