#행렬덧셈

n,m=map(int,input().split())

data=[list(map(int,input().split())) for _ in range(2*n)]

A=data[:n]
B=data[n:]

res=[[A[i][j]+B[i][j] for j in range(m)] for i in range(n)]

for row in res:
    print(" ".join(map(str,row)))