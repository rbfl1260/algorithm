def solution(answers):
    answer = []
    numThree=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    numTwo=[2, 1, 2, 3, 2, 4, 2, 5]
    numOne=[1,2,3,4,5]

    count1=0
    count2=0
    count3=0
    for i in range(len(answers)):
        if answers[i]==numOne[i%len(numOne)]:
            count1+=1
        if answers[i]==numTwo[i%len(numTwo)]:
            count2+=1
        if answers[i]==numThree[i%len(numThree)]:
            count3+=1
    max_val=max(count1,count2,count3)
   
    if count1==max_val:
        answer.append(1)
    if count2==max_val:
        answer.append(2)
    if count3==max_val:
        answer.append(3)
            
    return answer

nums=[1,2,3,4,5]	
solution(nums)