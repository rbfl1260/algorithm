#수 정렬하기3
#이 문제는 메모리 제한이 너무 적어서 sort사용 불가능. 
# 숫자 입력받기 위해 input을 사용해도 메모리 초과 => readline사용해야함
# 나머지 알고리즘으로는 풀 수 없음. 계수정렬 알고리즘으로 풀어야함
import sys

# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr
#     mid=len(arr)//2
#     left=arr[:mid]
#     right=arr[mid:]
#     LEFT=merge_sort(left)
#     RIGHT=merge_sort(right)
#     return merge(LEFT,RIGHT)

# def merge(left,right):
#     i,j=0,0
#     sorted_list=[]
#     while i<len(left) and j<len(right):
#         if left[i]<right[j]:
#             sorted_list.append(left[i])
#             i+=1
#         else:
#             sorted_list.append(right[j])
#             j+=1
#     while i<len(left):
#         sorted_list.append(left[i])
#         i+=1
#     while j<len(right):
#         sorted_list.append(right[j])
#         j+=1
#     return sorted_list


N=int(sys.stdin.readline())
arr=[0]*10001
for _ in range(N):
    index=int(input())
    arr[index]+=1

for i in range(1,len(arr)):
    if arr[i]!=0:
        for j in range(arr[i]):
            print(i)