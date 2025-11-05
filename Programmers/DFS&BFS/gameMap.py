from collections import deque

def solution(maps):
    H=len(maps)
    W=len(maps[0])
    visited=[[False]*W for _ in range(H)]
    q=deque()
    q.append([0,0,1])
    visited[0][0]=True

    while q:
        row,col,distance=q.popleft()
        if row==H-1 and col==W-1:
            return distance
        for d_row,d_col in [[1,0],[-1,0],[0,1],[0,-1]]:
            new_row,new_col=row+d_row,col+d_col
            if 0<=new_row<H and 0<=new_col<W and not visited[new_row][new_col] and maps[new_row][new_col]==1:
                visited[new_row][new_col]=True
                q.append([new_row,new_col,distance+1])
    return -1