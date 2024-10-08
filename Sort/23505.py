#커트라인

N,K=map(int,input().split()) #응시자 수, 수상자 수
score=[int(x) for x in input().split()]

#버블 정렬 사용
#2개씩 비교하면서 맨끝으로 가장 큰 값을 보냄
#비효율적이라 잘 사용하지 않음
for i in range(N):
    for j in range(N-1):
        if score[j]>score[j+1]:
            score[j],score[j+1]=score[j+1],score[j]

print(score[N-K])