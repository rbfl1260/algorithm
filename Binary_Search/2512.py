#예산
#정해진 총액 이하에서 가능한 한 최대의 총 예산 배정
#상한액을 mid로 잡아서 mid에서 각 지방 예산 요청을 뻄.
#그리고 뺀 값이 가장 적을 때의 mid가 최대 상한액.

n=int(input())
buget=list(map(int,input().split()))
m=int(input())#총 예산액
#s=n으로 하면 안됨.=> 왜????? 왜 안되긴 n은 지방개수니까 그렇지. 무슨 상관이있냐 지방개수랑 이 바보야
s=1
e=m
result=0

if sum(buget)<=m:
    print(max(buget))

else:
    while s<=e:
        mid=(s+e)//2
        count=0
        for i in buget:
            if i<=mid:
                count+=i
            else:
                count+=mid
        if count<=m:
            result=mid
            s=mid+1
        else:
            e=mid-1
    print(result)