#색종이

arr=[[0]*100 for _ in range(100)]
n=int(input())

for i in range(n):
    x,y=map(int,input().split())
    
    for j in range(x-1,x+9):
        for k in range(y-1,y+9):
            if arr[j][k]==0:
                arr[j][k]=1

count=sum(row.count(1) for row in arr)
print(count)
