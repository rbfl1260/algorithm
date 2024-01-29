#히오스 프로게이머
#mid를 최소 레벨 값이라고 생각하고 풀어야 함.
def binary_search(arr,s,e):
    result=0
    while s<=e:
        mid=(s+e)//2 #mid= 팀 목표레벨
        level=0
        for i in arr:
            if mid>i:
                level+=mid-i

        if level<=k:
            s=mid+1 #level 올리려면 mid값을 올려야함
            result=max(result,mid)
        else:
            #level 낮추려면
            e=mid-1
    print(result)

n,k=map(int,input().split()) #n개의 캐릭터, 올릴 수 있는 레벨 총합은 k
xi=[int(input()) for i in range(n)]
xi.sort()
binary_search(xi,min(xi),min(xi)+k)