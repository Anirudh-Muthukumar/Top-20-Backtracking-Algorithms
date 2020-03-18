

def isValid(string):
    ct = 0
    for ch in string:
        if ch=='(':
            ct+=1
        elif ch==')':
            ct-=1
        if ct<0:
            return False
    return ct==0

def removeValidParenthesis(string):

    if len(string)==0:
        return

    # Use BFS with backtracking
    queue = []
    visited = set()
    temp = 0
    level = 0

    queue.append(string)
    visited.add(string)

    while len(queue):
        string = queue[0]
        queue.pop(0)

        # print(queue)
        if isValid(string):
            print(string)
            level = True
        
        if level: # minimum number of paranthesis to be removed, so do not disturb an already valid string
            continue
            
        for i in range(len(string)):
            if string[i] in ['(', ')']:
                temp = string[:i] + string[i+1:] # remove parenthesis in current position
                if temp not in visited:
                    visited.add(temp)
                    queue.append(temp)


if __name__ == '__main__':

    string = "()())()"
    removeValidParenthesis(string)