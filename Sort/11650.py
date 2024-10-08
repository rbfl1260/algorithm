#좌표 정렬하기
N=int(input())
arr=[]
for i in range(N):
    x,y=map(int,input().split())
    arr.append([x,y])

arr.sort(key=lambda pair:(pair[0],pair[1]))

for x,y in arr:
    print(x, y)