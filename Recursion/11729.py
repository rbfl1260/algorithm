#하노이 탑 이동 순서

n=int(input())
#원판의 개수
def hanoi(num,start,mid,end):
    #start: 현재 원판이 놓여있는 기둥
    # mid: 보조 기둥
    # end: 목표 기둥
    if num==1:
        print(start, end)
    else:
        hanoi(num-1,start,end,mid)
        # 제일 큰 원판 제외한 num-1개의 원판을 start->mid로 옮김
        print(start,end)
        # 가장 큰 원판 1개를 start->end로 옮김
        hanoi(num-1,mid,start,end)
        # mid로 옮겨놓은 num-1개의 원판을 mid->end로 옮김
print(2**n-1)
hanoi(n,1,2,3)