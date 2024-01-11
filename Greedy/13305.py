#주유소
#1km 당 1L기름 사용
#다음수보다 작으면 다음수의 거리까지 가줌.
#n-1도시일때는 크기 상관없이 그냥 곱해줘야함.
import sys
n=int(input())
s1=list(map(int,sys.stdin.readline().split()))
s2=list(map(int,sys.stdin.readline().split()))
sum=s1[0]*s2[0]
length=len(s2)-1
i=1
while i<n-1:
    if i==n-2:
        sum+=s1[n-2]*s1[n-2]
        break
    if s2[i]<=s2[i+1]:
        sum+=s2[i]*(s1[i]+s1[i+1])
        length-=2
        i+=2
print(sum)


