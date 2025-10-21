def solution(nums):
    hash_map = {}
    maxValue=len(nums)//2
    for n in nums:
        hash_map[n] = hash_map.get(n, 0) + 1
    if len(hash_map)>maxValue:
        return maxValue
    else:
        return len(hash_map)

