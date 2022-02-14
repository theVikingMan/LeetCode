def shuffle(nums, n):
    res = []

    for i in range(n):
        res.append(nums[i])
        res.append(nums[i+n])
    return res

print(shuffle([2,5,1,3,4,7], 3))


# Option 2
def shuffle1(nums,n):
    return [j for i in zip(nums[:n], nums[n:]) for j in i]

print(shuffle1([2,5,1,3,4,7], 3))