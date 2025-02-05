#벌집

n=int(input())
minCount=1
start=2

if n==1:
    print(1)
else:
    while True:
        count=6*minCount
        
        if start<=n<start+count:
            print(minCount+1)
            break
        minCount+=1
        start+=count
    
