#알고리즘의 수행 시간 6

n=int(input())
res=0
for i in range(1,n-1):
    val=(i*(i+1))//2
    res+=val
print(res)
print(3)