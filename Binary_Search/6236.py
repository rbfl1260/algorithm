#용돈관리
#mid= 한번 뽑을 금액. 금액에 따라서 m번 이하인지 이상인지 체크하면서
#mid값 찾으면 됨.

n,m=map(int,input().split())
#n일, m번
money=[int(input()) for i in range(n)]
#money는 현우가 n일 동안 이용할 금액.
s=max(money)
e=sum(money)
result=0

while s<=e:
    mid=(s+e)//2
    count=1 #인출하고 시작.
    # 변수 하나 더 만들어서 mid 값 저장
    mid1=mid
    for i in money:
        if mid1>=i:
            mid1=mid1-i
        else:
            count+=1
            mid1=mid #m을 mid로 재설정 #s=max(money)이기 때문에 항상 m>=i
            mid1-=i
    if count>m:
        s=mid+1
    else:
        result=mid
        e=mid-1

print(result)

