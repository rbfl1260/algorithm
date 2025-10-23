from functools import cmp_to_key

def solution(numbers):
    num_strings=list(map(str,numbers))
    
    def compare(a,b):
        if a+b>b+a:
            return -1
        elif a+b < b+a:
            return 1
        else:
            return 0
    
    num_strings.sort(key=cmp_to_key(compare))

    answer=''.join(num_strings)
    return '0' if answer[0]=='0' else answer

num=[6,10,2]
solution(num)