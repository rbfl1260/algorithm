n=int(input())
c=0
while n>0:
    # 5의 배수 -> 5kg로 먼저 나눔.
    if n%5==0:
        c=c+n//5
        n=n-(n//5)*5
    else:
        # 5의 배수 x, -3 -> 5의 배수로 만듦 -> 위의 if문에서 n=0.
        #-> 5의 배수 만들어지지x -> -3 -> n이 음수.
        # 3의 배수-> -3 -> n=0.
        n=n-3
        c+=1
    if n==0:
        print(c)
if(n<0):
    print(-1)


