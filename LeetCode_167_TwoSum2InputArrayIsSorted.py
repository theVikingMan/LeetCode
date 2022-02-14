def twoSum(nums, target):
    res = []
    seen_nums = {}
    for key, value in enumerate(nums):
        other_value = target - value
        if other_value in seen_nums:
            res.append(seen_nums[other_value])
            res.append(key + 1)
            return res
        else:
            seen_nums[value] = key + 1


print(twoSum([2, 7, 11, 15], 9))
# [1, 2]

print(twoSum([2, 3, 4], 6))
# [1, 3]

print(twoSum([-1, 0], -1))
# [1, 2]
