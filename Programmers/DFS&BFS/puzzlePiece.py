def solution(game_board, table):
    answer = 0
    
    visited_board=[[False]*len(game_board[0]) for _ in range(len(game_board))]
    visited_table=[[False]*len(game_board[0]) for _ in range(len(game_board))]
    boardPieces=[]
    #보드의 빈칸 찾는 코드(0으로 채워진 부분)
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if game_board[i][j]==0 and not visited_board[i][j]:
                boardPiece=[]
                dfs_board(i,j,game_board,visited_board,boardPiece)
                boardPieces.append(boardPiece)

    #테이블의 채워진 부분 찾는 코드(1로 채워진 부분)          
    tablePieces=[]
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j]==1 and not visited_table[i][j]:
                tablePiece=[]
                dfs_table(i,j,table,visited_table,tablePiece)
                tablePieces.append(tablePiece)

    rotation_pieces=[]
    for i in range(len(tablePieces)):
        rotations=[
            nom(tablePieces[i]),rotate90(tablePieces[i]),rotate180(tablePieces[i]),rotate270(tablePieces[i])]
        rotation_pieces.append(rotations)

    nom_board=[]
    for i in range(len(boardPieces)):
        hole=nom(boardPieces[i])
        nom_board.append(hole)
        
    for i in nom_board:
        sorted_board=sorted(i)
        matched=False
        for idx,rotated in enumerate(rotation_pieces):
            if rotated is None:
                continue
            for shape in rotated:
                if sorted_board==sorted(shape):
                    matched=True
                    break
            if matched:
                break
        if matched:
            answer+=len(i)
            rotation_pieces[idx]=None

    return answer

#보드 빈칸하나씩 찾아서(연결된 하나의 덩어리) 리턴
def dfs_board(x,y,board,visited,piece):
    visited[x][y]=True
    piece.append((x,y)) 
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx,ny=x+dx,y+dy
        if 0<=nx<len(board) and 0<=ny<len(board[0]) and not visited[nx][ny] and board[nx][ny]==0:
            dfs_board(nx,ny,board,visited,piece)

#테이블 채워진 부분(연결된 하나의 덩어리) 찾아서 리턴
def dfs_table(x,y,table,visited,piece):
    visited[x][y]=True
    piece.append((x,y))
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx,ny=x+dx,y+dy
        if 0<=nx<len(table) and 0<=ny<len(table[0]) and not visited[nx][ny] and table[nx][ny]==1:
            dfs_table(nx,ny,table,visited,piece)

def rotate90(piece):
    rotated=[(y,-x) for x,y in piece]
    return nom(rotated)

def rotate180(piece):
    rotated=[(-x,-y) for x,y in piece]
    return nom(rotated)
def rotate270(piece):
    rotated=[(-y,x) for x,y in piece]
    return nom(rotated)

def nom(rotated):
    min_x=min(x for x,y in rotated)
    min_y=min(y for x,y in rotated)
    normalized=[(x-min_x,y-min_y) for x,y in rotated]
    return normalized