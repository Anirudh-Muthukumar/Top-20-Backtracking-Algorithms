# Word Break problem

# To check if given string can be really broken into words in dictionary
def breakable(s, words):
    d = [False] * len(s)
    for i in range(len(s)):
        for w in words:
            if w==s[i+1-len(w):i+1] and (d[i-len(w)] or i-len(w)==-1):
                d[i] = True
    return d[-1]

# Word Break function
def wordBreak(s, N, keys, res):
    if N==0:
        return
    
    for i in range(1, N+1):
        prefix = s[:i]
        if prefix in keys:
            if i==N:
                res += (' ' + prefix)
                print(res)
                return
            if res=='':
                wordBreak(s[i:], N-i, keys, res + prefix)
            else:
                wordBreak(s[i:], N-i, keys, res + ' ' + prefix)
if __name__ == '__main__':
    
 
    keys = ["i", "love", "man", "go", "mango", "icecream", "ice", "cream"]
    sent = "ilovemangoicecream"

    if breakable(sent, keys):
        wordBreak(sent, len(sent), keys, "")



            