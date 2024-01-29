#나무 자르기
#적어도 m미터라는건 더 가져가도 된다는 뜻.
def binary_search(arr,s,e):
    result=0
    while s<=e:
        count=0
        mid=(s+e)//2
        for i in arr:
            if i>mid:
                count+=i-mid
        if count>=m:
            result=max(result,mid)
            s=mid+1
        else:
            e=mid-1
    print(result)

n,m=map(int,input().split())
#m은 집에 가져가려고 하는 나무의 길이
tree=list(map(int,input().split()))
tree.sort()
binary_search(tree,0,max(tree))
#문제에서 높이는 양의 정수 또는 0이라 했기 때문에 0을 시작점으로 잡아야함.
#0으로 하면 이진탐색 시작점이 달라짐.
#1로 설정하면 나무 자르는 최소 높이가 1이 됨.(무조건 잘라야함)
#0으로 설정하면 나무를 전혀 자르지 않는 경우를 고려한 것임.