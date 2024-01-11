s=int(input())
n=1
while n*(n+1)//2 <=s:#1부터 n까지 자연수의 합
    n+=1
#마지막 반복에서 n값은 s를 초과하는 첫번째 수이므로 n-1이 결과값
print(n-1)
