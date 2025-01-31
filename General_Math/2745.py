#진법 변환

n,b=input().split()

ToTen={
    chr(i): v for i, v in zip(range(ord('A'),ord('Z')+1),range(10,36))
}
b=int(b)
print(int(n,b))