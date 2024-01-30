#보석 상자
#아이들의 수 N, 색상의 수 M
#이진탐색은 원본 데이터를 변경하지 않고 탐색조건만으로 최적의 값을 찾아야함.
#mid=한 사람이 가져가는 보석의 수

n,m=map(int,input().split())
color=[int(input()) for i in range(m)]
color.sort()
s=0  #보석을 받지 않아도 되는 학생이 있음
e=max(color) #색 섞이지 않으며 max
result=0

while s<=e:
    mid=(s+e)//2
    count=0

    for i in range(len(color)):
        if color[i]%mid==0:
            count+=color[i]//mid
        else:
            count+=(color[i]//mid)+1 #학생이 전부다 비슷하게 받아야 하는건 아님,
            #나눠서 남는 수까지 학생에게 주는 것임. 단지 제일 많이 받는애가 제일 최소로 받게만 해주면 됨.

    if count>n:
        s=mid+1
    else:
        result=mid
        e=mid-1
print(result)

# 7 4
#
# left = 0 right = 7 mid = 3 → 3 3 1, 3 1 count = 5 result = 3
#
# left = 0 right = 2 mid = 1 → count = 11
#
# left = 2 right = 2