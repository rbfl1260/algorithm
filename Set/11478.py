import sys

# 서로 다른 부분 문자열의 개수
#순서상관 없음

def u_count(s):
    u_set = set()  # 서로 다른 부분 문자열을 저장할 집합

    n = len(s)
    # 부분 문자열을 생성
    for i in range(n):  # 시작 위치
        for j in range(i + 1, n + 1):  # 끝 위치
            u_set.add(s[i:j])  # 부분 문자열 추가

    return len(u_set)  # 서로 다른 부분 문자열의 개수 반환

# 문자열 입력
s = sys.stdin.readline().strip()
result = u_count(s)
print(result)
