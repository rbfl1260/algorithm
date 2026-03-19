N=int(input())
number=int(input())

def solution(N, number):
    dp=[set() for _ in range(9)]
    for i in range(1,9):
        dp[i].add(int(str(N)*i))
        #str(N)*i는 N이 i개 붙은 수를 의미. 예를 들어 N=5, i=3이면 555가 됨.
        for j in range(1,i):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a+b)
                    dp[i].add(a-b)
                    dp[i].add(a*b)
                    if b!=0:
                        dp[i].add(a//b)
        if number in dp[i]:
            return i
    return -1
