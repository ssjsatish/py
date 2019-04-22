def printSolution(board,N):
    ans = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                ans.append(j+1)
    return ans
    

def printSolution1(board, N):
    ans = []
    for i in range(N):
        for x in range(N):
            if board[x][i] == 1:
                ans.append(x+1)
    return ans

def isSafe(board, row, col):   
    for i in range(col): 
        if board[row][i] == 1: 
            return False  
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)): 
        if board[i][j] == 1: 
            return False  
    for i,j in zip(range(row,N,1), range(col,-1,-1)): 
        if board[i][j] == 1: 
            return False  
    return True
    
def solveNQueen(board,N, col):
    if col== N:
        print(printSolution1(board,N))
        return True
    res = False
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            res = solveNQueen(board,N,col+1) or res
            board[i][col] = 0
    return res

for _ in range(int(input())):
    N = int(input())
    board = [[0 for i in range(N)] for j in range(N)]
    if solveNQueen(board, N, 0)==False:
        print(-1)
    else:
        continue
    