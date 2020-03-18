

def isSafe(x, y, grid, digit):
    # check if digit is already present in 3x3 grid
    row, col = x - x % 3, y - y % 3
    for i in range(3):
        for j in range(3):
            if grid[i+row][j+col]==digit:
                return False
    
    # check if digit is already present in row/col
    for i in range(len(grid)):
        if grid[i][y]==digit or grid[x][i]==digit:
            return False
    
    return True

def findUnassignedCell(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return i, j
    return -1, -1

def solve(grid):

    # find an unassigned cell
    row, col = findUnassignedCell(grid)

    if row==-1:
        # solution found
        return True

    # try all digits
    for digit in range(1, 10): 
        # check if digit is safe for filling
        if isSafe(row, col, grid, digit):
            grid[row][col] = digit
            if solve(grid):
                return True
            grid[row][col] = 0 # backtrack
    
    return False

if __name__ == '__main__':
    grid=[[3,0,6,5,0,8,4,0,0], 
          [5,2,0,0,0,0,0,0,0], 
          [0,8,7,0,0,0,0,3,1], 
          [0,0,3,0,1,0,0,8,0], 
          [9,0,0,8,6,3,0,0,5], 
          [0,5,0,0,9,0,6,0,0], 
          [1,3,0,0,0,0,2,5,0], 
          [0,0,0,0,0,0,0,7,4], 
          [0,0,5,2,0,6,3,0,0]] 
    
    if solve(grid):
        print("\nSolution : ")
        for row in grid:
            print(row)
    else:
        print("Solution does not exists!!")
    print()