#별 찍기 - 7

n=int(input())
max=2*n-1
count=1


for i in range(n):
    start= (max-count)//2
    print(' '*start, end='')
    print('*'*count)
    count+=2

count-=4
for _ in range(n-1):
    start= (max-count)//2
    print(' '*start, end='')
    print('*'*count)
    count-=2
