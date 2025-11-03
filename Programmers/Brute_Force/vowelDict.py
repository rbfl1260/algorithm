#모음 사전
from itertools import product

def solution(word):
    answer = 0
    vowels=['A','E','I','O','U']
    words=[]
    for length in range(1,6):
        for p in product(vowels,repeat=length):
            words.append(''.join(p))

    words.sort()
    count=0
    for i in words:
        count+=1
        if i==word:
            print(count)
            return count
words="AAAAE"
solution(words)