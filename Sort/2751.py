#수 정렬하기2
#시간복잡도가 O(n^2)인 알고리즘으로는 풀 수 없음
#퀵,합병 등을 사용해야함 또는 내장 함수.
#import sys를 사용해서 한번에 입력받는것도 도움될 듯

N=int(input())
num=[int(input()) for _ in range(N)]

# for i in range(N):
#     min_idx=i
#     for j in range(i+1,N):
#        if num[min_idx] > num[j]:
#            min_idx=j

#     num[i],num[min_idx]=num[min_idx],num[i]
num.sort()
for i in num:
    print(i)