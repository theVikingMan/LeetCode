def twoSum(numbers, target):
  l, r = 0, len(numbers) - 1

  while l < r:
    curTotal = numbers[l] + numbers[r]
    if curTotal < target:
      l += 1
    elif curTotal > target:
      r -= 1
    else:
      return [l + 1, r + 1]

print(twoSum([2, 7, 11, 15], 9)) # [1, 2]
print(twoSum([2, 3, 4], 6)) # [1, 3]
print(twoSum([-1, 0], -1)) # [1, 2]

# --------------- Binary Search --------------- #
# def twoSum(numbers, target):
#   first = 0
#   while first <= len(numbers) - 2:
#     l, r = first + 1, len(numbers) - 1
#     while l <= r:
#       diff = target - numbers[first]
#       m = (l + r) // 2
#       if (diff - numbers[m]) == 0:
#         return [first + 1, m + 1]
#       elif (diff - numbers[m]) > 0:
#         l = m + 1
#       else:
#         r = m - 1
#     first += 1

# --------------- Using Extra Space --------------- #
# def twoSum(nums, target):
#   res = []
#   seen_nums = {}
#   for key, value in enumerate(nums):
#       other_value = target - value
#       if other_value in seen_nums:
#           res.append(seen_nums[other_value])
#           res.append(key + 1)
#           return res
#       else:
#           seen_nums[value] = key + 1