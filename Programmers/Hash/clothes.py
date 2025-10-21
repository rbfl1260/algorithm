#의상

def solution(clothes):
    hash_map={}
    for cloth in clothes:
        category=cloth[1]
        item=cloth[0]
        hash_map.setdefault(category,[]).append(item)
    #위처럼 해도 됨. 아래를 간단하게 만든 것
       
    # for cloth in clothes:
    #     category=cloth[1]
    #     item=cloth[0]
    #     if category in hash_map:
    #         hash_map[category].append(item)
    #     else:
    #         hash_map[category]=[item]
    print(hash_map)
    count=1
    for k,v in hash_map.items():
        count*=len(v)+1
    print(count-1)

clothes=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)