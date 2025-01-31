#세로 읽기

arr=[list(input()) for _ in range(5)]
max_length=max(len(row) for row in arr)
min_length=min(len(row) for row in arr)

#가장 긴 줄 길이어 맞춰 공백으로 채우기
if min_length != max_length:
    for row in arr:
        while len(row)<max_length:
            row.append(' ')

res=[]

#세로 읽기(공백 제외)
for i in range(max_length):
    for j in range(5):
        if arr[j][i]!=" ":
            res.append(arr[j][i])
print(''.join(map(str,res)))