#소수 찾기
from itertools import permutations

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return False
    return True

def solution(numbers):
    nums=set()
    for i in range(1,len(numbers)+1):
        for p in permutations(numbers,i):
            num=int("".join(p))
            nums.add(num)
    count=0
    for n in nums:
        if is_prime(n):
            count+=1
    return count

numbers="011"
solution(numbers)