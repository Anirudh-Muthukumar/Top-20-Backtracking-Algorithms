# 79. Word Search Leetcode


def solveUtil(x, y, board, word):
    
    if len(word)==0:
        return True
    
    if not(0<=x<len(board)) or not(0<=y<len(board[0])) or word[0]!=board[x][y]:
        return False
    
    # To avoid repeating of characters
    temp = board[x][y]
    board[x][y] = '#'

    res = solveUtil(x-1, y, board, word[1:]) or solveUtil(x+1, y, board, word[1:]) or solveUtil(x, y-1, board, word[1:]) or solveUtil(x, y+1, board, word[1:])

    board[x][y] = temp # backtrack

    return res

def solve(board, word):

    if not board:
        return False
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if solveUtil(i, j, board, word):
                return True
    
    return False

if __name__ == '__main__':
    board = [   ['A','B','C','E'],
                ['S','F','C','S'],
                ['A','D','E','E']
            ]
    word = "ABCCED"
    print(solve(board, word))