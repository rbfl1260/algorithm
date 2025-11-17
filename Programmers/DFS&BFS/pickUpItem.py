#아이템 줍기
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    arr=[[""]*102 for _ in range(0,102)]
    visited=[[False]*102 for _ in range(0,102)]
    q=deque()
    q.append([characterX*2,characterY*2,0])
    visited[characterX*2][characterY*2]=True
    for i in range(len(rectangle)):
        lx=rectangle[i][0]*2
        ly=rectangle[i][1]*2
        rx=rectangle[i][2]*2
        ry=rectangle[i][3]*2
         #1로 직사각형 채우기
         #상하 테두리
        for j in range(lx, rx+1):
            arr[j][ly] = 1
            arr[j][ry] = 1
        for k in range(ly, ry+1):
            arr[lx][k] = 1
            arr[rx][k] = 1

    for i in range(len(rectangle)):
        lx=rectangle[i][0]*2
        ly=rectangle[i][1]*2
        rx=rectangle[i][2]*2
        ry=rectangle[i][3]*2
        
        #테두리만 남기고 안쪽 0으로 채우기
        for j in range(lx+1,rx):
             for k in range(ly+1,ry):
                    arr[j][k]=0
 
    while q:
        x,y,count=q.popleft()
        if x==itemX*2 and y==itemY*2:
            return count//2
        for d_row,d_col in [[1,0],[-1,0],[0,1],[0,-1]]:
            new_row,new_col=x+d_row,y+d_col
            if 0<=new_row<102 and 0<=new_col<102 and not visited[new_row][new_col] and arr[new_row][new_col]==1:
                visited[new_row][new_col]=True
                q.append([new_row,new_col,count+1])
        
