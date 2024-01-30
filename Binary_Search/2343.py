#기타 레슨
#m개의 블루레이에 블루레이 크기를 최소로하여 녹화하려고 함.
#가능한 블루레이 크기중 최소를 출력
#mid는 블루레이 크기
def binary_search(arr,s,e):
    result=0
    while s<=e:
        mid=(s+e)//2
        res=1
        count=0
        for i in arr:
            if mid>=count+i:
                count+=i
            else:
                res+=1
                count=i
        if res>m:
            s=mid+1

        else:
            result=mid
            e=mid-1

    print(result)

# n=9,m=3
#
# left = 9 right = 45 mid = 27,  res = 2, result=27
#
# left = 9 right = 26 mid = 17, res = 3, result = 17
#
# left = 9 right = 16 mid = 12, res = 5, result = 17
#
# left = 13 right = 16 mid = 14, res = 5, result = 17
#
# left 15 right = 16 mid 15, res = 4, result = 17

#n개의 강의,m개의 블루레이
n,m=map(int,input().split())
lesson=list(map(int,input().split()))
s=max(lesson) #9로 시작해야함.
e=sum(lesson)
binary_search(lesson,s,e)

