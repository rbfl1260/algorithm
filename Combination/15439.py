#베라의 패션
from itertools import combinations

n=int(input())
# count=0
# for i in range(n):
#     for j in range(i+1,n):
#         count+=1
# print(count*2)
nums=list(range(n))
count2=list(combinations(nums,2))
print(len(count2)*2)

