#진법 변환2

n,b=map(int,input().split())
arr=[]
NtoA={v:chr(i) for v,i in zip(range(10,36),range(ord('A'),ord('Z')+1))}

while n>0:
    val=n%b
    if val>=10:
        val=NtoA[val]
    arr.append(val)
    n=n//b

print(''.join(map(str,reversed(arr))))