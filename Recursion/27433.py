#팩토리얼2

import sys

def factorial(N):
    if N<1:
        return N
    else:
        N=N*factorial(N-1)

n=int(sys.stdin.readline())

if n==0:
    print(1)
else:
    factorial(n)