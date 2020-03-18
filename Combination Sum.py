def combinationSum(List, target):
    res = []
    util(List, target, 0, [], len(List), res)
    # return res
    print(res)

def util(List, target, index, path, N, res):

    if target < 0:
        return # backtrack
    
    if target==0:

        # combination sum I
        res.append(path)

        # combination sum II
        # path.sort()
        # if path not in res:
        #     res.append(path)
        return
    
    for i in range(index, N):
        util(List, target-List[i], i+1, path + [List[i]], N, res)


List = [10,1,2,7,6,1,5]
target = 8
combinationSum(List, target)