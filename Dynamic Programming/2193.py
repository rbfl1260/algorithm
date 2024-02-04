#이친수

#이진수 중 특별한 성질을 갖는 것들이 있음=>이친수
#0으로 시작하지 않음. 1이 연속 두번으로 나타나지 않음
#인덱스가 자릿수
#dp[i]=i에서의 최대 이친수 개수

n=int(input())
dp=[1]*(n+1)
for i in range(3,n+1):
    dp[i]=dp[i-2]+dp[i-1]
print(dp[n])

# dp[1]=1 1개
# dp[2]=10 1개
# dp[3]=101 100 2개
# dp[4]=1010 1001 1000 3개
# dp[5]=10100, 10010, 10000, 10101, 10001 5개
# dp[i-1]에서 0붙인 것+[i-2]에서 01 붙인것 =>이 규칙 찾으면=> 피보나치 수열

