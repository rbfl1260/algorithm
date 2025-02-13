# 문자열 반복

n=int(input())
for _ in range(n):
    r,s=input().split()
    S=[]
    for i in range(len(s)):
        R=int(r)
        while(R>0):
            S.append(s[i])
            R-=1
    print(''.join(map(str, S)))
            