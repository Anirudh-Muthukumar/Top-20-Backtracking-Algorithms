dictionary = ["oath","pea","eat","rain"]

def solveUtil(x, y, visit, boggle, str):
    N = len(boggle)
    visit[x][y] = True

    str = str + boggle[x][y]

    if str in dictionary:
        print(str)

    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if 0<=i<N and 0<=j<N and not visit[i][j]:
                solveUtil(i, j, visit, boggle, str)
    
    str = str[-1]
    visit[x][y] = False

def solve(boggle):
    N = len(boggle)
    visit = [ [False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            solveUtil(i, j, visit, boggle, "")

if __name__ == '__main__':
    boggle = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
    
    solve(boggle)