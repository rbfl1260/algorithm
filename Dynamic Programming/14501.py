#퇴사

#금액 신경써야함.
#상담 가능한 경우
# 8=> 6,7 없고(7+2=9,6+4=10)
# 5=> 5,6
# 4=>4
# 3=>3
# 2=>2+5 7 이내 이므로 넣을 수 있음.
# 1=>1+3 7이내 이므로 넣을 수 있음.

# 내가 현재 날짜일 때 상담을 할건지 안할건지.
# 상담한다 => 상담중이지 않음
# dp[i+ti]+pi=>상담하는 경우
# dp[i+1]

#일을 하지 않은 경우
# dp[5]=2
# dp[4]=dp[4+1]

n=int(input())
time=[]
price=[]
for i in range(n):
    t,p=map(int,input().split())
    time.append(t)
    price.append(p)

dp=[0]*(n+1)
# 0 0 0 0 0 0 0 0  n=7
for i in range(n-1,-1,-1): #인덱스 맞추기 위해 n-1에서 시작
    if i+time[i]<=n:
        dp[i]=max(dp[i+1],dp[i+time[i]]+price[i])
    else:
        dp[i]=dp[i+1]

print(dp[0])