#거스름돈
r=int(input())

c=0
while(True):
    if r%5==0:
        c+=r//5
        r%=5
    else:
        r-=2
        c+=1
    if r<0:
        print(-1)
        break
    if r==0:
        print(c)
        break

