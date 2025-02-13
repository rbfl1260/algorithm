#알고리즘 수업 - 병합 정렬 1
import sys

def merge_sort(arr,count):
    if len(arr)<=1:
        return arr,count
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    LEFT,count=merge_sort(left,count)
    RIGHT,count=merge_sort(right,count)
    return merge(LEFT,RIGHT,count)

def merge(left,right,count):
    i,j=0,0
    sorted_list=[]
    
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted_list.append(left[i])
            count+=1
            if count==k:
                print(left[i])
                return sorted_list, count

            i+=1
        else:
            sorted_list.append(right[j])
            count+=1
            if count==k:
                print(right[j])
                return sorted_list, count

            j+=1
    while i<len(left):
        sorted_list.append(left[i])
        count+=1
        if count==k:
            print(left[i])
            return sorted_list, count
        i+=1
    while j<len(right):
        sorted_list.append(right[j])
        count+=1
        if count==k:
            print(right[j])
            return sorted_list, count
        j+=1
    return sorted_list,count

n,k=map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))
count=0
sorted_list,count=merge_sort(numbers,count)
if count<k:
    print(-1)
