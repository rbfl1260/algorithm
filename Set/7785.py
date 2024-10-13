#회사에 있는 사람
#대소문자 구분해야함

import sys

n=int(sys.stdin.readline())
e=set()
#기록된 출입의 수
for i in range(n):
    name, state=sys.stdin.readline().strip().split()
    if state=='enter' and name not in e:
        e.add(name)
    if state=='leave' and name in e:
        e.remove(name)

for i in sorted(e,reverse=True):
    print(i)
