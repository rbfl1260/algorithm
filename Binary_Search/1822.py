#차집합
def binary_search(b,target,s,e,c,listC):

    if s>e:
        c+=1
        listC.append(target)
        return c
    mid=(s+e)//2

    if b[mid]==target:
        return 0

    elif b[mid]>target:
        e=mid-1
        return binary_search(b,target,s,e,c,listC)
    else:
        s=mid+1
        return binary_search(b,target,s,e,c,listC)

n_A,n_B=map(int,input().split())
listA=list(map(int,input().split()))
listB=list(map(int,input().split()))
listA.sort()
listB.sort()
listC=[]
c=0
res=0
for i in listA:
    res+=binary_search(listB,i,0,n_B-1,c,listC)

# listC.sort() 정렬 없어도 됨. 정렬돼서 들어감 어차피
if not listC: #빈 배열이면 0츌력
    print(0)
else:
    print(res)#비어있지 않다면 res출력
    for i in listC:#listC의 값들 출력
        print(i,end=" ")