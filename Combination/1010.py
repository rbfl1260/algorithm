#다리 

import math

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    result=math.comb(m,n)
    # 오름차순으로 동쪽사이트에서 N개를 고르는 조합이기 때문이므로 다리가 겹치지 않음
    print(result)