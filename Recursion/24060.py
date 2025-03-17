#알고리즘 수업 - 병합 정렬 1
import sys

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=(len(arr)+1)//2
    left=arr[:mid]
    right=arr[mid:]
    LEFT=merge_sort(left)
    RIGHT=merge_sort(right)
    return merge(LEFT,RIGHT)

def merge(left,right):
    i,j=0,0
    sorted_list=[]
    global count,k
    
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted_list.append(left[i])
            count+=1
            if count==k:
                print(left[i])
                return sorted_list

            i+=1
        else:
            sorted_list.append(right[j])
            count+=1
            if count==k:
                print(right[j])
                return sorted_list
            j+=1
    while i<len(left):
        sorted_list.append(left[i])
        count+=1
        if count==k:
            print(left[i])
            return sorted_list
        i+=1
    while j<len(right):
        sorted_list.append(right[j])
        count+=1
        if count==k:
            print(right[j])
            return sorted_list
        j+=1
    return sorted_list

n,k=map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))
count=0
merge_sort(numbers)
if count<k:
    print(-1)
