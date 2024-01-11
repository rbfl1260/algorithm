n= int(input())
# t=list(input().split())
#이렇게 하면 리스트길이가 마음대로임.
t=[int(x) for x in input().split()]
# t=[int(input()) for i in range(n)] -> 값을 엔터 쳐서 하나씩 받아야 함.
t.sort()
s=0
total=0
for i in range(0,n): # n 써줘야 함. 안써주면 오류 남.
    s+=t[i]
    total+=s
print(total)

#정수 n을 받고, 정수들의 리스트를 t에 넣음
#t 오름차순으로 정렬.
#for문을 통해 t[i]의 누적값을 s에 저장
#total에 s의 누적값을 더해 출력함.

# input() 함수를 사용하여 사용자로부터 입력을 받습니다.
# input() 함수로 받은 문자열을 split() 함수를 사용하여 공백을 기준으로 나눕니다.
# for x in input().split()은 이렇게 나뉜 부분들을 하나씩 가져와서 변수 x에 할당하는 반복문입니다.
# int(x)는 각 부분을 정수로 변환합니다.
# 이렇게 변환된 정수를 리스트로 저장하기 위해 리스트 내포(list comprehension)를 사용하여 t라는 리스트에 넣습니다.