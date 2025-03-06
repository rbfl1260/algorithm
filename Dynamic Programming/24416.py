#알고리즘 수업 - 피보나치 수 1

n=int(input())
arr=[]
a=1
b=1
val=0
for i in range(3,n+1):
    val=a+b
    a=b
    b=val
print(val,n-2)