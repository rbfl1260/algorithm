#숫자 카드

import sys

N=int(sys.stdin.readline())
#상근이가 가지고 있는 숫자 카드의 개수
N_nums=list(map(int,sys.stdin.readline().split()))
#상근이가 가진 숫자 카드들에 적혀진 숫자

M=int(sys.stdin.readline())

M_nums=list(map(int,sys.stdin.readline().split()))

M_nums_dict = {value: 0 for value in M_nums}

sets=list(set(N_nums)&set(M_nums))

for value in sets:
    if value in M_nums_dict:
        M_nums_dict[value] = 1
    else:
        M_nums_dict[value] = 0

for i in M_nums_dict.values():
    print(i,end=' ')