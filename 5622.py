# 다이얼

S=input()
dial=[['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
sum=0
for i in range(len(S)):
    for k in range(len(dial)):
        if S[i] in dial[k]:
            sum+=k+3
print(sum)
            