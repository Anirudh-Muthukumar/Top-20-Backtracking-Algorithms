count = None

def isSafe(row, col, board, N):
    
    for j in range(N):
        if board[row][j]==1:
            return False

    for i, j in zip(range(row,-1, -1), range(col, -1, -1)):
        if board[i][j]==1:
            return False
    
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]==1:
            return False
    
    return True

def solveNQUtil(col, board, N):
    if col==N:
        print("Solution : ")
        for i in range(N):
            print(board[i])
        return True 
    
    res = False

    # check for each row in given column
    for i in range(N):
        if isSafe(i, col, board, N):
            board[i][col] = 1
            res = solveNQUtil(col+1, board, N) or res
            board[i][col] = 0
    
    return res

def solveNQ(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    count = 1
    if not solveNQUtil(0, board, N):
        print("No solution exists!")

    return  
    
if __name__ == '__main__':
    size = 4
    solveNQ(size)