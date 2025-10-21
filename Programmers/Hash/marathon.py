def solution(participant, completion):
    hash_map = {}
    for p in participant:
        hash_map[p] = hash_map.get(p, 0) + 1  # 참가자 카운트
    
    for c in completion:
        hash_map[c] -= 1  # 완주자 차감
    
    for k, v in hash_map.items():
        if v > 0:  # 남아 있는 사람이 답
            return k