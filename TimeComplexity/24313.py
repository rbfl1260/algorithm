#알고리즘 수업 - 점근적 표기 1

#기준함수도 일차함수여야하므로 g(n)=n

a1,a0=map(int,input().split())
c=int(input())
n0=int(input())
n=n0
f_n=a1*n+a0
g_n=n
res=2
while n0<=n<=100:
    if f_n>c*g_n:
        res=0
        break
    n+=1
if res==0:
    print(0)
else:
    print(1)