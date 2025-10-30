#피로도
#정렬을 하는게 아니라 모든 경우를 다해봐야함. 순열사용해서 모든 순서 만들어본 뒤
#직접 실행해봐야 알 수 있음
from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for i in permutations(dungeons,len(dungeons)):
        current_k=k
        count=0
        for need,use in i:
            if current_k>=need:
                current_k-=use
                count+=1
        answer=max(answer,count)
            
    return answer

k=80
dun=[[80,20],[50,40],[30,10]]
solution(k,dun)