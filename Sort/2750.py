#수 정렬하기

N=int(input())

arr = [int(input()) for _ in range(N)]

#삽입정렬
# for i in range(N):
#     for j in range(i):
#         if arr[j]>arr[i]:
#             arr[j],arr[i]=arr[i],arr[j]

for i in arr:
    print(i)
