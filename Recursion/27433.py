#팩토리얼2

import sys

def factorial(N):
    if N==0:
        return 1
    else:
        return N*factorial(N-1)

n=int(sys.stdin.readline())
print(factorial(n))