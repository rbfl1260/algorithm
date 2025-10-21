def solution(s):
    answer=True
    stack=list()
    for ch in s:
        if ch=='(':
            stack.append(ch)
        else:
            if not stack:
                answer=False
                return answer
            stack.pop()
    if not stack:
        return answer
    else:
        answer=False
        return answer

s="(()("	
print(solution(s))