#팰린드롬인지 확인하기

s=input()
reverse_s=''.join(reversed(s))
if s==reverse_s:
    print(1)
else:
    print(0)