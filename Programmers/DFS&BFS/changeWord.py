from collections import deque

def solution(begin, target, words):
    answer = 0
    queue=deque()
    queue.append([begin,answer])
    visited=[False for _ in range(len(words))]

    while queue:
        begin,answer=queue.popleft()
        if begin==target:
            return answer
        for i in range(len(words)):
            if diff_one(begin,words[i]) and visited[i]==False:
                #begin은 현재 레벨 단어, 다음 단어로 직접 바꿔버리면 BFS의 구조 깨짐.
                queue.append([words[i],answer+1])
                visited[i]=True
    return 0

def diff_one(a,b):
    if len(a)!=len(b):
        return False
    else:
        diffCount=0
        for i in range(len(a)):
            if a[i]!=b[i]:
                diffCount+=1
        if diffCount>1:
            return False
        elif diffCount==1:
            return True
        

begin='hit'
target='cog'
words=["hot", "dot", "dog", "lot", "log", "cog"]
solution(begin,target,words)