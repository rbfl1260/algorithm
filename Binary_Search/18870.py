#좌표압축
#작은 값을 0으로 두고 차례로 설정함.
#bisect로 푸는게 훤씬 간단함. =>bisect_left사용해서!
#새로운 배열을 만들고 이진탐색 사용해서 기존배열과 비교하여 값이 같다면
#새로운 배열의 인덱스 값을 기존배열에 부여한다.
def binary_search(a):
    for i in A: #이 for문을 생각못해서 오래 걸림.^^
        s=0
        e=len(a)-1
        while s<=e:#while문 끝나고 나서 각 값마다 다시 돌아야 하므로 s,e따로 설정.
            mid=(s+e)//2
            if i==a[mid]:
                print(mid,end=' ')
                break
            elif i<a[mid]:
                e=mid-1
            else:
                s=mid+1

n=int(input())
A=list(map(int,input().split()))
a=sorted(list(set(A))) #중복요소 제거->리스트로 변환->오름차순 정렬->새로운 리스트 생성

binary_search(a)
