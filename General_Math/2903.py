#중앙 이동 알고리즘

n=int(input())
side=1
for i in range(1,n+1):
    side=2**i
    count=(side+1)**2

print(count)
