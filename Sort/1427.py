#소트인사이드

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    LEFT=merge_sort(left)
    RIGHT=merge_sort(right)
    return merge(LEFT,RIGHT)

def merge(left,right):
    i,j=0,0
    sorted_list=[]
    while i<len(left) and j<len(right):
        if left[i]>right[j]:
            sorted_list.append(left[i])
            i+=1
        else:
            sorted_list.append(right[j])
            j+=1
    while i<len(left):
        sorted_list.append(left[i])
        i+=1
    while j<len(right):
        sorted_list.append(right[j])
        j+=1
    return sorted_list

num=input()
numbers = list(map(int, str(num)))
res=merge_sort(numbers)

for i in res:
    print(i,end='')
