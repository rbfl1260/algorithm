#좌표 정렬하기 2

N=int(input())
arr=[]
for i in range(N):
    x,y=map(int,input().split())
    arr.append([x,y])

arr.sort(key=lambda pair:(pair[1],pair[0]))

for x,y in arr:
    print(x, y)