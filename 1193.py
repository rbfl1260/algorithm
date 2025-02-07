#분수 찾기

x=int(input())

n=1
while x>n*(n+1)//2:
    n+=1

start=n*(n-1)//2 +1

offset=x-start
# 짝수/홀수에 따라 분수 계산
if n % 2 == 0:
    a = 1 + offset
    b = n - offset
else:
    a = n - offset
    b = 1 + offset

print(f"{a}/{b}")