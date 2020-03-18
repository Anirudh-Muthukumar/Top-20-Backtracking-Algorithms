def util(nums, path, res):
    if not nums:
        res.append(path)
        return
    
    for i in range(len(nums)):
        util(nums[:i] + nums[i+1:], path + [nums[i]], res)

res = []
util([3, 2, 1], [], res)
print(res)


