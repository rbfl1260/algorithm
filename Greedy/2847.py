#게임을만든 동준이
#아직 안품
n=int(input())
a=list(int(input()) for i in range(n))
c=0
k=n-2
max=a[n-1]
while(k>-1):
    if max>a[k]:
        k-=1
        max=a[k]

    else:
        while(max<=a[k]):
            a[k]-=1
            c+=1
        max=a[k]
        k-=1
print(c)
