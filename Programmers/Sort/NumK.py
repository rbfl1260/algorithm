def solution(array, commands):
    answer = []
    for n in range(len(commands)):
        i=commands[n][0]
        j=commands[n][1]
        k=commands[n][2]
        new_array=array[i-1:j]
        sorted_array=sorted(new_array)
        answer.append(sorted_array[k-1])
    print(answer)
array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

solution(array,commands)