#타겟 넘버
def solution(numbers, target):
    answer = dfs(numbers,0,0,target)
    return answer

def dfs(arr,n,current_sum,target):
    if n==len(arr):
        return 1 if current_sum==target else 0
    plus=dfs(arr,n+1,current_sum+arr[n],target)
    minus=dfs(arr,n+1,current_sum-arr[n],target)

    return plus+minus

# num=[1, 1, 1, 1, 1]
# solution(num,3)