#세로 읽기

arr=[list(input()) for _ in range(5)]
max_length=max(len(row) for row in arr)
min_length=min(len(row) for row in arr)


if min_length != max_length:
    for row in arr:
        while len(row)<max_length:
            row.append(' ')

res=[]

for i in range(max_length):
    for j in range(5):
        if arr[j][i]!=" ":
            res.append(arr[j][i])
print(''.join(map(str,res)))