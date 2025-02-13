#상수

a,b=input().split()
A=''.join(reversed(a))
B=''.join(reversed(b))

#a.reverse()는 문자열에서는 쓸 수 없음. 리스트에서 사용함.
#문자열을 리스트로 변환해서 사용하거나, reversed를 사용해서 join으로 다시 묶어주는 방법 사용.

A=int(A)
B=int(B)

if A>B:
    print(A)
else:
    print(B)