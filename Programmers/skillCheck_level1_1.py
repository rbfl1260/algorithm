#양의 정수 -> x의 제곱일 때

import sys

def solution(n):
    x=n** 0.5
    if x.is_integer():
        return int((x+1)**2)
    else:
        return -1
    
input=sys.stdin.read().strip()

if not input:
    print('값이 없음')
else:
    n=int(input)
    print(solution(n))
