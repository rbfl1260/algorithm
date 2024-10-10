#좌표 압축

#좌표를 똑같은 간격차로 줄였다는게 아니라 좌표 압축의 뜻 자체가 
#순서(랭킹)을 매긴다고 생각하면 됨. 오름차순으로 0부터
import sys

N=int(sys.stdin.readline())

arr=list(map(int,sys.stdin.readline().split()))

sorted_numbers = sorted(arr)

ranking=[sorted_numbers.index(num) for num in arr]

for i in ranking:
    print(i,end=' ')
