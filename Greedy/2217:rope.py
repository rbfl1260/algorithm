n=int(input())
a=[int(input()) for i in range(0,n)]
max=0
a.sort(reverse=True)
print(a)
for i in range(0,n):
    if ((i+1)*a[i]) >= max:
        max=(i+1)*a[i]
print(max)

#큰값순으로 정렬
#로프들 중 최소중량 * N
#첫번째 로프=> a[i]*1
#두번째 로프=> a[i+1]*2 (a[i+1]이 더 작으므로 최소중량)
