# 크로아티아 알파벳

S=input()
alphabet=['c=','c-','dz=','d-','lj','nj','s=','z=']
wordCount=0

for i in alphabet:
    S=S.replace(i,'*')
print(len(S))