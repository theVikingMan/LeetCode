
# Best Solution
def twoSum(nums: int, target: int) -> int:
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i


print(twoSum([2, 7, 11, 15], 9))


# Better solution

# def twoSum(nums, target):
#     new_map = {}
#     for i in range(len(nums)):
#         new_map[nums[i]] = i
#     for i in range(len(nums)):
#         complet = target - nums[i]
#         if complet in new_map and new_map[complet] != i:
#             return i, new_map[complet]


# Brute force method

# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target and i != j:
#                 return i, j

# print(twoSum([2, 7, 11, 15], 9))
