global N
N = 4
def printSolution(board):
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

def solveNQueen(board, col):
    if col== N:
        print(printSolution(board))
        return True
    res = False
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            res = solveNQueen(board,col+1) or res
            board[i][col] = 0
    return res


def solveNQ():
    board = [[0 for i in range(N)] for j in range(N)]
    if solveNQueen(board, 0)==False:
        print('Solution does not exist')
        return False    
    return True

solveNQ()

    
