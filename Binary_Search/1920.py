#수 찾기
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
A.sort()#정렬 중요! 이분탐색에서는 정렬 빼먹으면 안됨!
m=int(input())

M=list(map(int,input().split())) #이 배열안의 수들이 A안에 존재하는지 출력
#존재하면 1, 존재하지 않으면 0

for i in range(m):
    res=binary_search(A,M[i],0,n-1)
    print(res)

