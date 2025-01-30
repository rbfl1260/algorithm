#최댓값

arr=[list(map(int,input().split())) for _ in range(9)]

maxVal=0
maxI=0
maxJ=0
for i in range(9):
    for j in range(9):
        if arr[i][j]>maxVal:
            maxVal=arr[i][j]
            maxI=i
            maxJ=j
print(maxVal)
print(maxI+1, maxJ+1)
