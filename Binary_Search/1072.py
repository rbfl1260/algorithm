#게임
#게임을 최소 몇 번 더 해야 z가 변하는지?
#z가 절대 변하지 않으면 -1 출력,

def binary_search(z,s,e):
    result=-1
    while s<=e:
        mid=(s+e)//2
        res=(y+mid)*100//(x+mid)
        # print(mid,res,z)
        if res>z:
            result=mid #작아지는거기 때문에 작은 값으로 계속 갱신됨,min쓰지 않아도 됨.
            e=mid-1
        elif res==z:
            s=mid+1
    print(result)

x,y=map(int,input().split())
z=y*100//x
# z=(y//x)*100 게속 이렇게 계산하려고 해서 안됐던거였음.
binary_search(z,1,x)

