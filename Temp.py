
def solve(grid):
    m, n = len(grid), len(grid[0])
    sol = [[0 for _ in range(n)] for _ in range(m)]
    if grid[0][0]==0:
        sol[0][0] = 1

    # initializing first row and col
    for i in range(1, n):
        if grid[0][i]==0:
            sol[0][i] = sol[0][i-1]
    
    for i in range(1, m):
        if grid[i][0]==0:
            sol[i][0] = sol[i-1][0]
    
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j]==0:
                sol[i][j] = sol[i][j-1] + sol[i-1][j]
    
    print("# of ways:", sol[-1][-1])
    

if __name__ == '__main__':
    maze = [[0, 0, 0], [0, 1, 0], [0, 0, 0]] 
    
    solve(maze)