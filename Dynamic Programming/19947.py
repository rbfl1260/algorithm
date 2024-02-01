#투자의 귀재 배주형

h,y=map(int,input().split())
dp=[0]*(y+1)
dp[0]=h

for i in range(1,y+1):
    dp[i]=int(dp[i-1]+dp[i-1]*0.05)
    if i>=3 and i<5:
        dp[i]=int(max(dp[i],dp[i-3]+dp[i-3]*0.2))
    elif i>=5:
        dp[i]=int(max(dp[i],dp[i-3]+dp[i-3]*0.2,dp[i-5]+dp[i-5]*0.35))

print(dp[y])
