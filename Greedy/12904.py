#A와B
#T를 보고 s랑 비교하는 식으로 접근
s=list(input())
t=list(input())
s = len(s)- 1
t = len(t)- 1

for i in range(t, s, -1):
    if t[i]=='A':
        del t[i]
    else:
        del t[i]
        t.reverse()

if s==t:
    print(1)
else:
    print(0)
