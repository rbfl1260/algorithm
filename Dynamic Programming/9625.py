#BABBA
#모든 B는 BA로 바뀌고, A는 B로 바뀜.
#K번 눌렀을 때, 화면에 A와 B의 개수는 몇 개가 될까?

k=int(input())

if k==1:
    print(0,1)

else:
    dp=[0]*(k+1)
    dp[0]=1 #기본값 A일 때(문자열 길이)
    #인덱스가 누른 횟수.
    dp[1]=1 #A->B(문자열 길이)

    for i in range(2,k+1):
        dp[i]=dp[i-1]+dp[i-2]

    dp[k]=5
    print(dp[k-2],dp[k-1])

#문자열 길이
# dp[2]=2 BA
# dp[3]=3 BAB
# dp[4]=5 => 4번 눌렀을 때, 5글자.
#B는 전 문자열의 길이. A는 전 문자열의 B의 개수(=B의 개수는 그 전 문자열의 길이.)

#피보나치 수열


