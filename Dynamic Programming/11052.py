#카드 구매하기

n=int(input()) #n개 구매하려고 함.
p=list(map(int,input().split()))
# p.insert(0,0)
dp=[0]*(n+1)
dp[1]=p[0]
for i in range(2,n+1):
    #i개 살때마다 dp[i]=카드 i개 구매하는 최대 가격
    dp[i]=p[i-1]
    for j in range(1,i):
        dp[i]=max(dp[i],dp[i-j]+dp[j])
print(dp[n])

