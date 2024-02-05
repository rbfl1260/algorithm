#계단 오르기
#dp[i]의 값은 현재 얻은 최대 점수
#i는 현재 층수
#max쓰면 안됨! 총 점수 최댓값이 안나옴.
#그럼 어케?? 현재 최대가 아니라 마지막 최대?
#현재 층수에 가질 수 있는 값들을 전부 넣어야 하나?
stair=int(input())
score=[int(input()) for i in range(stair)]
score.insert(0,0)
dp=[0]*(stair+1)
dp[1]=score[1] #dp[1]=10
dp[2]=dp[1]+score[2]
dp[3]=max(dp[1]+score[3],dp[2]+score[3])

for i in range(4,stair+1):
    dp[i]=max(dp[i-3]+score[i-1]+score[i],dp[i-2]+score[i])
    #이전칸을 밟냐,안밟냐에 따라서 정해짐.
print(dp[stair])