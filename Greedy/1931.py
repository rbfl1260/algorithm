#회의실 배정
# import sys
# n=int(input())
# s1=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# s2=[]
# for i in range(len(s1)):
#     s1[i].append(s1[i][1]-s1[i][0])
# s1.sort(key=lambda x:(x[2],x[0]))
# j=0
# c=0
# s3=[]
# print(s1)
# while(j<n):
#     f=0
#     if s1[j][0]==s1[j][1]:
#         s3.append(s1[j][0])
#     else:
#         while s1[j][0]!=s1[j][1]:
#             s3.append(s1[j][0])
#             s1[j][0]+=1
#     for i in range(0,len(s3)):
#         if s3[i] in s2:
#             f=-1
#             break
#     if f==0:
#         for i in range(len(s3)):
#             s2.append(s3[i])
#         c+=1
#     j+=1
#     s3=[]
#
# print(c)
#완전 잘못접근함. 최소로 나올 수가 없음.
# 6
# 1 1
# 1 2
# 2 2
# 3 3
# 2 3
# 4 4
#위의 경우에는 6이 나와야하는데 4로 나옴. (1,1) (1,2)일 때 둘 다 스케줄이 되는데 위의 코드에서는
#제외됨.


import sys
n=int(input())
s1=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
s1.sort(key=lambda x:(x[1],x[0]))
j=0
c=0
end=0
while(j<n):
    if end<=s1[j][0]:
        end=s1[j][1]
        c+=1
        j+=1
    else:
        j+=1
print(c)
