
class TrieNode:

    def __init__(self):
        self.children = [None]*26
        self.wordEnd = False

class Trie:

    def __init__(self):
        self.root = self.getNode()
    
    def getNode(self):
        return TrieNode()

    def charToIndex(self, ch):
        return ord(ch)-ord('A')

    
    def insert(self, key):
        marker = self.root
        length = len(key)
        for level in range(length):
            index = self.charToIndex(key[level])
            if not marker.children[index]:
    
                marker.children[index] = self.getNode()
            
            marker = marker.children[index] 

        marker.wordEnd = True
    
    
    def search(self, key):
        marker = self.root
        length = len(key)
        for level in range(length):
            index  = self.charToIndex(key[level])
            if not marker.children[index]:
                return False 
            marker = marker.children[index] 
        return marker!=None and marker.wordEnd 


def isSafe(x, y, boggle, visit):
    N, M = len(boggle), len(boggle[0])
    return 0<=x<N and 0<=y<M and not visit[x][y]

def util(x, y, boggle, trie, res, visit):

    # print(res)
    if trie.wordEnd:
        print(res)
    
    if isSafe(x, y, boggle, visit):
        visit[x][y] = True

        for k in range(26):
            if trie.children[k]!=None:
                ch = chr(ord('A') + k )
                if isSafe(x+1, y+1, boggle, visit) and boggle[x+1][y+1]==ch:
                    util(x+1, y+1, boggle, trie.children[k], res + ch, visit)
                if isSafe(x-1, y-1, boggle, visit) and boggle[x-1][y-1]==ch:
                    util(x-1, y-1, boggle, trie.children[k], res + ch, visit)
                if isSafe(x+1, y, boggle, visit) and boggle[x+1][y]==ch:
                    util(x+1, y, boggle, trie.children[k], res + ch, visit)
                if isSafe(x-1, y, boggle, visit) and boggle[x-1][y]==ch:
                    util(x-1, y, boggle, trie.children[k], res + ch, visit)
                if isSafe(x, y+1, boggle, visit) and boggle[x][y+1]==ch:
                    util(x, y+1, boggle, trie.children[k], res + ch, visit)
                if isSafe(x, y-1, boggle, visit) and boggle[x][y-1]==ch:
                    util(x, y-1, boggle, trie.children[k], res + ch, visit)
                if isSafe(x+1, y-1, boggle, visit) and boggle[x+1][y-1]==ch:
                    util(x+1, y-1, boggle, trie.children[k], res + ch, visit)
                if isSafe(x-1, y+1, boggle, visit) and boggle[x-1][y+1]==ch:
                    util(x-1, y+1, boggle, trie.children[k], res + ch, visit)
        
        visit[x][y] = False

def solve(boggle, trie):
    N, M = len(boggle), len(boggle[0])
    visit = [[False for _ in range(M)] for _ in range(N)]

    res = ""

    t = Trie()

    for i in range(N):
        for j in range(M):
            index = t.charToIndex(boggle[i][j])
            if trie.children[index]:
                res += chr(ord('A') + index)
                util(i, j, boggle, trie.children[index], res, visit)
                res = ""
    
if __name__ == '__main__':
    keys = [ "GEEKS", "QUIZ"]
    trie = Trie()
    for key in keys:
        trie.insert(key)
    
    boggle = [ [ 'G', 'I', 'Z' ], 
                          [ 'U', 'E', 'K' ], 
                          [ 'Q', 'S', 'E' ] ]
    
    # output = ['no', 'yes']

    # print('there ', output[trie.search('there')])
    # print('their ', output[trie.search('their')])
    # print('the', output[trie.search('the')])

    solve(boggle, trie.root)