#분해합

from itertools import product

N=input()
nums=list(range(10))
maxVal= -1

for comb in product(nums,repeat=len(N)):
    total=sum(comb)
    number=int(''.join(map(str,comb)))
    if number<int(N):
        if total+number==int(N):
            maxVal=max(maxVal,total)
if maxVal==-1:
    print(0)
else:
    print(int(N)-maxVal)