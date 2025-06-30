#파도반 수열

MAX=100

dp=[0]*(MAX+1)
dp[1]=dp[2]=dp[3]=1
dp[4]=2

for i in range(5,MAX+1):
    dp[i]=dp[i-1]+dp[i-5]

t=int(input())
for _ in range(t):
    n=int(input())
    print(dp[n])