N=int(input())
arr=[]
for i in range(N):
    S=input()
    if S not in arr:
        arr.append(S)
arr.sort()        
arr.sort(key=len)
for i in arr:
    print(i)