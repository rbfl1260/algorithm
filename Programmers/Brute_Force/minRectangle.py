def solution(sizes):
    answer = 0
    max_w=0
    max_h=0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0],sizes[i][1]=sizes[i][1],sizes[i][0]
        if sizes[i][0]>max_w:
            max_w=sizes[i][0]
        if sizes[i][1]>max_h:
            max_h=sizes[i][1]
    answer=max_w*max_h
    return answer

size=[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
solution(size)