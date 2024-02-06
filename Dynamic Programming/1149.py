#RGB거리
#i=집 개수, dp[i]=집이 i개일 때 최소 비용
n=int(input())
price=[list(map(int,input().split())) for i in range(n)]

dp=[[0]*3 for i in range(n)]

for k in range(3):
    dp[0][k]=price[0][k]

for i in range(1,n):
    for j in range(3):
        if j==0:
            dp[i][j]=min(price[i][j]+dp[i-1][j+1],price[i][j]+dp[i-1][j+2])
        elif j==1:
            dp[i][j]=min(price[i][j]+dp[i-1][j-1],price[i][j]+dp[i-1][j+1])
        else:
            dp[i][j]=min(price[i][j]+dp[i-1][j-1],price[i][j]+dp[i-1][j-2])
print(min(dp[n-1]))