#숫자카드2
import bisect
def find_count(a,target):
    left_index=bisect.bisect_left(a,target)
    right_index=bisect.bisect_right(a,target)
    return right_index-left_index

n=int(input())
A=list(map(int,input().split()))
A.sort()
m=int(input())
M=list(map(int,input().split()))

for i in range(m):
    a=find_count(A,M[i])
    print(a)