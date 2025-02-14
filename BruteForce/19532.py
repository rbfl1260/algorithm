a, b, c, d, e, f = map(int, input().split())

# 연립방정식의 해 계산
x = (c * e - b * f) // (a * e - b * d)
y = (a * f - c * d) // (a * e - b * d)

print(x, y)
