#문자열

n=int(input())
for _ in range(n):
    s=input()
    l=len(s)
    print(f"{s[0]}{s[l-1]}")
    #: f-string을 사용하여 문자열 내에 변수 값을 삽입
    # {} 중괄호 안에 변수나 표현식을 넣어 사용할 수 있음
    