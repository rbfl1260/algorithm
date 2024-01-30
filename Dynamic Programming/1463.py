#1로 만들기
#d[i]에 연산횟수 저장.
n=int(input())
dp=[0]*(n+1)
# dp[0]=>계산할 필요없음
# dp[1]=0 이미 1이기 때문에 계산할 필요없음
for i in range(2,n+1):

    dp[i]=dp[i-1]+1

    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)

    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)

    #예를 들어 n=4이면
    # dp[2]=dp[1]+1=1
    # 2%2==0이므로 dp[2]=min(1,1) => dp[2]=1

    # dp[3]=dp[2]+1=2
    # 3%3==0이므로 dp[3]=min(2,1) => dp[3]=1

    # dp[4]=dp[3]+1=3
    # 4%2==0이므로 dp[4]=min(3,2) => dp[4]=2

print(dp[n])