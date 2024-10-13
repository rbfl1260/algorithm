#대칭 차집합

import sys

a,b=map(int,sys.stdin.readline().split())

A=set(sys.stdin.readline().split())
B=set(sys.stdin.readline().split())

A_B=A-B
B_A=B-A

print(len(A_B)+len(B_A))