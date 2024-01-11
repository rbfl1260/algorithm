n,m=map(int,input().split())
a=[list(map(int,input())) for _ in range(n)]
b=[list(map(int,input())) for _ in range(n)]
c=0

if(n>=3 and m>=3):
    for i in range(n-2):
        for j in range(m-2):
            if a[i][j] != b[i][j]:
                x=i
                y=j
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        a[x][y]=1-a[x][y]
                c+=1
if a==b:
    print(c)
else:
    print(-1)
