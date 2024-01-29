#과자 나눠주기
#같은 길이의 과자를 나눠주는데, 1명에게 줄 수 있는 최대 길이구하기
#나눌 수는 있으나 합칠 수는 없음
#왜 이분탐색?써야하지? 수가 커서??
#인덱스로만 생각하면 안됨. mid가 값 자체라고 생각하고 풀 수도 있음.

def binary_search(arr,s,e):
    result=0
    while s<=e:
        count=0
        mid=(s+e)//2
        for i in arr:
            if i>=mid:
                count+=i//mid
            # else:
            #     break

        # if count==m:
        #     return mid
        #반환조건이 문제? => count가 m조카수 이상이면서 최대길이 찾아야함.

        if count>=m: #과자가 더 많아도 됨.
            # print(result,mid)
            result=max(result,mid)#가장 긴 과자길이
            # result=mid 이렇게 하면 틀림.
            s=mid+1
        else:
            e=mid-1
    print(result)

m,n=map(int,input().split())#m은 조카 수
n_len=list(map(int,input().split())) #과자 길이 배열
n_len.sort()
binary_search(n_len,0,max(n_len))
#zerodivisionerror가 생기는 이유는 최소값이 0으로 시작하기 때문.
#1로 시작해야함.과자의 길이는 양의 정수라고 했으니.!
#문제 잘 읽는게 중요한듯. 문제 잘못읽으면 바로 틀림