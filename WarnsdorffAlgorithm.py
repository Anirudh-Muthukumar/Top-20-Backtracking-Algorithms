# Warnsdorff algorithm for knight tour problem
import numpy as np

moveX = [1, 1, 2, 2, -1, -1, -2, -2]
moveY = [2, -2, 1, -1, 2, -2, 1, -1]

def isEmpty(x, y, board, N):
    return 0<=x<N and 0<=y<N and board[y*N+x]<0  

def getDegree(x, y, board, N):
    # returns the degree of given position = accessible indices from given position
    count = 0
    for i in range(N):
        if isEmpty(x + moveX[i], y + moveY[i], board, N):
            count+=1
    return count

def nextMove(x, y, board, N):
    min_deg_index, min_degree = -1, N+1
    start = np.random.randint(N)

    for i in range(N):
        index = (start + i) % N
        next_x = x + moveX[index]
        next_y = y + moveY[index]
        degree = getDegree(next_x, next_y, board, N)
        if isEmpty(next_x, next_y, board, N) and degree < min_degree:
            # print(next_x, next_y)
            min_deg_index = index
            min_degree = degree
    
    # if not found
    if min_deg_index == -1:
        return None, None, False
    
    new_x = x + moveX[min_deg_index]
    new_y = y + moveY[min_deg_index]

    # update knight step at new position
    board[new_y * N + new_x] = board[y*N+x] + 1
    
    # return the updated values
    return new_x, new_y, board


def neighbor(x, y, xx, yy, N):
    for i in range(N):
        if (x+moveX[i])==xx and (y+moveY[i])==yy:
            return True
    return False 

def display(board):
    for i in range(8):
        for j in range(8):
            print(board[i*8+j], end = ' ')
        print()

def findClosedTour(N):

    # create an array for board
    board = [-1 for _ in range(N*N)]

    # start from random index
    start_x = np.random.randint(N)
    start_y = np.random.randint(N)
    # start_x = 4
    # start_y = 0

    x, y = start_x, start_y


    # mark the first knight move
    board[y*N+x] = 1

    # Keep picking next position using Warnsdorff heuristic
    for i in range(N*N-1):
        x, y, board= nextMove(x, y, board, N)
        if board is None:
            return False
        
    
    # Check if tour is closed 
    if not neighbor(x, y, start_x, start_y, N):
        return False
    
    # Print the solution
    print("Solution : ")
    display(board)
    return True


if __name__ == '__main__':
    size = 8
    while not findClosedTour(size):
        continue


