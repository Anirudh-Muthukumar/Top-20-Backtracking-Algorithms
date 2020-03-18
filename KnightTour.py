import numpy as np

moveX = [1, 1, 2, 2, -1, -1, -2, -2]
moveY = [2, -2, 1, -1, 2, -2, 1, -1]

def isEmpty(x, y, board, N):
    return 0<=x<N and 0<=y<N and board[y*N+x]==-1

ct = 0

def getDegree(x, y, board, N):
    count = 0
    for i in range(8):
        if isEmpty(x + moveX[i], y + moveY[i], board, N):
            count += 1
    return count

def nextMove(x, y, board, N):
    
    min_degree_index = -1
    min_degree = N+1

    start_index = np.random.randint(N)

    for i in range(8):
        index = (start_index + i) % N
        next_x = x + moveX[index]
        next_y = y + moveY[index]
        degree = getDegree(next_x, next_y, board, N)

        if isEmpty(next_x, next_y, board, N) and degree < min_degree:
            min_degree_index = index
            min_degree = degree
    
    if min_degree_index == -1:
        return None, None, False
    
    new_x = x + moveX[min_degree_index]
    new_y = y + moveY[min_degree_index]

    board[new_y * N + new_x] = board[y * N + x] + 1

    return new_x, new_y, board


def neighbor(x, y, xx, yy):
    for i in range(8):
        if (x+moveX[i])==xx and (y+moveY[i])==yy:
            return True
    return False

def display(board):
    n = int(len(board)**0.5)
    for i in range(n):
        for j in range(n):
            print(board[j*n+i], end = ' ')
        print()

def solveKT(N):
    global ct
    board = [-1 for _ in range(N*N)]
    start_x, start_y = np.random.randint(N), np.random.randint(N)

    x, y = start_x, start_y

    board[y*N+x] = 1

    for i in range(2, N*N+1):
        x, y, board = nextMove(x, y, board, N)
        if board is None:
            return False
    
    ct += 1
    print(ct)
    if not neighbor(x, y, start_x, start_y):
        return False
    
    print("Solution : ")
    display(board)
    return True

if __name__ == '__main__':
    size = 8
    while not solveKT(size):
        # continue until a solution is found by choosing another random starting point
        continue

