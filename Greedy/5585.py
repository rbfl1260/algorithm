p=int(input())
m=1000-p
r=[500,100,50,10,5,1]
c=0
i=0
while(m!=0):
    if m>=r[i]:
        c+=m//r[i]
        m=m%r[i]
    i+=1
print(c)