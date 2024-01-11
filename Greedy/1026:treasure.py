n=int(input())
A=[int(x) for x in input().split()]
B=[int(x) for x in input().split()]

A.sort()
s=0
for j in range(0,n):
    max=0
    for i in range(0,len(B)):
        if max<B[i]:
            max=B[i]
    B.remove(max)
    s=s+A[j]*max
print(s)

# A와 B의 값 정수들의 리스트로 받음
# A오름차순으로 정렬
# 이중 for문 설정해서 리스트 B에서 max값 구한 후 제거하여 리스트 길이 줄임
# 그리고 리스트 A의 첫번째 요소부터 max를 곱해 누적 합을 s에 저장.
