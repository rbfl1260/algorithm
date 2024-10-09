#좌표 정렬하기
N=int(input())
arr=[]
for i in range(N):
    x,y=map(int,input().split())
    arr.append([x,y])

arr.sort(key=lambda pair:(pair[0],pair[1]))
#이렇게 굳이 안하고 그냥 arr.sort()해도 됨. 왜냐면 기본적으로 첫번째 요소를 기준으로 정렬하고
#첫번쨰 원소가 같다면 두번째 요소를 기준으로 정렬해주기 때문에.

for x,y in arr:
    print(x, y)