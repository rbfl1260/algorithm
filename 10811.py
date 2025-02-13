n,m=map(int,input().split())
a = list(range(1, n + 1)) 

for k in range(m):
    b,c=map(int,input().split())
    i=b-1
    j=c-1
    while(i<j):
       a[i],a[j]=a[j],a[i]
       i+=1
       j-=1
print(' '.join(map(str, a)))
# a의 각 요소를 문자열로 변환한 후, 이들을 공백 문자로 연결하여 하나의 문자열로 출력
#map(str, a): 리스트 a의 각 요소를 str 함수를 사용하여 문자열로 변환합니다.
#' '.join(...): 변환된 문자열 요소들을 공백 문자 ' '를 구분자로 사용하여 하나의 문자열로 연결합니다.