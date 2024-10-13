#숫자카드 2
#m개의 수에 대해 각 숫자카드를 상근이가 몇개 가지고 있는지 출력해야함
import sys

n=int(sys.stdin.readline())

n_list=sys.stdin.readline().split()
#한줄의 문자열을 입력받으므로 리스트로 만들어줌
m=int(sys.stdin.readline())

m_list=sys.stdin.readline().split()

n_count={}

for num in n_list:
    if num in n_count:
        n_count[num]+=1
    else:
        n_count[num]=1

print(n_count)
res=[n_count.get(num,0) for num in m_list]

print(' '.join(map(str,res)))