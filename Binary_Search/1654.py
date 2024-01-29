#랜선 자르기
#k<=n k는 가지고 있는 랜선의 개수, n은 필요한 랜선의 개수
#mid는 랜선 길이.
def binary_search(arr,s,e):

    result=0
    while s<=e:
        mid=(s+e)//2
        count=0
        for i in arr:
            if i>=mid: #같아도 한개 만들 수 있는데 같다는 표시 없어서 계속 틀린거였음..^^
                count+=i//mid
        if count>=n:
            result=max(mid,result)
            s=mid+1
        else:
            e=mid-1
    print(result)

k,n= map(int,input().split())
LAN=[int(input()) for i in range(k)]
LAN.sort()
binary_search(LAN,1,max(LAN))


