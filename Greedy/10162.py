#전자레인지
T=int(input())
s=[5*60,60,10]
s1=[]
while T>10:
    for i in range(len(s)):
        c=0
        if(T>=s[i]):
            c=T//s[i]
            s1.append(c)
            T=T%s[i]
        elif(T<s[i]):
            s1.append(0)
if(T!=0 and T<10):
    print(-1)
else:
    for i in s1:
        print(i, end=" ")
