def threeSum(self, nums):
  res = []
  nums.sort()

  for idx, a in enumerate(nums):
    if idx > 0 and a == nums[idx - 1]:
      continue

    l, r = idx + 1, len(nums) - 1
    while l < r:
      threeSum = a + nums[l] + nums[r]
      if threeSum > 0:
        r -= 1
      elif threeSum < 0:
        l += 1
      else:
        res.append([a, nums[l], nums[r]])
        idx += 1
        while nums[l] == nums[l - 1] and l < r:
          l += 1
  return res

print(threeSum([-1,0,1,2,-1,-4]))