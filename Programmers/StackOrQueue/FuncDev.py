import math

def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]

    count = 1
    max_day = days[0]  # 기준 일수 설정

    for i in range(1, len(days)):
        if days[i] <= max_day:
            count += 1
        else:
            answer.append(count)
            count = 1
            max_day = days[i]  # 새로운 기준으로 갱신

    answer.append(count)
    return answer