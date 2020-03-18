

def isSafe(x, y, maze):
    N = len(maze)
    return 0<=x<N and 0<=y<N and maze[x][y]==1

def solveUtil(sol, x, y, maze):
    N = len(maze)
    if x==N-1 and y==N-1:
        sol[x][y] = 1
        return True
    

    if isSafe(x, y, maze):
        
        sol[x][y] = 1

        # take one tentative horizontal step
        if solveUtil(sol, x+1, y, maze):
            return True
        
        # take one tentative vertical step
        if solveUtil(sol, x, y+1, maze):
            return True

        sol[x][y] = 0
        return False


def solveMaze(maze, x, y):
    sol = [ [0 for _ in range(len(maze))] for _ in range(len(maze[0]))]

    if not solveUtil(sol, 0, 0, maze):
        print("Solution does not exists!!!")
        return False

    
    print("Solution : ")
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            print(sol[i][j], end = ' ')
        print()

    return True


if __name__ == '__main__':

    maze = [ [1, 0, 0, 0], 
                [1, 1, 0, 1], 
                [0, 1, 0, 0], 
                [1, 1, 1, 1] ] 

    solveMaze(maze, 0, 0)