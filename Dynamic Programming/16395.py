#파스칼의 삼각형
#n번째 행, k번째 수 출력

n,k=map(int,input().split())
dp=[[1] for i in range(n+1)] #2차 배열
#1로 시작하기 때문에 처음부터 1로 초기화
if n==1:
    print(1)
#n==1일 경우 따로 처리해주지 않으면 dp[2]에 값을 넣으려고 해서 인덱스 에러 남.
else:
    dp[2]=[1,1]
    for i in range(3,n+1):
        for j in range(1,i-1):
            sum=0
            sum=dp[i-1][j]+dp[i-1][j-1]
            dp[i].append(sum)
        dp[i].append(1)
    print(dp[n][k-1])