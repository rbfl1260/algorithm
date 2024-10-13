#듣보잡

import sys

n,m=map(int,sys.stdin.readline().split())

no_listen=set([sys.stdin.readline().strip() for _ in range(n)])
no_see=set([sys.stdin.readline().strip() for _ in range(m)])

no=no_listen&no_see

print(len(no))
for i in sorted(no):
    print(i)