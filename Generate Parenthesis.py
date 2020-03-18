
def generate(p, left, right, parens = []):

    if left:
        generate( p + '(', left-1, right)
    if right > left:
        generate(p + ')', left, right-1)
    if not right:
        parens += [p]
    return parens


if __name__ == '__main__':
    n = 4
    ans = generate('', n, n)
    print(ans)
