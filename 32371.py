#샷건

keyboard = [list(input()) for _ in range(4)]
note = input().strip()


def findKey(i,j):
     # 상하좌우 '샷건 조건' 확인
     if (keyboard[i - 1][j] in note and keyboard[i + 1][j] in note and
        keyboard[i][j - 1] in note and keyboard[i][j + 1] in note):
        print(keyboard[i][j])
        return


# 모든 위치 검사 후 샷건 조건 확인
for i in range(1, 3):
    for j in range(1, 9):
        if keyboard[i][j] in note:  # 문자가 note에 포함되면 검사
            findKey(i,j)
