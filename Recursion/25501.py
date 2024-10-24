#재귀의 귀재

import sys
def recursion(s,l,r,count):
    if l>=r:
        return 1,count
    elif s[l]!=s[r]:
        return 0,count
    else:
        count+=1
        return recursion(s,l+1,r-1,count)
    
def isPalindrome(s):
    count=1
    return recursion(s,0,len(s)-1,count)


t=int(sys.stdin.readline())

for i in range(t):
    s=list(sys.stdin.readline().strip())
    print(' '.join(map(str,isPalindrome(s))))