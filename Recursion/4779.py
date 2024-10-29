#칸토어 집합
import sys

def Div(arr):
    if len(arr)==1:
        return arr
    val=len(arr)//3
    empty=arr[val:val+val]
    left=arr[:val]
    right=arr[val+val:]
    L=Div(left)
    R=Div(right)
    return Cantor(L,R,empty)

def Cantor(left,right,empty):
    res=[]
    for i in range(len(empty)):
        empty[i]=' '
    res=left+empty+right
    return res
    

while True:
    n=sys.stdin.readline().strip()
    if n:
        n=int(n)
        count=3**n
        arr=[]
        for i in range(count):
            arr.append('-')
        print(''.join(map(str,Div(arr))))
    else:
        break
