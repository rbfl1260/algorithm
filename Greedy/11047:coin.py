n,k=map(int,input().split())
a=[int(input()) for i in range(0,n)]

i=n-1
c=0

while(k!=0):
    if k>=a[i]:
        c+=k//a[i]
        k=k%a[i]
    i-=1
print(c)

# 동전의 가치가 오름차순으로 주어졌으므로 i값을 n-1로 잡아 가장 큰 수의 동전부터
# 사용하도록 함. 몫->동전 개수, 남은가격->나머지