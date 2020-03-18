
dictionary = [ str(i) for i in range(0, 256)]

def validIP(string):
    ct = 0
    for ch in string:
        if ch=='.':
            ct+=1
    return ct==3

def generateIPUtil(string, N, result):
    if N==0:
        return

    for i in range(1, N+1):
        prefix = string[:i]
        if prefix in dictionary:
            if i==N:
                result += ('.' + prefix)
                if validIP(result):
                    print(result)
                return
            if result=="":
                generateIPUtil(string[i:], N-i, result + prefix)
            else:
                generateIPUtil(string[i:], N-i, result + '.' + prefix)


def generateIP(string):
    return generateIPUtil(string, len(string), "")

if __name__ == '__main__':
    string = '11211'
    generateIP(string)