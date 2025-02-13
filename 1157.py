#단어 공부

s=input()
s=s.upper()
alphabet=[]
for i in range(65,91):
    alphabet.append(chr(i))
wordCount=[]
for i in alphabet:
    wordCount.append(s.count(i))

if(wordCount.count(max(wordCount))>1):
    print("?")
else:
    print(alphabet[wordCount.index(max(wordCount))])
    